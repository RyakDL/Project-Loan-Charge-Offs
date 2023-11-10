import pandas as pd
import datetime
import regex as re
from datetime import date
from pathlib import Path

## Date list function
def get_month_start(value):
    next_months_date = value + datetime.timedelta(days=32)
    new_dt = datetime.date(value.year, next_months_date.month, 1)
    return new_dt

def create_extra_dates(date_list):
    new_dates = []
    for i, value in enumerate(date_list):
        new_dates.append(value)
        next_month = get_month_start(value)
        nnext_month = get_month_start(next_month)
        new_dates.append(next_month)
        new_dates.append(nnext_month)
    return (new_dates)

## Data list function
def create_extra_data(data_list):
    new_data = []
    for i in data_list:
        value = i
        new_data.append(value)
        new_data.append(value)
        new_data.append(value)
    return (new_data)

# def data_preprocessing(files):
#     df_list = []
#     for file_name in files:
#         ## import data and initialize the dataframes
#         data = Path(f'..\Project-Loan-Charge-Offs\Resources\{file_name}')
#         df = pd.read_excel(data, header=10)
        
#         ## extract substring from file name
#         value_label = re.findall(r"(.*?)_QTR\.xlsx", file_name)
        
#         ## Prepare the date data
#         df["observation_date"] = df["observation_date"].astype("datetime64[M]")
#         val_col = df.columns[1]
#         df = df.rename(columns={val_col: value_label})

#         ## initialize and create new_df columns
#         date_list = df["observation_date"]
#         value_list = df[value_label]

#         new_datelist = create_extra_dates(date_list)
#         new_valuelist = create_extra_data(value_list)

#         ## Create new Dataframes
#         new_df = pd.DataFrame({
#             "observation_date": new_datelist, 
#             value_label: new_valuelist})
        
#         df_list.append(new_df)
        
#         # Export DF
#         new_df.to_csv(
#             f"..\Project-Loan-Charge-Offs\Resources\{value_label}_MO.csv", 
#                 sep=',', encoding='UTF-8')

#     return df_list

