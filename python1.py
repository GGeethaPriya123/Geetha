import pandas
import numpy as np
from pandas import json_normalize
inputdata =[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
df = json_normalize(inputdata)

df["BMI"]=(df["WeightKg"]*10000)/(df["HeightCm"]**2)
def categorise(row):  
    if row["BMI"]  <= 18.4:
        return "under weight"
    elif row["BMI"] > 18.4 and row["BMI"] <= 24.9:
        return "Normal weight"
    elif row["BMI"] > 24.9  and row["BMI"] <= 29.9:
        return "over Weight"
    elif row["BMI"] > 29.9 and row["BMI"] <= 34.9:
        return "Moderately Obese"
    elif row["BMI"] > 34.9  and row["BMI"] <= 39.9:
        
         return "severely obese"
    return "very severely obese"
df["BMICATEGORY"] = df.apply(lambda row: categorise(row), axis=1)
def categorise_risk(row):  
    if row["BMI"]  <= 18.4:
        return "Mal Nutrition"
    elif row["BMI"] > 18.4 and row["BMI"] <= 24.9:
        return "Low Risk"
    elif row["BMI"] > 24.9  and row["BMI"] <= 29.9:
        return "Enhanced Risk"
    elif row["BMI"] > 29.9 and row["BMI"] <= 34.9:
        return "Medium Risk"
    elif row["BMI"] > 34.9  and row["BMI"] <= 39.9:
        
         return "High Risk"
    return "very High Risk"
df["HEALTH RISK"] = df.apply(lambda row: categorise_risk(row), axis=1)
print('Table with BMI , BMI CATEGORY , HEALTH RISK')
print(df)
num_rows=df[df["BMICATEGORY"] == "over Weight"]
print('NO OF OVER WEIGHT PEOPLE: ',end='')
print (len(num_rows))


