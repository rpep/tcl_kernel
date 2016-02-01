========================
A Jupyter Kernel for Tcl
========================

This uses the version of Tcl that comes with Python, through Tkinter, so you do not need to install anything else.

Not packaged up to pip yet, so to test out, clone the repository:
::
    git clone https://github.com/ryanpepper/tcl_kernel.git
    jupyter kernelspec install tcl_kernel
    cd tcl_kernel
    jupyter console --kernel tcl_kernel


For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_, and

Huge thanks to Thomas Kluyver (@takluyver) who's `Jupyter bash kernel <https://github.com/takluyver/bash_kernel>`_ I 
made heavy use of to get this working.
