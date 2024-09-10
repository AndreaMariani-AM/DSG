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

- Running-mean or mean-smoothing filter. Sets each data point in the smoothed version as the mean of `n` points in the surroundings. How much you go before and after (forward and backwards in time) is called **order** of the filter (`k`), crucial param. Works best when noise is *gaussian*, not applicable everywhere.  

- This filter is applied in the time domain (smoothed over x-coord). With convolution and spectral multiplication you can apply a smoothing filter in the frequency domain (y-coord??)

- The larger `k`, the smoother the time series.  

- Applying any temporal filters causes a **edge effect**, aka edges usually don't have any values being the last and the first `nth` points (depending on `k`). Either set them as the original values or ignore them and filter them out.  

- Sampling Rate: measured in Hz, is the avg number of samples obtained in one seconds. **Sample** == value of the signal at a point in time and/or space. Obtained from *sampling* aka reducing continous-time signal to a discrete-time signal.