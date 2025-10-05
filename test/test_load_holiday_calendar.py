from app.universal_scheduling_app import load_holiday_calendar, load_employee_list
import pandas as pd

def test_load_holiday_calendar():

    df_holiday = load_holiday_calendar("test/test_file.xlsx","team")
    df_team = load_employee_list("test/test_file.xlsx","team")
    assert isinstance(df_holiday, pd.DataFrame)

    for name in df_holiday["agent_name"].values:
        if any(c.isalpha() for c in name):
            assert name.islower()
        assert not any(c in [" ", "-"] for c in name)

    df_holiday_name_list = df_holiday["agent_name"].values.tolist()
    df_team_name_list = df_team["agent_name"].values.tolist()
    assert len(df_holiday_name_list) == len(df_team_name_list)
    assert set(df_holiday_name_list) == set(df_team_name_list)