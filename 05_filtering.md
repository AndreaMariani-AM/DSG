# [05_filtering_notebook]()

## Intuition, Goals and Types

- Why filtering? Generally you have multiple signals mixed together and different source of noise at the sensors (**singal mixing**). The idea is to try and isolate all of these distinc sources (**signal separation**).

- `Spectral mixing`: If the assumption that Signals and noise are mixed with **different** frequency, aka they have different spectral properties, you can achieve `spectral separation` by applying filtering. This is a critical assumption, otherwise temporal filtering won't helo you separate various sources of signals and noise. 

- Even if two signals are mostly different, the portion where the frequencies overlap are going to be hard to discriminate, but you can achieve a high efficiency everywhere else.

- `Filtering in the frequency domain`: Apply FFT to bring the signal to frequency domain. Then applying filtering to zero out frequencies you are not interested in. For example, high-pass filtering preverves with some attenuation closer to the cutoff the frequency and zeros out the ones lower than the cutoff. Then apply IFFT to go back to time domain.

- `Filtering in the time domain`: Applies to the original signal a `kernel filter`. For example, you want to apply a low-pass filter (so keeping signal below a thresold), with the kernel filer, each data point in the filtered signal is the weighted linear combination of the previous values form the original signal. The weights of the data points are given by the `filter kernel function` that multiplies each data point in the original signal with the corresponding element in the kernel and then sums them up. --> `FIR filters`. Another category is `IIR filters`, with shorter kernels and you take liner weighted combinations of both original signals and also previous points in the filtered signal. 

- Filtering in the time and frequency domains seems different but in reality are pretty much the same, even identicall if time domain is set in a particular way --> thanks to the `convolution theorem`.

- Procedure:
    1) Define `frequency-domain shape` (ideal filter response) and spectral cut-offs.
    2) Generate the filter kernel (various methods)
    3) Evaluate kernel in the time domain but mainly in its power spectrum.
    4) Apply filter kernel to data

- The `filter kernel` is what it's applied to the data. Takes in as input the ideal filter response, and one algorithm to create the filter. To evaluate the filter kernel, take the FFT and evaluate the power spectrum againts the idel filter --> `frequency of responde of the filter`.


|       | FIR   | IIR
|-------|-------|-------|
| name  | Finite Impulse response | Infinite impulse response |
|-------|-------|-------|
| Kernel length | Long | Short |
|-------|-------|-------|
| Speed | Slower | Fast |
|-------|-------|-------|
| Stability | High | Data-dependent |
|-------|-------|-------|
| Mechanism | Multiply data with kernel | Multiply data with data|
|-------|-------|-------|
