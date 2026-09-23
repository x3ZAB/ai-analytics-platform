import pandas as pd

from backend.profiling.column_profiler import ColumnProfiler
from backend.profiling.statistics_summary import StatisticsSummaryEngine
from backend.profiling.data_quality_warning import DataQualityWarningEngine


class ProfilingService:

    def __init__(self):
        self.column_profiler = ColumnProfiler()
        self.statistics_engine = StatisticsSummaryEngine()
        self.warning_engine = DataQualityWarningEngine()

    def profile(self, df: pd.DataFrame) -> dict:

        columns = []

        for column in df.columns:
            series = df[column]

            column_profile = self.column_profiler.profile(series)

            column_profile["statistics"] = (
                self.statistics_engine.summarize(series)
            )

            column_profile["warnings"] = (
                self.warning_engine.check(series)
            )

            columns.append(column_profile)

        return {
            "rows": len(df),
            "columns_count": len(df.columns),
            "columns": columns,
            "duplicate_rows": int(df.duplicated().sum()),
        }