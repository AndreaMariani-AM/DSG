# [05_filtering_notebook](https://github.com/AndreaMariani-AM/DSG/blob/main/notebooks/05_filtering.ipynb)

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
| name  | Finite Impulse response | Infinite Impulse response |
| Kernel length (Order) | Long (100s-1000s) | Short (as low as 2 points) |
| Speed | Slower (offline filtering) | Fast (online filtering) |
| Stability | High | Data-dependent  |
| Mechanism | Multiply data with kernel | Multiply data with data|

## FIR filters with firls

 - How to create FIR kernels with firls algorithm (finite impulse response least square). To create it, we need some fraction of the nyquist frequency and the `gain` at those frequencies. For example, a `bandpass filter`, you would most likely need 6 points to create a parallelogram to keep frequencies inside of it. With filtering, its best to keep the shape as simple as possible. The first and last point are always the DC and Nyquist. The other four create the shape of the bandpass filter. Generally is best to avoid sharp edges as those edges require many frequencies to be represented as part of the FT --> `ripple effects` in the time domain. Moreover, sharp edges are difficult to represent with sine wave basis fucntions, and its easier to design poor filters. 

 - Between different gains (0 -->1 or 1 -->0), you have transition zones, defined as the area between the change of gain. usually transition zones are specified as `percentage of frequency`

 - With particularly wide filter like firls with `bandpass` you always have some ripple effects in the upper part of the signal. usually it's recommended to apply to different filters, one `high pass` for the lower end and then one `low pass` for the higher end. usually better than wide filer kernels.

 - When deciding an order (length of the Kernel) isn't not always straightforward to figure which orders are better. Some of them are clearly wrong but once you reach a good range it becomes tricky to choose one. It all boils down to the particular data you are working with and what parts of the signal you think it's better to filter or to retain.

 ## FIR filters with fir1

 - It's basically firls without a transition zone. For a `bandpass filter` you only specify the gain at 1 and for `high or low pass filter` only one point at gain 1. Given there's no transition zone, i'll drops right from gain 1 to 0 with the same frequency. We said before that sharp edges introduce ripple effects in the time domain. Therefore, `fir1` applies a window to the time domain filter kernel to smooth out the edges and that ends up creating a transition zone. 
 
 - You would apply `fir1` instead of `firls` when you really want maximal attenuation, even with the risk of attenuating some signal at the edges of the kernel.

 ## IIR filters with Butterworth filters

 - `IIR` filters are set up similarly to `fir1 filters` where you don't need to specify transition zones. They are never going to be better than FIR filters, at best very similar, but are faster

 - `IIR` filter are evaluated differently compared to `FIR`. Basically you use them and see how they look in pratice with `impulse response`. You look at the response of an impulse to the filter. 

 - An `impulse` is a time series of all zeros with one one right in the middle of the series

 - `IIR` when designed, give back two sets of coefficients. This is because the filtered signal is the weigthed sum of previous points in the original signal and the weigthed sum of the previous points in the filtered signal. `Coeffs B` are the weights of the previous values in the original signal and the `coeffs A` are thw weigths of the previous values of the alredy filtered signal. They are not even in the same scale.

 ## Causal and Zero-phase-shift filter

 - `Causal filters` are sometimes called `forward filters`. 

 - With filters you have `phase shift` bacause past events are taken into account when computing the filtered signal. This is the example of `FIR and IIR` filters. For online filtering this has to happen, as there's no info on future data (with some tricks it can be predicted). For offline analysis the signal has already be recorded and you can create a `zero-phase-shift filter`.

 - `Zero phase shift filter`: first filters the signal forwards in time, so the current time point in the **filtered** signal is a function of previous values of the **original** signal. Then you flip time around backwards and filter again this time going backwards in time. So now the current **filter point** is a function of weighted values of the previous **filtered** signal. Then you flip the signal again.

 ## Edge effects with reflections

 - Pretty much unavoidable when working with time series and applying filters! Although, they shouldn't contaminate the entire signal and there are ways to attenuating it.

 - `Reflection`: a prodcedure to attenuate them. Basically adds at the beginning and end a version of the signal, let edge effects to happen and then cut them off. The reason `FIR and IIR` have edge effects is because the filtered signal is a function of the original signal (and filtered for IIR) and so can only starts at a `kernel lenght` inside the original signal (before it's impossible).

 - `Reflection Procedure`: 
    1) You take your signal and reflect it. 
    2) The reflected signal is added as the beginning and at the end. 
    3) Apply the filter
    4) Edge effect will happen at the ends of the mirrored signals
    5) Cut the reflected signal at both ends

- For very long TS it's impractical to reflect the whole signal, it's enough to reflect the order or the kernel.

- When **not** to reflect? There's extra time series that you don't care about and therefore it's not necessary

## Low Pass Filter

- Usually changing the transition width means making the drop/attenuation steeper, and changing the order makes is "faster" for higher orders. Although it's clear by now that rarely exist a set of "right" parameters to specify to filters. **NEVER BLINDLY TRUST A SET OF PARAMETERS**

## Windowed-sinc Filter (FIR)

- It's a type of `low pass filter` generated by a `sinc function` of the form 
_____________________
$$\Large y = \frac{\sin(2\pi ft)}{t}$$
_____________________

where $\large t$ is any kind of factor, usually time. $\large f$ is the frequency and allows you to specify the frequency in for the sine wave (`in Hz if t in in seconds`). In practice, one time point is trick and it's when $\large t = 0$, se we need to `interpolate` it. 

- A `windowed-sinc filter` is used because there'll be edge effects at the begging and end of the kernel, and some tapering/windowing can be applied. Different forms of windowin: `gaussian`, `hann`, `blackman`, `kaiser`

## Narrow-band filter

- Use simmetric transition zones as much as possible as they can create awful kernels otherrwise.

## Two stage wide-band filter

- Sometimes when creating bandpass filters, its hard to come up with a really good kernel for a given set of frequencies to keep. You can try and change parameters but sometimes this won't go far. A better approac would be to filter `twice` -->` two stage filter`. For example, if you want a band of 10-60 Hz, you can apply a high pass fiter at 10Hz and a low pass filter at 60Hz.

- Dosen't really matter if the filter are applied separately in a two stage filter, they result will be the same as if i had a great bandpass.

# Roll-off characteristics

- One of the ways to describe the characteristics of a temporal filter is to quantify the `roll-off` of the filter, aka the decrease in amplitude with the increasing frequency. Basically quantify the decay in amplitude of filtered signal. E.g. when aplying a low pass filter, the roll-off in the decays in the amplitude after the cutoff at high frequency (in the power spectrum). higher roll off =  higher attenuation of the signal.

- The roll-off is quantified as the slope of the decay signal in the power spectrum and it's given by
_____________________
$$\large RL = \frac{g_{2f} \space - g_{-3}}{Hz_{sf} \space - Hz_f}$$
_____________________

1) You start with a prespecified cutoff frequency (which is the frequency chosen for the filter).
2) Convert the power spectrum to decibel (gain in decibel).
3) Find the frequency that has $\large -3$ decibels attenuation ($\large f_{-3}$). Based on the order of the filter it could be either before or after the cutoff.
4) Double that quantity to get the change in frequency and these two last points go to the denominator.
5) in the denominator, the last term will always be the Gain -3 (or as close as possible), and the first term is the gain in decibels (also negative) at double the frequency of the frequency at -3.

- The `roll-off` of a filter isn't the only important characteristic of a filter
