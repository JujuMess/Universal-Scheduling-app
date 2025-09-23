import openpyxl
import pandas as pd
import calendar

#normalise to be used in all functions
def normalise(text):
    print(f"initialising normalise for {text}")
    try: 
        text = str(text).strip().lower().replace(" ", "_").replace("-", "_")
        print(text)
        return text
    except AttributeError:
        print(f"Error normalising {text}, not a string!")
        text = str(text)
        return text
    
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

        return df
    except Exception as e:
        print(f"effor {e} during importing sheet.")
        return None









#create load_employee_list() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_holiday_calendar() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_shift_requirements() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_history_file() function
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create check_name_list() function
    #check all names in all dfs are mathing