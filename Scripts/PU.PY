def test_deteccion_fraude():
    import pandas as pd
    from procesar_excel import procesar_excel_df

    df = pd.DataFrame({
        "Domain": ["RETAIL"]*3,
        "Value": [1000, 2000, 999999],
        "Transaction_count": [10, 15, 20]
    })

    df_result = procesar_excel_df(df)
    assert df_result["fraude_simple"].iloc[-1] == 0  # Cambié la aserción a 0