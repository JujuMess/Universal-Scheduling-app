from app.universal_scheduling_app import load_employee_list
import pandas as pd
import pytest

def test_load_employee_list():
    df_team = load_employee_list("test/test_file.xlsx","team")
    assert isinstance(df_team, pd.DataFrame)

def test_normalised():
    agent_list = df["agent_name"].tolist()
    for name in agent_list:
        for n in name:
            assert n not in [" ", "-"]
            if n.isalpha():
                assert name.islower(), f"{name} not normalised"

def test_no_empty_names():
    df_team = load_employee_list("test/test_file.xlsx","team")

    for idx, row in df_team.iterrows():
        for col, value in row.items():
            assert not (pd.isna(value) or
                str(value).strip() == ""
            ), f"Empty value at row {idx}, column {col}"


def test_file_cant_be_imported():
    with pytest.raises(RuntimeError) as exc_info:
        load_employee_list("test/blabla_file.xlsx", "team")

    # Check that the message contains the expected substring
    assert "error" in str(exc_info.value)
    assert "during importing sheet" in str(exc_info.value) 


