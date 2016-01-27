A Jupyter Kernel for Tcl

This uses the version of Tcl that comes with Python, through Tkinter, so you do not need to install anything else.

To install::

    pip install tcl_kernel
    python -m tcl_kernel.install

To use it, run one of:

.. code:: shell

    jupyter notebook
    # In the notebook interface, select Bash from the 'New' menu
    ipython qtconsole --kernel Tcl
    ipython console --kernel Tcl

For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_, and

Huge thanks to Thomas Kluyver (@takluyver) who's Jupyter bash kernel (<https://github.com/takluyver/bash_kernel>) I 
modified to get this working.
