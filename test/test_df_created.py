def check_df_created(df):

    assert df isinstance(df, pd.DataFrame)
    print(df.columns)