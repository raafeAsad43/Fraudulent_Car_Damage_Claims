import pandas as pd
import numpy as np
from dataprep.eda import create_report

df = pd.read_csv('D:/MS Files/DA/Data Analysis Term Project/training_data.csv')

report = create_report(df)
report.show_browser()