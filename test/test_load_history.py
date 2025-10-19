from app.universal_scheduling_app import load_history_file
import pandas as pd
import datetime


def test_load_employee_list():

    df_history = load_history("test/test_file.xlsx","team")

    assert isinstance(df_history, pd.DataFrame)

    for name in df_history["agent_name"].values:
        if any(c.isalpha() for c in name):
            assert name.islower()
        assert not any(c in [" ", "-"] for c in name)


    for idx, row in df_history.iterrows():
        for col, value in row.items():
            assert isinstance(value, datetime.date) or str(value).strip() == "", f"UNexpected value type at row {idx}, column {col}"