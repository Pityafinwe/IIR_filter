#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:38:10 2018

@author: SalvaCarceles
"""
class IIR_filter:
    def __init__(self):
        
        self.orden = 2 # Internarl variable which defines the order of the filter
        self.control = 0 # Internal variable which allows to calculate the coefficients
                         # just once
    # This fuction takes as first argument data we want to filter, the kind of filter we
    # want (highpass, lowpass, bandpass and bandstop), and the cut frequencies.
    # The use of * allows keep empty  one of the arguments       
    def iir_filter(self,value,mode,f1,*f2):
        # Libraries we need to run the function independently 
        import numpy as np
        import scipy.signal as signal
        # If which calculates the coefficients of the filter
        if self.control == 0: 
            self.control = 1 # This line disable this calculation 
            self.b, self.a = signal.butter(self.orden, [f1,*f2], mode, output="ba")
            # Using this function we get the coeffients which are kept in arrays 
            self.buffer = np.zeros(len(self.b)) # Defining the buffer
            

        self.acc1 = value # Taking the value in 
        
        # For loops I use to take coefficients and calculate FIR/IIR data, without care 
        # how long is the array where coefficients are
        for i in range(1,len(self.buffer)):
            self.acc1 = self.acc1 - (self.a[i] * self.buffer[i])
       
        self.acc2 = self.acc1 * self.b[0]
        
        for j in range(1,len(self.buffer)):
            self.acc2 = self.acc2 + (self.b[j] * self.buffer[j])
        
        # Lines which renew data in buffer
        self.buffer[1:] = self.buffer[:-1]
        self.buffer[1] = self.acc1
  
        return self.acc2