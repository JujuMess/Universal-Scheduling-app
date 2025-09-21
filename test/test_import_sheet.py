from app.universal_scheduling_app import import_sheet

def test_import_sheet():
    sheet_list = ["april_2025", "history", "team", "shifts", "week_requirements", "holidays"]
    for sheet in sheet_list
        sheet = import_sheet("test/test_file.xlsx")
        assert isinstance(sheet, pd.DataFrame)