from src.reporter import DataFrameReporter
import pandas as pd

def main():
    # Загружаем данные
    data = pd.read_csv('data/payments.csv')

    # Инициализируем объект
    report = DataFrameReporter(float_format='0.02f', percent_format='0.02%', include_all=True)

    # Вызываем метод
    report.show_report(data)

if __name__ == '__main__': 
    main()