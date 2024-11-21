# [11_variability_notebook]()

## Total and windowed variance and RMS

- Two ways to measure variability (or amoutn of energy) in a time domain signal

- `Variance` 
_____________________
$$\Large var = \frac{1}{n} \sum^{n}_{i=1} (y_i - \hat y)^2$$
_____________________

- `RMS` (root mean square)
_____________________
$$\Large RMS = \sqrt{\fra{1}{n} \sum^{n}_{i=1} y_{i}^2}$$
_____________________

The most important difference is the mean subtraction in the **variance**. You can think about RMS and the `total energy` of the system and the `variance` as the dispersion of energy around the mean.

- You can compute them over the entire TS or over small windows. IF computed over small windows you get a TS of variance/RMS.

# Signal to Noise ratio

- Some conceptual difficulties in computing S/N. There are various ways that you can use to compute S/N.

- `Mean/std` can be an appropriate procedure for certain datasets
- Another way could be to pick a point (maximum of the signal) as the numerator for `signal` and then the variance over a window fort the `noise`. This window can over flat activities in the signal, e.g. before time point 0

## (Shannon) Entropy

- Used in many fields:
_____________________
$$\Large H = - \sum^{n}_{i=1} p_i \log2(p_i)$$
___________________

Where $\large n$ is a bin,, $\large p_i$ is the probability of a data point to be in bin $\large i$. `Bin` can be interpreted as different states of the system.