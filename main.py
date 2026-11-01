
import pandas as pd
from src.reporter import DataFrameReporter


def main():
    # Загружаем данные
    data = pd.read_csv('data/payments.csv')

    # Создаём объект класса
    reporter = DataFrameReporter()

    # Формируем и выводим отчёт
    reporter.show_report(data)


if __name__ == '__main__':
    main()
