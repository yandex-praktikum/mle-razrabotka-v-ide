import pandas as pd
from src.reporter import DataFrameReporter


def main():
    # Загружаем датасет из папки data/
    data = pd.read_csv('data/payments.csv')

    # Инициализируем объект класса с параметрами по умолчанию
    reporter = DataFrameReporter()

    # Вызываем создание отчета
    reporter.show_report(data)


if __name__ == '__main__':
    main()