# [10_feature_detection]()

## Local maxima and minima

- Global and local maxima/minima. Local can be loosely defined depending on the range that' being considered

## How to recover signal from noise amplitude

- When the feature of the system i'm interested in, isn't the overall mean but the magnitude of the fluctuations.

- Rectify means take the absolute value of a signal

- `Hilbert transform` is a way to extract a complex analytic signal from a real valued signal. It's a measure of the energy of the system and tends to be smoother than other methods, especially when you narrowband the filter 

## Wavelet convolution for feature extraction

- Use a combination of wavelet convolution and local minima to identify possible features in the signal.

## Area under the curve

- Classical calculus subject. Given a function $\large f(x)$, what is the area unde the curve between two boundaries $\large x_1, x_2$, where the minimum is $\large f(x) = 0$ and the maximum is the function itself.

- You can do it in discrete way thorugh `Riemann sum`, which is a **discrete** approximation of an **integral** by a finite sum. Or in a continous way using an `integral`.

- With `Riemann sum` you set a discretization unit called `\large \Delta x` and divide the segment from $\large x_1, x_2$ byt that and obtain some "rectangles" under the curve. Then, you calculate the value of $\large f(x_1)$ (height of the rectangle) and multiply by $\large \Delta x$ to get the area of the rectangle and sum over all areas.