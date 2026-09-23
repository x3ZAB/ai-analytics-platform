import pandas as pd

from backend.profiling.type_inferencer import TypeInferencer


class ColumnProfiler:

    def __init__(self):
        self.type_inferencer = TypeInferencer()

    def profile(self, series: pd.Series) -> dict:
        total_rows = len(series)
        null_count = series.isna().sum()
        unique_count = series.nunique(dropna=True)

        return {
            "name": series.name,
            "type": self.type_inferencer.infer(series),
            "null_count": int(null_count),
            "missing_percentage": (
                round((null_count / total_rows) * 100, 2)
                if total_rows > 0
                else 0
            ),
            "unique_count": int(unique_count),
            "sample_values": series.dropna().head(5).tolist(),
        }