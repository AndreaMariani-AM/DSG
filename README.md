# Collection of notes for Udemy course on Digital Signal Processing (DSG)

This repo contains exercises from the [Udemy course on Signal Processing](https://www.udemy.com/course/signal-processing/?couponCode=JUST4U02223). Courses files aren't synched and can be found [here](https://github.com/mikexcohen/SignalProcessing/tree/main).  

_____________________


Signal processing =  decision-making + tools

Tools are mostly generic, decisions are specific
Some tools:
- Temporal Filters
- Convolution
- Wavelets transforms
- Spectral analysis (FFT) --> frequency and time frequency
- Cleaning/Denoising
- Resampling (up and downsampling)
- Interpolation and extrapolation
- Feature detection
- SNR/RMS


# [02_ts_denoising]()

## Smoothing Filter

- Running-mean or mean-smoothing filter. Sets each data point in the smoothed version as the mean of `n` points in the surroundings. How much you go before and after (forward and backwards in time) is called **order** of the filter (`k`), crucial param. Works best when noise is *gaussian*, not applicable everywhere.  $$\Large y_t = (2k + 1)^{-1} \sum_{i=t-k}^{t+k} x_i$$

- This filter is applied in the time domain (smoothed over x-coord). With convolution and spectral multiplication you can apply a smoothing filter in the frequency domain (y-coord??)

- The larger `k`, the smoother the time series.  

- Applying any temporal filters causes a **edge effect**, aka edges usually don't have any values being the last and the first `nth` points (depending on `k`). Either set them as the original values or ignore them and filter them out.  

- Sampling Rate: measured in Hz, is the avg number of samples obtained in one seconds. **Sample == value of the signal at a point in time and/or space**. Obtained from *sampling* aka reducing continous-time signal to a discrete-time signal.

## Gaussian-smooth Filter

- Derivation of mean-smoothing. Weigths `k` before and after by a **Gaussian Function** (but can be extended to other functions). $$\Large y_t = \sum_{i=t-k}^{t+k} x_i g_i$$. There's no normalization factor (denominator), because the **Gaussian** should be suitably normalized so that the sum of all data points in this **Gaussian** function is one (`g`). [*aka area under the function is one or total probability density of the function is one*].

- Tends to be smoother than mean-smoothing filter for the same `k`.

- Formula to compute the Gaussian $$\Large g = e^{\frac{-4 \ln(2)t^2}{w^2}}$$. `t` is centered at 0 and the gaussian is 1 when `t=0`. `w` is **full-width at half maximum** aka the distance between two points when the gaussian is 1 forward and backwards w.r.t `t` [if you think about a gaussian, is one point on the left side of the curve and one on the right side when y-coord == 0.5, half the height of the gaussian]. Helps to think how much smoothing you want to apply (in ms usually).  

- `k` should be sufficiently long so that the gaussian goes down to 0 (asymptotic) on both sides --> **correct fwhm identification**, but not to long so that it doesn't stretch to much --> **edge effects**. Strive for as small as i can achieve the first condition.

- Always important to normalize the gaussin to unit energy $$\Large \frac{g}{sum(g)}$$ otherwise the smoothed signal is on a different scale than the original signal.

- The decision between mean-smoothing and gaussian-smoothing filters is application specific. Both useful when noise around the signal is gaussian

## Gaussian-smooth a spike time series

- This is basically just convolving a spike time series with a gaussian window, aka smoothing out the spikes.