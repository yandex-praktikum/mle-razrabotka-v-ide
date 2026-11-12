class DataFrameReporter:
    def __init__(
        self,
        float_format: str = '0.05f',
        percent_format: str = '0.02%',
        include_all: bool = False,
    ) -> None:
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, 
    df: pd.DataFrame, 
    title: str | None = None):
    if title is not None:
        print (title)
    print(f'Количество столбцов: {df.shape[1]}')
    print(f'Количество строк: {df.shape[0]}')
    print(f'Количество дубликатов: {df.duplicated().sum()}')
    print(f'Доля дубликатов: {format(df.duplicated().mean(), self.percent_format)}')