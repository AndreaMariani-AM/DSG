# [07_wavelet_analysis]()

## Wavelets

- `Wavelets` should have the following properties:
1) Taper down to zero at the beginning and the end
2) They have to integrate to zero from $\large \pm \infty$, or very close to 0
The major difference between wavelets is the central component, which is created in different ways and serves different purposes.

- `Morlet wavelet` is a `sine wave` multiplied by a `gaussian` and is really useful for time frequency analysis because the cental component nicely localize in the frequency domain

- It's useful to think about in terms of `wavelet families` from which you can derive all the others. Some important families are:
1) `Morlet wavelet`
2) `Daubechies wavelet`
3) `Ricker wavelet`, aka mexican hat wavelet
4) `Meyer wavelet`, sometimes called coilet

The derivation usually is done by streatching and squeezing the "original" wavelet and therefore changing the frequency.

- Wavelets have two main applications:
1) Filtering in time-frequency analysis --> spectrogram
2) Feature detection (pattern matching)

## Time-frequency analysis with complex wavelets

- `Complex wavelet`means using a complex sine wave instead of a real valued sine wave
_____________________
$$\Large e^{ik} = \cos(k) + i\sin(k)$$
_____________________

$\large e^{ik}$ is Euler notation for some angle $\large k$ where:
_____________________
$$\Large k = 2\pi ft + \theta $$
_____________________

When multiplied by a gaussian that gives you a complex `morlet wavelet`. You use it to do "normal" convolution but now you have a kernel with a real and and imaginary part. Not that the kernel is a complex vector, the dot product between the signal and the kernel yields a complex number (`complex dot product`). 

- For each `complex dot product` you want to extract: 
1) the `magnitude` of the complex dot product, that value is plotted as `time-frequency power`, freq (Hz) on y-coord and time on x-coord.
2) The `angle` of the complex vector w.r.t the positive real axis --> can be plotted as `time-frequency phase`
3) The `projection` down to the real axis which represents the band-pass filtered signal, which is what you get when you do convolution with a real valued kernel.