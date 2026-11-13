from src.reporter import DataFrameReporter as dfr
import pandas as pd


def main():
    data = pd.read_csv('data/payments.csv')
    reporter_1 = dfr(float_format='0.02f', percent_format='0.03%')
    reporter_2 = dfr(float_format='0.03f', percent_format='0.01%', include_all=True)
    reporter_1.show_report(data)
    print()
    reporter_2.show_report(data, 'reporter_2 отчет!')


if __name__ == '__main__':
    main()