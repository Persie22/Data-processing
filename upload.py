# -*- coding: utf-8 -*-
""" Upload excel files from drive to Big query tables """

from google.colab import auth,drive
auth.authenticate_user()
from google.cloud import bigquery

drive.mount('/content/gdrive/')

dataset_name = "project_main"
project_id = "test-project"
client = bigquery.Client(project=project_id)

df = pd.read_csv(fpath) # to upload csv files
df = pd.read_excel(fpath)  #to upload excel files
tbl_name = dataset_name+"."+"table_name"
 
pandas_gbq.to_gbq(df, tbl_name, project_id=project_id, if_exists="replace")
print("Following Table  : "+tbl_name+" uploaded to Bigquery")
