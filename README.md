# IIR_filter
IIR filter 

This class filter is done as the final assignment of Digital Signal Processing. The goal of this code is to create an IIR filter of a high order by linking several filters of a lower order.

The function takes four arguments:
  Value: this is the datum/data we want to filter.
  Mode: this is the class of filter we need (lowpass, highpass, bandpass and stopband as keywords).
  f1: it is the corner frequency for low and highpass filters and the lower one for pass and stopband filter (it is always necessary).
  f2: it is the upper corner frequency in band and stopband filter (it must be omitted when low and highpass filter are used).

The order of the filter is defined by a self-value of the class filter, it is defined by default as 2.

The class works as follow:
  1) The first "if" calculates the coefficients of the filters by using scipy.signal.butter command, output = "SOS".
  2) Then these coefficients are divided between IIR and FIR coefficients.
  3) It is created a number of buffers equal to the order of the filer (one per filter).
  
  These first three steps are held in an "if", due to it just need to calculate them once.
  
  4) The "for" loop selects each link of the chain by selecting a specific buffer.
  5) For each buffer, it is iterated data through "for" loops which represent the IIR and FIR filters.
  6) The buffer is renewed at the end of both "for" loops.
  7) Data is returned.
