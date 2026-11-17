from src.reporter import DataFrameReporter
import pandas as pd

def main():
    df = pd.read_csv('data/payments.csv')

    reporter = DataFrameReporter(include_all=True)
    reporter.show_report(df, 'PAYMENTS')

if __name__ == '__main__':
    main()