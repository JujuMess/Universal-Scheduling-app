from app.universal_scheduling_app import import_sheet
import pandas as pd

def test_import_sheet():
    sheet_list = ["april_2025", "history", "team", "shifts", "week_requirements", "holidays"]
    for sheet in sheet_list:
        df = import_sheet("test/test_file.xlsx", sheet)
        assert isinstance(df, pd.DataFrame)
        if "agent_name" in df.columns:
            agent_list = df["agent_name"].tolist()
            for name in agent_list:
                for n in name:
                    assert n not in [" ", "-"]
                    if n.isalpha():
                        assert name.islower()

    