import pandas as pd


class DataQualityWarningEngine:

    def check(self, series: pd.Series) -> list[str]:
        warnings = []

        total_rows = len(series)

        if total_rows == 0:
            return warnings

        missing_percentage = (
            series.isna().sum() / total_rows
        ) * 100

        if missing_percentage > 20:
            warnings.append("High missing values")

        unique_count = series.nunique(dropna=True)

        if unique_count == 1:
            warnings.append("Constant column")

        return warnings