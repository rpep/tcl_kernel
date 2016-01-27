from ipykernel.kernelbase import Kernel
import tkinter
__version__ = '0.0.1'

class TclKernel(Kernel):
    implementation = 'tcl_kernel'
    implementation_version = __version__
    language_info = {'name': 'bash',
                     'codemirror_mode': 'shell',
                     'mimetype': 'text/x-script.tcl',
                     'file_extension': '.tcl'}

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        try:
            self.tcl = tkinter.Tcl()

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        
        output = self.tcl(code.rstrip())
        
        if not silent:
            stream_content = {'name': 'stdout', 'text': code}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count,
                    'payload': [], 'user_expressions': {}}

