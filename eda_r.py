import pandas as pd
import numpy as np
from dataprep.eda import create_report
import sweetviz as sv

# read csv file
df = pd.read_csv('D:/MS Files/DA/Data Analysis Term Project/training_data.csv')

# Auto EDA report
report = create_report(df)
report.show_browser()
report.save('dataPrep_report')

# sweet_report = sv.analyze(df)
# sweet_report.show_html('eda_report.html')
