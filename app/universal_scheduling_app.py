import openpyxl
import pandas as pd
import calendar
import re

#normalise to be used in all functions
def normalise(text):

    if isinstance(text, str):
        text = str(text).strip().lower().replace(" ", "_").replace("-", "_")
        text = re.sub(r"\s+", "_", text) 
        print(text)
        return text
    elif isinstance(text, list):
        return [normalise(t) for t in text]

    elif isinstance(text, pd.Series):
        return text.apply(normalise)

    elif isinstance(obj, pd.Index):
        return pd.Index([normalise(c) for c in obj], name=obj.name)
    
    else:
        return normalise(str(obj))
    
# create import_sheet() function
    # should be pandas to load the workbook based on the sheet entered as the function argument
def import_sheet(file_path, sheet_name):
    print(f"launching import sheet function for {sheet_name}")
    try: 
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = [normalise(col) for col in df.columns]
        if "agent_name" in df.columns:
            df = df.dropna(subset=["agent_name"])
            df["agent_name"] = df["agent_name"].astype(str).apply(normalise)
        print("sheet import over")
        return df
    except Exception as e:
        raise RuntimeError(f"error {e} during importing sheet.")

#create load_employee_list() function

def load_employee_list(file_path, team_tab):
    try:
        print("loading employee list initialised")
        df_team = import_sheet(file_path, team_tab)
        df_team = df_team.fillna("empty")

        print("df_team loaded")
        return df_team
    except Exception as e:
        raise RuntimeError(f"error {e} loading employee list.")



    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_holiday_calendar() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_shift_requirements() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_history_file() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create check_name_list() function
    #check all names in all dfs are mathing