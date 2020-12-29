# -*- coding: utf-8 -*-
"""Write Data to Google sheets using Colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1chfKI64jxsTw-lNJsffB-540A8ykY4H8
"""

from google.colab import auth,drive
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
from gspread_dataframe import set_with_dataframe, get_as_dataframe


gc = gspread.authorize(GoogleCredentials.get_application_default())

drive.mount('/content/gdrive/')

df = pd.read_csv(path+file)

sh = gc.open_by_url('https://docs.google.com/spreadsheets/')  # add url of sheet here
sh.values_clear("sheet1!A:H")

worksheet = sh.worksheet("sheet_name") # sheetname where you want to write the data
set_with_dataframe(worksheet, df) # df is the dataframe