# [03_Spectral_rhythmicity_analysis]()

## Fourier transform

- The general idea is that you can use the `forward fourier transform` to go from a singal in the `time` domain to the `frequency` domain. You can also do the inverse `frequency` --> `time` domain using the `inverse fourier transform`. For both domains, `Amplitude` is on the y-coord and `time` or `frequency (Hz)` is on the x-coord.

- `Hz` can be thought as **cycles per second**. So 3 Hz corresponds to **three cycles per second**

- When going from `time` to `frequency` domain, i'll plot on the x-coord the frequency, aka how many complete cycles are done in a period (seconds usually), and the amplitudine is the amount of energy in the signal at that frequency. Imagine a sine wave going between 0 and 1 in amplitude and doing 3 full cycles each second. When mapped to a `frequency` domain, i'll have a signal at 3Hz and the height of the signal will ben 1.  

- Each sine wave in the signal (number of components in the frequency domains, aka how many bars) is called a `spectral component`.

- Especially when the signal becomes commplex or has noise, visualizing the signal in the `frequency` domain **might** give you and easier and better overview of what's going on. In the end, it depends on the nature of the signal, works best when there is some `rhythmicity` or `repetition` to the signal. Too much noise can lead you to overestimate the number of `spectral components`

- For the math have a look at the other [course](https://www.udemy.com/course/fourier-transform-mxc/?couponCode=ST11MT91624B)

- Steps for one sine wave frequency:
    1) Take a signal in the time domain
    2) Take a sine wave, use is like a template, a waveform to match againt your signal
    3) Compute a `similarity` score between the sine wave and the signal using the `dot product` 
    4) This gives you basically how much of your signal is similar to a sine wave.
    5) Create a `spectral plot`. a plot that has `similarity` (or the characteristic obtain from the dot product, there's probably much more on this on the full course) on the y-coord and `frequency` on the x-coord. The position on the `frequency` axis correspond to the frequency of the sine wave.

- This same process is repeated with other sine waves of a different frequency (faster). Each combination of `similarity` and `frequency` is called `fourier coefficient`. From these you can extract `amplitude` and square it to get `power`. This whole graph is called `amplitude/power spectrum`.

- This is a very simplistic overview of the Fourier transform!!

- The inverse works backwards by mapping `Fourier coeffs` back onto pure sine waves and then sum all together.

- Major User of `Fourier Transform`:
    1) Spectral analysis where signals are better understood on the frequency domain or where the time domain cannot reveal the same insights
    2) As a tool to perfom some operations in the frequency domain, like `temporal filtering`, `autocorrelation` and so on. It exploits the `convolution theorem` to compare two signals to obtain a third one. Also, most computations are easier and faster in the frequency domain.

- `Frequency resolution in the FT` = number of time points in signal (between 0 and Nyquist), or the distance between any two successive frequency bins. It's a product of the `sampling rate` and the `number of time points` in the signal.

- `Nyquist frequency` is an important number spectral analysis and is just $$\Large Nyquist Freq = \frac{sampling rate}{2}$$. So if `srate` == 1024 Hz, then the Nyquist frequency == 512Hz.
When you do the FT, the frequencies that you get back from the signal, are between the 0 (called **DC**) and the Nyquist (srate/2). To increase the frequency resolution you have to have a longer signal, because the number of data points in the signal is directly related with the frequency resolution

- `DC` or `zero frequency component` captures the average of the signal over the whole duration of the signal

## Welch's method and windowing

- Slight variations to fast fourier transform. Goal is to do spectral analysis with FFT + increase S/N particularly if there are non stationarities in the signal (aka characteristics of the signal change over time).

- You can apply one FT over the whole signal giving you a amplitude/power spectrum over frequency domain ("static FT") OR with the `welch method` you can: 
    1) divide the signal into epochs with non overlapping or partially overlapping (more common) windows. 
    2) apply a FT to each epoch seprately --> this gives you X amplitude/power spectra. 
    3) average the power spectra together over all epochs.

- If features of the signal do not change over time both methods give you similar results. If the features change or the noise change, then the welch method should give you a better S/N. 

- One important thing to consider when applying the `Welch's method` is that the frequency resolution of each power spectrum is given by the number of data points, and with each windowd it's drastically reduced. Moreover, each time i'm cutting up the signal, the `FT` will introduce some edge effects because it captures the shard decrease from the value of the signal to 0. For this reason, we can apply and "smoothing" procedure (`Hann window`) to taper off gently the edges and avoid a point the in the power spectrum with very small frequency (left most side of the plot usually). Now, this means pratically throwing away some data at the edges and therefore having **ovelapping** windows helps recover this signal in the next/previous window.

## Time Frequency Analysis

- It's an alternative to the `Welch's method` when there are changes in the spectral properties  over time that you are interested in. Welch's average those together and therefore it's not suitable.

- More info on the Wavelets section
