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

- If you don't flip it backwards you are doing `cross-correlation`. Technically in the time domain, you could avoid flipping the kernel and do the convolution with cross-correlation, although it's not recommended.

- The **intuitive reason** why the kernel is flipped is because when you design a kernel you do it from you perspective and think applying left to right. From the signal perspective, if you need to apply the kernel on previous data, the kernel has to run backwards, and to be run correclty it needs to be flipped. So when you apply your kernel in reality the kernel runs forward but flipped. Also, the **convolution theorem** states that it needs to be flipped. This is because this implementation seen in time-domain can be implemented in the frequency-domain by `element wise multiplication of the Fourier spectra on both signal and kernel`.

## Convolution Theorem

- `Convolution theorem` states that the `FT` of a convolution of two signals, is the product of their `FT`. So basically doing convolution and then taking the FT of the convolved signal is the same as taking the FT of the signals and multiply them element-wise (IFT to go back to time domain).

- The result of convolution is the same as taking the IFFT of the spectral coefficients multiplied element wise. This means that you can implement convolution without doing the sliding dot product in the time domain --> FT of signal and kernel, element-wise multiplication --> IFFT.

- Advantages:
1) Convolution is rather slow, FT is fast
2) Convolution is less efficient computationally
3) Gives you a different intuition of why convolution seems like a narrowband filtering.

- Regarding the third point, the convolution with a specific kernel (`morlet wavelet` --> sine wave * gaussian) is the same thing as narrowband filtering. The power spectrum of the wavelet looks like a gaussian that peaks at some frequency and tapers off to 0, and therefore when multiplied with the power spectrum of the signal, is non-zero under the gaussian. This means the signal gets filtered outside the frequencies of the gaussian where there is zero eenergy in the kernel spectrum. 

## Convolution as Spectral multiplication

- As convolution is basically a low pass filtering, it'll also have edge effects. This is because the power spectrum of the gaussian (kernel) covers only the lower frequency and therefore the rest is attenuated. A wider gaussian kernel is even more narrow in the power spectrum and attenuates more. When you multiply the power spectra, where the gaussian in zero the signal in basically filtered out. 

##  Narrowband filtering with convolution and freq-domain Gaussian

- This is differnt from `time-domain` gaussian, as we've seen before, that is always a `low pass` filter. Creating a gaussian in the frequency domain gives you a narrow band filter when going back to the time domain using convolution implemented in the frequeny domain

- Convolution with frequency-domain gaussian != convolution with time-domain gaussian

- Computing a gaussian in the frequency domain is slightly different:
_____________________
$$\Large g = e^{-.5((h-p)/s)^2}$$
_____________________

where $\large s$ is 
_____________________
$$\Large s = \frac{w(2 \pi -1)}{4 \pi}$$
_____________________

$\large h$ = frequencies (Hz), $\large p$ = peak frequency (Hz) and $\large w$ = FWHM (Hz). The FWHM now is how wide is the gaussian but in the frequency domain (not the Hz units)

## Conv with frequency-domain Planck taper (bandpass filt)

- `Planck taper`, kinda looks like a gaussian, starts and ends at 0, kinda peaks at a certain frequencies. It has a rapid but smooth increase and decrease.
The difference with a gaussian is that when it reaches the maximum, it plateaus there for a certain range of frequencies, and then decrease again. It's a piecewise function, a system of three equations:
1) left side
2) center, plateau
3) right side 

Left and right side are `sigmoid functions`, increasing on the left and decreasing on the right. $\large \epsilon$ determines the increase/decrease (steepness) of the functions.