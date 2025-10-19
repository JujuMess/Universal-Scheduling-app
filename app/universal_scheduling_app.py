import openpyxl
import pandas as pd
import calendar
import re
                                            #### daram import functions ####

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

    elif isinstance(text, pd.Index):
        return pd.Index([normalise(c) for c in text], name=text.name)
    
    else:
        return normalise(str(text))
    
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


#create load_holiday_calendar() function TEST CREATED
def load_holiday_calendar(file_path):
    pass
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_shift_requirements() function TEST CREATED
def load_shift_requirements(file_path):
    pass
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create load_history_file() function TEST CREATED
def load_history_file(file_path):
    pass
    # create a pandas dataframe from the sheet with a column for each one in the sheet, all names normalised
#create check_mismatch() function CURRENTLY CREATING TEST
def check_mismatch(df_team, df_history, df_holiday, df_schedule):
    pass
#check all names in all dfs are matching return two string, one saying the missing names in df_team and where to find it, and other saying the missing dta compared to df_team and where it's missing
# takes all dfs as arguments


# create a function that turns the holiday df to long format

#create the schedule structure

#merge team df and schedule structure

#TEST TO SEE IF ALL NAMES MATCH


                                            #### utilities functions ####
# extract teams off dfs into a list
#create masks for dfs for each skill

#pick random staff function

#select fairest function
#assign_one_agent function

#update history function

                                            #### LOGIC ASSIGNMENT ####
#assign days of annual leave
#assign default shift function

#assign shift function : should work for all shifts, build a team that natches all requirements

#checker fuctions checking all shift requirements are met (number and skills met)
#checker function checking the agents don't get the same shift all the time
#assign days off

#wrapper function applying the logic weekly

                                            #### OUTPUT SCHEDULE ####
#building empty schedule function
#building the empty history tab function if needed
#filling the schedule function
#updating history tab function (must have an "updated on" box)

#function to check if missing names between previous month and new schedule
#function to check if missing names between history tab and new schedule

#function to update yram in history tab 

