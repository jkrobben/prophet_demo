# encoding: utf-8
"""
@author: lee
@time: 2019/5/10 14:55
@file: main.py.py
@desc: 
"""
import pandas as pd
from fbprophet import Prophet
from pandas.plotting import register_matplotlib_converters


def main():
    df = pd.read_csv('./data/example_wp_log_peyton_manning.csv')
    print(df.head())
    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=365)
    print(future.tail())

    forecast = m.predict(future)
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    register_matplotlib_converters()
    fig1 = m.plot(forecast)
    fig1.show()
    fig2 = m.plot_components(forecast)
    fig2.show()


if __name__ == "__main__":
    main()
