# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:58:22 2023

@author: Raafe
"""
import os
import pandas as pd
import numpy as np
import uuid

chunk_size = 6001
batch_no = 1

for chunk in pd.read_csv('test_2021.csv', chunksize=chunk_size):
    chunk.to_csv('validation_data' + '.csv', index=False)


