import pandas as pd


class DataFrameReporter:
    """Класс для формирования отчёта по DataFrame."""

    def __init__(
        self,
        df: pd.DataFrame,
        float_format: str = '{:.2f}',
        include_all: bool = False
    ):
        """
        :param df: датафрейм с данными
        :param float_format: формат отображения долей (по умолчанию 2 знака после запятой)
        :param include_all: включать ли все столбцы в describe() (по умолчанию False — только числовые)
        """
        self.df = df
        self.float_format = float_format
        self.include_all = include_all
    def show_report(self) -> None:
        """Выводит отчёт о данных: размер, дубликаты, описательную статистику и пропуски."""
        print('=' * 50)
        print('ОТЧЁТ О ДАННЫХ')
        print('=' * 50)

        print(f'\nКоличество строк: {self.df.shape[0]}')
        print(f'Количество столбцов: {self.df.shape[1]}')

        # Дубликаты: считаем полные повторы строк
        duplicates_count = self.df.duplicated().sum()
        duplicates_share = duplicates_count / len(self.df) if len(self.df) > 0 else 0
        print(f'\nКоличество дубликатов: {duplicates_count}')
        print(f'Доля дубликатов: {self.float_format.format(duplicates_share)}')
        # Описательная статистика с учётом настройки include_all
        print('\nОписательная статистика:')
        print(self.df.describe(include='all' if self.include_all else None))

        # Информация о пропущенных значениях по всему датафрейму
        missing = self.df.isna().sum()
        print('\nПропущенные значения по столбцам:')
        print(missing[missing > 0] if missing.sum() > 0 else 'Пропусков нет')
