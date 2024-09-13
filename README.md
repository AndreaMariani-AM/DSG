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
_____________________
$$\Large y_t = (2k + 1)^{-1} \sum_{i=t-k}^{t+k} x_i$$  
_____________________

- This filter is applied in the time domain (smoothed over x-coord). With convolution and spectral multiplication you can apply a smoothing filter in the frequency domain (y-coord??)

- The larger `k`, the smoother the time series.  

- Applying any temporal filters causes a **edge effect**, aka edges usually don't have any values being the last and the first `nth` points (depending on `k`). Either set them as the original values or ignore them and filter them out.  

- Sampling Rate: measured in Hz, is the avg number of samples obtained in one seconds. **Sample == value of the signal at a point in time and/or space**. Obtained from *sampling* aka reducing continous-time signal to a discrete-time signal.

## Gaussian-smooth Filter

- Derivation of mean-smoothing. Weigths `k` before and after by a **Gaussian Function** (but can be extended to other functions).  
_____________________
$$\Large y_t = \sum_{i=t-k}^{t+k} x_i g_i$$  
_____________________

There's no normalization factor (denominator), because the **Gaussian** should be suitably normalized so that the sum of all data points in this **Gaussian** function is one (`g`). [*aka area under the function is one or total probability density of the function is one*].

- Tends to be smoother than mean-smoothing filter.

- Formula to compute the Gaussian  
_____________________
$$\Large g = e^{\frac{-4 \ln(2)t^2}{w^2}}$$  
_____________________

`t` is centered at 0 and the gaussian is 1 when `t=0`. `w` is **full-width at half maximum** aka the distance between two points when the gaussian is 1 forward and backwards w.r.t `t` [if you think about a gaussian, is one point on the left side of the curve and one on the right side when y-coord == 0.5, half the height of the gaussian]. Helps to think how much smoothing you want to apply (in ms usually).  

- `k` should be sufficiently long so that the gaussian goes down to 0 (asymptotic) on both sides --> **correct fwhm identification**, but not to long so that it doesn't stretch to much --> **edge effects**. Strive for as small as i can while achieving the first condition.

- Always important to normalize the gaussian to unit energy  
_____________________
$$\Large \frac{g}{sum(g)}$$  
_____________________

otherwise the smoothed signal is on a different scale than the original signal.

- The decision between mean-smoothing and gaussian-smoothing filters is application specific. Both useful when noise around the signal is gaussian

## Gaussian-smooth a spike time series

- This is basically just convolving a spike time series with a gaussian window, aka smoothing out the spikes.

## Denoising EMG via TKEO

- **EMG** is electromyogram and measures muscle movement from electrical signals starting from the brain. Can be helpful to measures when movements are initiated (onset). It's inherently noisy and some algo might have a hard time differentiating between noise and movement start.

- **TKEO**: **Taeger-Kaiser enerthy-tracking operator** is a general denoising strategy.  
_____________________
$$\Large y_t = x_{t}^{2} - x_{t-1}x_{t+1}$$  
_____________________

Easy operator, square the signal at time point t and substract the product of the previous and subsequent signal. It suppresses then noise and augment the signal

## Median filter to remove spike noise

- Really great filter to remove spikes in time series data. Its a **Non Linear Filter**, better to apply it to only selected data points that i think are outliers or very unusual (spikes)

## Detrending (can be linear or not)

- Aka removing linear trends (or slow drifts) with a line fitting to time serie or removing non-linear trends with polynomial fitting.

- Fit a line through data and then subtract it to remove the trend. Imagine a trend going up but you are interested in local changes and fluctuations regardless of the trend.

- Most of the time you wouldn't have a linear trend to remove because trends that you want to remove, most of the time, are the results of artifacts or oscillations in the system/sensors and thefore do not a linear pattern, most of the time. Can also be called **slow drifts**

- The $$\Large \beta_0$$ as the first term of the polynomial $$\Large \beta_0 + \beta_1 x + \beta_2 x^2 + ... + \beta_n x^n$$ it a general mena offset.

- To find the order of the polynomial that best matches the TS, i can use `BIC` (Bayes information criterion). The calculate the residuals and denoise the signal from the nth order polynomial trend. `BIC` is a way to evaluate a fit of a model to a dataset, evaluate different models with different parameters and then pick the one with the lowest `BIC`.  
_____________________
$$\Large b = n \space ln(\epsilon) = k \space ln(n)$$  
_____________________
$$\Large \epsilon = n^{-1} \sum_{i=1}^{n} (\hat y_i - y_i)^2$$  
_____________________
The secondon term in the `BIC` accounts for all the free parameters tha you have in the model (in this case these are the `orders` of the polynomial). This portion offsets the `BIC` to avoid that models with a higher number of parameters fit the data better even if they are not better models.

- In case of two minimas in the `BIC`, it's usually better to go with the smaller order poly.

## Time-Synchronous Averaging

- Can increase `S/N ratio` by averaging multiple repetitions of some events in the signal. Take a continous TS and cut it into epochs. They have to be cut so that they are aligned to the onset of some event in the system. You can then average by time point across all epochs to increse `S/N ratio`. This reduces the inter-variability of the each epoch

- It's necessary to know when the events will happen, otherwise this approach won't work. In that case, use **Template Matching or Pattern Matching** to identify likely events.

## Least-Square Template Matching

- Removes an artifact from a timeseries based on some structural identification of the artifact. It requires a data channel and some form of measuring the artifact (like and artifacat channel). Then by identifying some structures or patterns in the data channel that looks like the artifact channel, i can remove it.

- In this case, i can use `Least-Square` procedure (aka regression models of GLMs) and find a statistical (linear??) mapping between the artifact channel and the data channel. Then i can remove the best "candidates artifact" by regressiing it out.  
_____________________
$$\Large \beta = (X^T X)^{-1} X^Ty$$  
_____________________
$\Large \beta$ is a parameter vector (`regression weigths`) obtained from a regression model solving through least squares. $\Large \beta$ is the best fit or closest match between the artifact channel, a column in design matrix $\Large X$ and the data channel, vector $\Large y$. You can also think about $\Large X$ as the artifact pattern or artifact signal.  
_____________________
$$\Large r = y - X \beta$$  
_____________________
Then the residuals are what's left of the vector signal $\Large y$ when subtracted with the design matrix $\Large X$ scaled by $\Large \beta$. $\Large X \beta$ is the predicted data from the regression model, aka the component in the data vector $y$ best explained by the design matrix. 

- $\Large X$ design matrix has $\Large n+1$ columns where $\Large n$ is the number of artifact channels. The first columns is always all 1s and the *nrow* is equal to the time points in the artifact channel. The nth column is timepoints in the artifact channel