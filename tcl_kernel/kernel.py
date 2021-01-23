from ipykernel.kernelbase import Kernel
from contextlib import contextmanager
import os
import sys
import tempfile
import platform
import ctypes

OS = platform.platform()
libc = ctypes.CDLL(None)
if 'Darwin' in OS:
    c_stdout = ctypes.c_void_p.in_dll(libc, '__stdoutp')
elif 'macOS' in OS:
    c_stdout = ctypes.c_void_p.in_dll(libc, '__stdoutp')
elif 'Linux' in OS:
    c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')

else:
    print("""Your OS is not currently compatible with this Kernel \n
             Please make an issue here: \n
             https://github.com/ryanpepper/tcl_kernel
             """)
try:
    import io
    import Tkinter
except ImportError:
    import tkinter as Tkinter
__version__ = '0.0.4'


@contextmanager
def stdout_redirector(stream):
    # The original fd stdout points to. Usually 1 on POSIX systems.
    original_stdout_fd = sys.__stdout__.fileno()

    def _redirect_stdout(to_fd):
        """Redirect stdout to the given file descriptor."""
        # Flush the C-level buffer stdout
        libc.fflush(c_stdout)
        # Flush and close sys.stdout - also closes the file descriptor (fd)
        sys.stdout.close()
        # Make original_stdout_fd point to the same file as to_fd
        os.dup2(to_fd, original_stdout_fd)
        # Create a new sys.stdout that points to the redirected fd
        sys.stdout = io.TextIOWrapper(os.fdopen(original_stdout_fd, 'wb'))

    # Save a copy of the original stdout fd in saved_stdout_fd
    saved_stdout_fd = os.dup(original_stdout_fd)
    try:
        # Create a temporary file and redirect stdout to it
        tfile = tempfile.TemporaryFile(mode='w+b')
        _redirect_stdout(tfile.fileno())
        # Yield to caller, then redirect stdout back to the saved fd
        yield
        _redirect_stdout(saved_stdout_fd)
        # Copy contents of temporary file to the given stream
        tfile.flush()
        tfile.seek(0, io.SEEK_SET)
        stream.write(tfile.read())
    finally:
        tfile.close()
        os.close(saved_stdout_fd)


class TclKernel(Kernel):

    implementation = 'tcl_kernel'
    implementation_version = __version__
    language_info = {"name": "Tcl",
                     "codemirror_mode": {
                         "version": 2,
                         "name": "text/x-tcl"
                     },
                     "mimetype": "text/x-tcl",
                     "file_extension": ".tcl"}

    _banner = "Tcl Kernel"

    @property
    def banner(self):
        if self._banner is None:
            banner_undecoded = self._run_code('puts [info patchlevel]')
            self._banner = banner_undecoded.decode('utf-8')
        return self._banner

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.tcl = Tkinter.Tcl()
        self.execution_count = 0

    def _run_code(self, code, decodestr='utf-8'):
        temp_stdout_stream = io.BytesIO()
        stderr_output = None
        returnval = ''
        with stdout_redirector(temp_stdout_stream):
            try:
                returnval = self.tcl.eval(code)
            except Tkinter.TclError as scripterr:
                stderr_output = scripterr.args[0]
        output = temp_stdout_stream.getvalue()
        temp_stdout_stream.close()
        return (output.decode(decodestr) + returnval,
                stderr_output)

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        output, stderr_output = self._run_code(code)

        if not silent:
            stream_content = {
                'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            if stderr_output:
                stream_content = {
                    'name': 'stderr', 'text': stderr_output}
                self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count,
                'payload': [], 'user_expressions': {}}
