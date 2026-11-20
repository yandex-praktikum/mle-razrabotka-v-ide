from src.reporter import DataFrameReporter
import pandas as pd

def main():
    payments_df = pd.read_csv("data/payments.csv")

    dataFrameReporter = DataFrameReporter()
    dataFrameReporter.show_report(payments_df)


if __name__ == '__main__': 
    main() 