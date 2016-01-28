from ipykernel.kernelapp import IPKernelApp
from .kernel import TclKernel
IPKernelApp.launch_instance(kernel_class=TclKernel)
