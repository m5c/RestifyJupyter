#!/usr/bin/env python3

import pandas as pd
statscsv=pd.read_csv("stats.csv")
taskcsv=pd.read_csv("tasks.csv")
skillcsv=pd.read_csv("partitionskills.csv")
intermediate1=statscsv.merge(taskcsv,on="codename")
result=intermediate1.merge(skillcsv,on="codename")
result.to_csv("restify.csv", index=None)
