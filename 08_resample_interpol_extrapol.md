# [08_resampling](https://github.com/AndreaMariani-AM/DSG/blob/main/notebooks/08_resampling.ipynb)

## Upsampling

- Given a "low" sampling rate, upsampling is a set of ways to increate the sampling rate. Upsampled signal should overlap with the original signal and have additional data points. Usually a `smooth interpolation function` like a `spline function` is used to estimate the data points. 

- Using a smooth interpolation functions allows the spectra to be very similar and not changing that much between the original and the upsampled one.

## Downsampling

- The core concept is the opposite of upsampling, where you reduce the amount of data tha you have. It's slightly more articulated

- Steps:
1) Pick a new sampling rate
2) Low-pass filter at **new** Nyquist
3) Downsample 

- Step 2 is necessary because with the new (lower) sampling frequency the Nyquist will be lower. Any frequency above this new Nyquist, but below the original Nyquist, needs to be removed as it'll appear as an artifact in the new downsampled data. `Anti aliasing filter` is also called.

## Multirare signals

- Simultaneous measures of the same system (in different ways) done by different sensors. They have different sampling rates because of different tech. You can upsample to match the highest sampling rate or downsample to the lowest sampling rate. No universal better answer, as a rule of thumb, downsampling to match the lowest means losing real information, therefore might be more sensible to upsample everything.

## Interpolation

- It's basically a guessing game, you need to estimate unknown points based on observed random variables. If you estimate points between first and last data point that you have is called `interpolation`. If you estimate outside these bounds, then it's called `extrapolation`, as you have non before and after reference point to interpolate your estimation.

- Assuptions about transitions between points are crucial and shape the time series.

## Extrapolation

- It's guessing what happens outside the boundaries of your measured signal, given your measured signal. Usually it's more reliable when extrapolating closer to the boundaries.

- `Linear` and `Spline` interpolation

## Spectral interpolation

- What we have seen so far for interpolation works if some datapoints here and there are missing or for upsampling. If I miss a big continous chunck, then these methods aren't great, as i don't have in between data points to interpolate correctly.

- With `Spectral interpolation`, the assumption is that the spectrum of the signal before the missing part and the spectrum of the signal after the missing part, should be relative similar. The assumption we make is that in the missing part, the spectrum smoothly transition from before to after, and we should reflect tha when interpolating.

- Take two FT before and after the boundaries of the missing part. For convenience, the windom length for taking the FT should match the length of the missing signal. Average the two fourier spectra to interpolate the missing part, then take the IFT. Most likely, the transition won't be smooth, so you can add a linear trend to facilitate that.

## Dynamic Time Warping

- When comparing two time series, if you want to know whether the two TS are similar, you might think about using a `correlation coeffs` to do that. Another way is `Euclidean Matching` where you compare the **distance** of pairs of time point from the two TS. For TS it might make more sense to `warp` them, where you shift/compress/elongate certain parts of the signal to make it match between TS, both forward and backwards in time.

- `Dynamic time warping` is a non linear method to match two TS as much as possible. Create a `distance matrix`, where you compute the distance between **EVERY** possible pairs between signals and then you find a path/trajectory through this distanc matrix that minimize the distances. 

- [Here for a visual understanding of the above concept](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2016.00046/full)

- Standard `DTW` is pretty slow for many time points. Some alternatives:
1) `Constrained DTW`: assumption is that signals will be similar across the diagonal of the distance matrix, you can skip computing distances for many points at the edges of the matrix.
2) `Multiresolution/Multiscale DTW`: reduce the total number of blocks that need to be searched to reduce the temporal resolution. Test if it's a minimum only for regions around the diagonal and reduce the search space. Downsample the signal to have a smaller distance matrix, search for the minimum and convert it back to the original time series. Now you have a smaller area in which you look for the "true" minimum.
