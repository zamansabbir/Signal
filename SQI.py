'''
Created on May 1, 2019

@author: mzaman
'''
import SignalDetection as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import SignalDetection
#fileDir='E:/UofM/ESARP/Projects/DataCheckingProject/Database/PPG_data/'
fileDir='E:/UofM/ESARP/Projects/DataCheckingProject/Database/ECG_data/'
#file=fileDir+'bidmc/Signals/'+'bidmc_01_Signals.csv'
file=fileDir+'set-a/'
filewrite=fileDir+'SQI/SQI.csv'
skip=0;
x_col,y_col=0,2


fig1=plt.figure(1)
acceptable=[1002867,
1005639,
1007823,
1009404,
1009856,
1013179,
1015620,
1021036,
1027085,
1027294,
1028505,
1029390,
1029776,
1031414,
1035858,
1041530,
1045434,
1049030,
1053871,
1058551,
1062220,
1066522,
1066648,
1066767,
1067343,
1068169,
1071514,
1073952,
1073996,
1074828,
1075113,
1084750,
1085234,
1085468,
1095208,
1097104,
1098180,
1098605,
1098634,
1101252,
1102129,
1102445,
1105148,
1108131,
1108642,
1109779,
1112518,
1115111,
1116393,
1122248,
1124627,
1129323,
1129523,
1133939,
1134074,
1137606,
1138505,
1139243,
1144476,
1146503,
1157735,
1165660,
1166425,
1168042,
1168914,
1173628,
1176338,
1178618,
1179983,
1185077,
1186453,
1192519,
1194123,
1197142,
1201815,
1202023,
1203950,
1206548,
1208494,
1223204,
1224250,
1225426,
1227497,
1228058,
1232746,
1234270,
1234318,
1238368,
1240272,
1247012,
1256457,
1260448,
1268034,
1273536,
1274881,
1281719,
1282270,
1284537,
1286932,
1289729]
i=0;

###
step=500
for i in acceptable:
    fileName=file+str(i)+'.txt'  
    data=[]
    data.append(i)
    t,v=sd.readCSV(fileName, skip,x_col,y_col)
    for j in range(0,len(v),step):
        start=j
        stop=start+step-1
        if(stop<=len(v)):
            w,t_w=sd.getWaveWindowBySample(v,t,start,stop)
            k=sd.getEngropy(w)
            print('start=',start,'stop=',stop,' ',k)
            data.append(k)  
    SignalDetection.writeCSV(filewrite, data)
 
###
print(data)
plt.plot(t,v)
plt.show()