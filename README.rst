========================
A Jupyter Kernel for Tcl
========================

This uses the version of Tcl that comes with Python, through Tkinter, so you do not need to install anything else.

Note: Requires Python 3!

Install via:

    pip3 install tcl_kernel
    
    python3 -m tcl_kernel.install
    
To use try one of these:
    - jupyter notebook
        - Then select the Tcl option in the 'New' section
    - jupyter qtconsole --kernel tcl
    - jupyter console --kernel tcl


For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_.
Copyright 2015-2016 Ryan Pepper, Thomas Kluyver, Hans Fangohr, University of Southampton.

This work was supported by an EPSRC Doctoral Training Centre grant (EP/L015382/1).

I do not have time to add functionality to this project anymore but will happily review and merge pull requests to add new features/fix bugs.
