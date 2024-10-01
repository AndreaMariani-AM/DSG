# [06_convolution_notebook]()

## Time-Domain Convolution

- A `convolution` is a way to combine two time series to create a third time series. Can happen in 2D in the case of images. For semplicity, the two time series are usually referred to as the `signal` (the "interesting" time series) and the `kernel` (usually the filter). The output of the convolution is a time series composed of a mixture of features of the signal and the kernel. 

- Usually the convolution result is a smoothed version of the original signal (but mostly depends on the type of kernel used).

- Convolution in the `time-domain` is different from convolution in the `frequency-domain` (convolution theorem). Convolution uses the `dot-product` 
_____________________
$$\Large \alpha = a^Tb = \sum_{i=1}^n a_i b_i  $$ 
_____________________

between the two time series.

- Convolution in `time-domain`:
1) Line up data and kernel such as right most point in the kernel is lined up with left most point in the data.
2) Add zero padding to the signal to reach `len(kernel)-1`. This is necessary to have the two vectors with the same length to computed the dot-product
3) The result of the convolution, a scalar, goes into the convolution result array at index corresponding to center of the kernel
4) Move the kernel one step (which is the sampling rate for a time series) and repeat
5) last step is when right most point in the signal (without counting the zero padding) is aligned with the left most point in the kernel.

- An interesting property of convolution is that the length of the output is greater than the original two time series, in generale is the length of the signal and kernel summed, minus one.

- Lastly, the convolution kernel is actually `flipped backwards` when perfomring convolution. More in this later

## Flipped Kernel

- As said before, when doing convolution you take your kernel, flip it backwards and them do a sliding dot-product over the signal.

- If you don't flip it backwards you are doing `cross-correlation`. Technically in the time domain, you could avoid flipping the kernel and do the convolution with cross-correlation