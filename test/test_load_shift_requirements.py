#test for load shit requirements

from app.universal_scheduling_app import load_shift_requirements
import pandas as pd

def test_load_employee_list():

    df_shift_requirements = load_shift_requirements("test/test_file.xlsx","team")

    assert isinstance(df_shift_requirements, pd.DataFrame)

    for shift in df_shift_requirements["shift_name"].values:
        if any(c.isalpha() for c in shift):
            assert shift.islower()
        assert not any(c in [" ", "-"] for c in shift)


    for idx, row in df_shift_requirements.iterrows():
        for col, value in row.items():
            assert not (pd.isna(value) or
                str(value).strip() == ""
            ), f"Empty value at row {idx}, column {col}"
    for col in df_shift_requirements.columns:
        assert col == col.strip().lower().replace(" ", "_").replace("-", "_"), (
            f"Column '{col}' is not in snake_case"
        )