'''
Created on Oct 26, 2018

@author: mzaman
'''
import numpy as np
import matplotlib.pyplot as plt
import csv
import pywt
def readCSV(file,skip,x_col,y_col):   
    file=open(file,'r')
    reader=csv.reader(file)
    v=[]
    t=[]
    i=0;
    for row in reader:
        if i>=(skip+1):
            t.append(float(row[x_col]))
            v.append(float(row[y_col]))
        else:
            i+=1
            continue               
    file.close()
    return np.array(t),np.array(v)
def writeCSV(file,data):
    file=open(file,'a',newline='')
    writer=csv.writer(file)
    writer.writerow(data)
    file.close()
    return

def addGWN(signal,SNR):
    signal_energy=np.linalg.norm(signal)**2
    noise_energy=signal_energy/(10**(SNR/10))
    noise_variance=noise_energy/(len(signal)-1)
    noise_standardDev=np.sqrt(noise_variance)
    noise=noise_standardDev*np.random.randn(len(signal))
    noisy_signal=noise+signal
    return noise,noisy_signal

def doWaveletDenoising(data,wavelet='db4',levelValue=1):
    coefficients= pywt.wavedec(data,wavelet,level=levelValue,mode='per') #step 1: Find the coefficients
    from statsmodels.robust import mad
    sigma=mad(coefficients[-levelValue])#Step 2.1: Set the threshold 
    uthresh=sigma*np.sqrt(2*np.log(len(data)))#Step 2.2: Set the threshold
    print('Threshold Value=',uthresh)
    coefficients[1:]=( pywt.threshold( i, value=uthresh, mode="soft" ) for i in coefficients[1:] )#Step 2.3: Set the threshold 
    y=pywt.waverec(coefficients,wavelet,mode='per') #Step 3: Reconstruct the wave
    return y
def findRMS(data):
    rms=np.sqrt(np.mean(np.square(data)))
    return rms
def addPowerlineNoise(signal,time,SNR):
    signal_rms_amplitude=findRMS(signal)
    noise_rms_amplitude=signal_rms_amplitude/(10**(SNR/20))
    number_of_points=len(signal)
    #time=np.linspace()
    noise=noise_rms_amplitude*np.sqrt(2)*np.sin(2*np.pi*60*time)
    noisy_signal=noise+signal
    return noise,noisy_signal
def getEngropy(w):
    from scipy.stats import entropy
    e=entropy(np.square(w),np.square(w))
    return e
def getPerfusion(w):
    pi=(np.amax(w)-np.amin(w))/np.mean(w)
    return np.abs(pi)*100
def getWaveletCoefficients(data,wavelet):
    coefficients= pywt.wavedec(data,wavelet) 
    return coefficients
def getCAAverage(w):
    coefficients=getWaveletCoefficients(w,'coif1')
    cA=sum(coefficients[0])/len(coefficients[0])
    #print('cA= ',cA)
    return cA
def getWaveWindowByTime(signal,time,start,stop):
    import numpy as np
    startIndex=np.where(time>=start)[0][0]
    stopIndex=np.where(time>=stop)[0][0]
    windowWave=signal[startIndex:(stopIndex+1)]
    t=time[startIndex:(stopIndex+1)]
    return windowWave,t
def getWaveWindowBySample(signal,time,startIndex,stopIndex):
    import numpy as np
    windowWave=signal[startIndex:(stopIndex+1)]
    t=time[startIndex:(stopIndex+1)]
    return windowWave,t
