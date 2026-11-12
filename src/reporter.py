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