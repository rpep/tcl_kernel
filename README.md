
# tcl_kernel - A Jupyter Kernel for Tcl

![PyPi](https://img.shields.io/pypi/v/tcl_kernel)
![Python Version 3](https://img.shields.io/pypi/pyversions/tcl_kernel)

This uses the version of Tcl that is used within Python, through Tkinter, so you do not need to install anything else.

Install via:

```bash
    pip3 install tcl_kernel
    python3 -m tcl_kernel.install
```

To use try one of these:
* `jupyter notebook`
    * Then select the Tcl option in the 'New' section
* `jupyter qtconsole --kernel tcl`
* `jupyter console --kernel tcl`

For details of how this works, see the Jupyter docs on [wrapper kernels](http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html)


Copyright 2015-2021 Ryan Pepper, Thomas Kluyver, Hans Fangohr, University of Southampton. This work was supported by an EPSRC Doctoral Training Centre grant (EP/L015382/1)
