#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:20:55 2023

@author: adityataware
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Ken/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)