import pandas as pd
from app import universal_scheduling_app
def test_load_employee_list(excel):

    df_team, name_map = scheduling_app.load_employee_list(excel)
    assert isinstance(df_team, pd.DataFrame)

    for name in df_team["norm_name"].values:
        assert name.islower()