#importation
import Bigeleisen_KIE as kie
import pandas as pd

#path of Excel you have fill with your data
df = pd.read_excel('../OneDrive/Bureau/KIE_Vibration.xlsx')

#Data
lini=df['frequencies of the molecule containing the light isotope at the initial state'].to_list()
hini=df['frequencies of the molecule containing the heavy isotope at the initial state'].to_list()
lTrans=df['frequencies of the molecule containing the light isotope at the transition state'].to_list()
htrans=df['frequencies of the molecule containing the heavy isotope at the transition state'].to_list()

#we ask the temperature
T=float(input("Temperature in Kelvin : "))


#we calculate Kie with bigeleisen equation
kie.KIE(lini,hini,lTrans,htrans,T)
