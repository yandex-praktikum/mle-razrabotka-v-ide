from src.reporter import DataFrameReporter
import pandas as pd


def main():
    """Загружает данные и выводит отчёт о них."""
    df = pd.read_csv('data/payments.csv')
    reporter = DataFrameReporter(df)
    reporter.show_report()


if __name__ == '__main__':
    main()
