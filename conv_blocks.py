import contextlib 
import tf_slim as slim 
import functools
import tensorflow.compat.v1 as tf

def _fixed_padding(inputs, kernel_size, rate=1): 
  """Pads the input along the spatial dimensions independently of input size.

  Pads the input such that if it was used in a convolution with 'VALID' padding,
  the output would have the same dimensions as if the unpadded input was used
  in a convolution with 'SAME' padding.

  Args:
    inputs: A tensor of size [batch, height_in, width_in, channels].
    kernel_size: The kernel to be used in the conv2d or max_pool2d operation.
    rate: An integer, rate for atrous convolution.

  Returns:
    output: A tensor of size [batch, height_out, width_out, channels] with the
      input, either intact (if kernel_size == 1) or padded (if kernel_size > 1).
  """

  kernel_size_effective = [kernel_size[0] + (kernel_size[0] - 1) * (rate - 1),
                           kernel_size[1] + (kernel_size[1] - 1) * (rate - 1)]
  pad_total = kernel_size_effective[0] - 1, kernel_size_effective[1] - 1
  