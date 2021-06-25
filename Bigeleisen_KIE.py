#Importation : 
import pandas as pd
import numpy as np
################################################
#Parameters : 
#Planck constant (J/Hz)
h=6.62*10**-34
#Boltzmann constant (J/K)
kB=1.38*10**-23
#Light velocity in vaccum (m/s)
c=299792458.0

####################################################################################
#Functions:
######################################################################################
#We check for errors : 
    
#We check if all values are positiv for initial states
def CheckPositiv(Data):
    if len(Data)!=len([i for i in Data if (i>0)]):
        print("At least one initial state hasn't every frequency that are positiv")
   
def error(isH,isD,tsH,tsD):
    CheckPositiv(isH)
    CheckPositiv(isD)  
 
#####################################################################################


#Function which takes the lists of vibration frequencies of 2 states to give the product of the ratio of frequencies
def Operation(Data1,Data2):
    if len(Data1)!=len(Data2):
        print("The number of frequencies isn't the same for two same states")
        return 
    x=1
    for i in range(len(Data1)):
        x=x*Data1[i]/Data2[i]
    return x

#Function which takes one list of vibration frequencies to give the sinh of Ui = h*x/(kB*T) according to the Biegelheisen equation
def Ui(Data,T):
    return pd.Series(Data).apply(lambda x : np.sinh(float(x)*((h*100*c)/(2.0*kB*T))))

#Function which takes in entry the lists of frequencies(cm-1) and the temperature(K) and gives the KIE
def KIE(isH,isD,tsH,tsD,T):
    error(isH,isD,tsH,tsD)
    #We calculate the sinh of  h*x/(kB*T)
    UisH=Ui(isH,T).tolist()
    UtsH=Ui(tsH,T).tolist()
    UisD=Ui(isD,T).tolist()
    UtsD=Ui(tsD,T).tolist()
    #######################
    #We begin to calculate the ratio of the two imaginary frequencies
    op1=tsH[0]/tsD[0]
    Result=op1
    #We calculate the second factor
    Result=Result*Operation(tsH[1:],tsD[1:])
    #We calculate the third factor
    Result=Result*Operation(isD,isH)
    #We calculate the fourth factor
    Result=Result*Operation(UtsD[1:],UtsH[1:])
    #We calculate the fifth factor
    Result=Result*Operation(UisH,UisD)    
    return Result


####################################################################################


