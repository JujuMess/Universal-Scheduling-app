from app.universal_scheduling_app import 
def test_load_employee_list():

    df_team, name_map = scheduling_app.load_employee_list("test/test_file.xlsx")

    assert isinstance(df_team, pd.DataFrame)

    for name in df_team["norm_name"].values:
        assert name.islower()
        for n in name:
            assert n not in [" ", "-"]
