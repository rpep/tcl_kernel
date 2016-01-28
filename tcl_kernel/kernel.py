from ipykernel.kernelbase import Kernel
import textwrap
try:
    import Tkinter
except ImportError:
    import tkinter as Tkinter
__version__ = '0.0.1'


class TclKernel(Kernel):
    implementation = 'tcl_kernel'
    implementation_version = __version__
    language_info = {'name': 'Tcl',
                     'codemirror_mode': 'Tcl',
                     'mimetype': 'text/x-script.tcl',
                     'file_extension': '.tcl'}
    banner = "Tcl Kernel"

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.tcl = Tkinter.Tcl()
        self.execution_count = 0
        putsredef = textwrap.dedent("""\
                  rename puts original_puts 
                  proc puts {args} {
                      if {[llength $args] == 1} {
                          return "=> [lindex $args 0]"
                      } else {
                          eval original_puts $args
                      }
                  }""")
        self.tcl.eval(putsredef)

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        try:
            output = self.tcl.eval(code.rstrip())
            if not silent:
                stream_content = {'name': 'stdout', 'text': output[3:]}
                self.send_response(self.iopub_socket, 'stream', stream_content)
        except Tkinter.TclError as scripterr:
            output = "Tcl Error: " + scripterr.args[0]
            if not silent:
                stream_content = {
                    'name': 'stderr', 'text': output}
                self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count,
                'payload': [], 'user_expressions': {}}
