import numpy as np
import scipy.io as sio
import scipy.signal
from scipy import *
import matplotlib.pyplot as plt
import copy

from typing import Iterable


def mean_smoothing(k: int, time: int, signal: Iterable[float]) -> Iterable[int]:
	"""
      Applies the mean smoothing procedure

      Args:
        k: number of time points to consider before and after 
        time: time domain of the time serie
        signal: array of singal to denoise

      Returns:
        An Array 
      """
	# allocate filtSig
	filtSig = np.zeros(time)
	
	for i  in range(k, time-k):
		filtSig[i] = np.mean(signal[i-k:i+k+1])

	return filtSig


def gaussian_smoothing(fwhm: int, signal: Iterable[float], time: int, 
					   srate: int, k: int, check_kernel: bool = True
					   ) -> Iterable[int]:
	"""
      Applies gaussian smoothing 

      Args:
	  	fwhm: Full-width half-maximum value
		signal: the raw signal to be smoothed
		time: time domain of the time serie
		srate: sampling rate
	  	k: number of time points to consider before and after 
		check_kernel: Boolen, if True check the fwhm is reasonable

      Returns:
          if check_kernel == False, returns the filtered signal, otherwise plots FWHM
      """
	# prevents changing the original array
	filtSignal = np.copy(signal)
	# convert k points to milliseconds, `t` in the gaussian formula
	gtime = 1000*np.arange(-k, k+1)/srate
	# create gaussian window
	gauss_window = np.exp( -(4 * np.log(2) * gtime**2) / fwhm**2)
	
	# Check if fwhm makes sens
	if check_kernel is True:
		# Computre empirical fwhm
		postFWHM = k + np.argmin( (gauss_window[k:] - 0.5)**2 )
		preFWHM = np.argmin( (gauss_window - 0.5)**2 )
		empFWHM = gtime[postFWHM] - gtime[preFWHM]

		# Plot the FWHM
		plt.plot(gtime, gauss_window, 'ko-')
		plt.plot([gtime[preFWHM], gtime[postFWHM]], [gauss_window[preFWHM], gauss_window[postFWHM]], 'm')
		plt.ylabel('Gain')
		plt.title(f'Gaussian kernel with empirical FWHM: {empFWHM}')
		plt.show()
	else:
		# normalize gaussian to unit energy
		gauss_window = gauss_window / np.sum(gauss_window)
		for i in range(k+1, time-k):
			filtSignal[i] = np.sum(filtSignal[i-k:i+k+1] * gauss_window)

	return filtSignal

def TKEO_denoising(signal: Iterable[float]) -> Iterable[float]:
	"""
      Applies TKE operaton to a time serie

      Args:
		signal: the raw signal to be smoothed

      Returns:
          denoised signal
      """
	filtSignal = np.copy(signal)
	# TKEO operator
	filtSignal[1:-1] = filtSignal[1:-1]**2 - filtSignal[0:-2]*filtSignal[2:]
	
	return filtSignal

def median_filter(threshold: int, signal: Iterable[float],
				  k: int) -> Iterable[float]:
	"""
      Applies median filter to random spikes in the signal

      Args:
	  	threshold: An int that specify the transitioning bound from signal to random spike
		signal: the raw signal to be smoothed
	  	k: number of time points to consider before and after

      Returns:
	  	Smoothed signal with spikes removed
      """
	filtSignal = np.copy(signal)
	thresh_over = np.where(filtSignal > threshold)[0]

	for i in range(len(thresh_over)):
		# set lower and upperbound
		low_bound = np.max((0, thresh_over[i]-k))
		up_bound = np.min((thresh_over[i]+k+1, len(filtSignal)))

		# Compute median of surrounding points
		filtSignal[thresh_over[i]] = np.median(filtSignal[low_bound:up_bound])
	
	return filtSignal

def polynomial_fit(orders: Iterable[int], signal: Iterable[float],
				    n: int, check_BIC: bool = False) -> Iterable[float]:
	"""
      Applies a polynomial fit to remove non linear trends after finding the best polynomial order
	  with Bayes information criterion

      Args:
		orders: Range of Ints, corresponds to orders of polynomial to test
		signal: the raw signal to be detrend.
		n: number of data points in the signal
		check_BIC: boolean, whether to plot of not the BIC plot for visual inspection

      Returns:
	  	Smoothed signal with spikes removed
      """
	# crete MSE object
	epsilon = np.zeros(len(orders))
	
	# create time range
	time = range(n)

	# compute sum of squared errors
	for i in range(len(orders)):
		# Compute polynomial
		yHat = np.polyval(np.polyfit(time, signal, orders[i]), time)
		# Compute sum of squared errors
		epsilon[i] = np.sum( (yHat- signal)**2)/n
	
	# Compute BIC
	BIC = n*np.log(epsilon) + orders*np.log(n)

	# Find best order
	best_BIC = min(BIC)
	best_idx = np.argmin(BIC)

	# Plot for visual inspection
	if check_BIC is not False:
		plt.plot(orders, BIC, 'ks-')
		plt.plot(orders[best_idx],best_BIC, 'ro')
		plt.xlabel('Polynomial order')
		plt.ylabel('Bayes Information Criterion')
		plt.show()
	
	else:
		# repeat the polynomial fit for the best candidate
		yHat_best = np.polyval(np.polyfit(time, signal, orders[best_idx]), time)
		# compute residuals
		residuals = signal - yHat_best
		return (residuals, yHat_best)
	
def time_synch_averaging(signal: Iterable[float], n_events: int, k: int,
						 onset_time: int) -> Iterable[float]:
	"""
      Averages multiple epochs of some signal to increase S/N ratio

      Args:
		signal: The raw signal to be averaged
		n_events: Number of repetitive events in the singal to be averaged
		k: Fundamental param, duration of the event in time (in data indx, not ms)
		onset_time: Idx of singal at which the event occurs

      Returns:
	  Signal with events averaged
    """
	mat = np.zeros((n_events, k))

	for i in range(n_events):
		mat[i,:] = signal[onset_time[i]:onset_time[i]+k]

	mat = np.mean(mat, axis=0)

	return mat

def least_square_template_matching(signal: Iterable[float], artifact: Iterable[float]
								   ) -> Iterable[float]:
	"""
      Removes artifacts from a signal via least-square template matching over an artifact signal

      Args:
		signal: The raw data channel/signal of interest
		artifact: The raw artifcal channel/signal that captures the artifact leaked into the data signal

      Returns:
	  Residuals of signal channel
    """
	# Set matrix size
	DM = np.shape(signal)
	# initialize residual data
	residuals = np.zeros(DM)

	for i in range(DM[1]):
		# Create design matrix X
		X = np.column_stack((np.ones(DM[0]), artifact[:, i]))
		# Compute regression coefficients for signal channel
		# equation $\beta = (X^T X)^{-1} X^Ty$
		beta = np.linalg.solve(X.T@X, X.T@signal[:,i]) #this avoids inverting the matrix
		yHat = X@beta
		# residuals
		residuals[:,i] = signal[:,i] -yHat
	
	return residuals