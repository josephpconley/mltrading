import pandas as pd

def test_run():
    start_date = "2010-01-22"
    end_date = "2010-01-26"
    dates = pd.date_range(start_date, end_date)
    df = pd.DataFrame(index=dates)
    dfSpy = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"], na_values=["nan"])
    dfSpy = dfSpy.rename(columns={"Adj Close": "SPY"})

    df = df.join(dfSpy, how="inner")

    symbols = ["GOOG", "IBM", "GLD"]
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"], na_values=["nan"])
        df_temp = df_temp.rename(columns={"Adj Close": symbol})
        df = df.join(df_temp)

    print(df)

if __name__ == "__main__":
    test_run()