#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:32:16 2018

@author: SalvaCarceles
"""

class IIR_filter:

    def __init__(self):
        
        self.orden = 2 # Order of the filter by default
        self.control = 0 # Variable used to calculate just once the coeff
        self.buffer = list() # List where buffers are held
     
    def iir_filter(self,value,mode,f1,*f2):
        # Libraries it will be used to run, imdependently, the fuction
        import numpy as np
        import scipy.signal as signal
        # If which calculates the coeff
        if self.control == 0: 
            self.control = 1 # Control to avoid next calculations
            self.sos = signal.butter(1,[f1,*f2],mode,output="SOS") # Calculating coeff
            self.b = self.sos[0][:3] # Selecting FIR coeffs
            self.a = self.sos[0][3:] # Selecting IIR coeffs
            for i in range(self.orden): # Creating a number of buffer we need
                self.buffer.append(np.zeros(len(self.b)))

        self.acc1 = value # Renaming datum in
        
        for k in range(self.orden): # It takes the proper link of the chain
            for i in range(1,len(self.buffer[k])): # Running through IIR coeffs
                self.acc1 = self.acc1 - (self.a[i] * self.buffer[k][i])
       
            self.acc2 = self.acc1 * self.b[0]
        
            for j in range(1,len(self.buffer[k])): # Running through FIR coeffs
                self.acc2 = self.acc2 + (self.b[j] * self.buffer[k][j])
           
            self.buffer[k][1:] = self.buffer[k][:-1] # They renews the values of the buffer
            self.buffer[k][1] = self.acc1
        
            self.acc1 = self.acc2 # This line renames acc2 to use it again at the start of the "k for" loop
       
        return self.acc2