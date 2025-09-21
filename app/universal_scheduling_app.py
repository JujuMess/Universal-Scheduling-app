import openpyxl
import pandas as pd
import calendar


def normalise(text):
    print(f"initialising normalise for {text}")
    try: 
        isinstance(text, str)
        text = text.strip().lower().replace(" ", "_").replace("-", "_")
        print(text)
        return text
    except AttributeError:
        print()
        return text
    
# create import_sheet() function
    # should be openpyxl to load the workbook based on the sheet entered as the function argument
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