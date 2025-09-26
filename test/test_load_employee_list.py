from app.universal_scheduling_app import load_employee_list
import pandas as pd

def test_load_employee_list():

    df_team = load_employee_list("test/test_file.xlsx","team")

    assert isinstance(df_team, pd.DataFrame)

    for name in df_team["agent_name"].values:
        if any(c.isalpha() for c in name):
            assert name.islower()
        assert not any(c in [" ", "-"] for c in name)


    for idx, row in df_team.iterrows():
        for col, value in row.items():
            assert not (pd.isna(value) or
                str(value).strip() == ""
            ), f"Empty value at row {idx}, column {col}"