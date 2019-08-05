
import numpy as np
import csv
import pandas as pd
LANGUAGES = "LanguageWorkedWith"
SALARY = "ConvertedSalary"
DEV_TYPES = "DevType"

print("Reading data...")
data = pd.read_csv("./SO_2018_survey/data.csv",
    dtype={LANGUAGES: str, SALARY: float, DEV_TYPES: str},
    usecols=[LANGUAGES, SALARY, DEV_TYPES]
)

data.dropna(inplace=True)
data = data[data[DEV_TYPES] != "Student"]
data = data[data[SALARY] < 200000]
data = data[data[SALARY] > 1000]

data = data.rename(columns={LANGUAGES: "languages", SALARY: "salary", DEV_TYPES: "devTypes"})

print("Saving", len(data), "rows...")
data.to_csv("SO_2018_survey/ui-data.csv", index=False)
