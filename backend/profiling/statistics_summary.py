import pandas as pd


class StatisticsSummaryEngine:

    def summarize(self, series: pd.Series) -> dict:

        if pd.api.types.is_numeric_dtype(series):
            return {
                "mean": series.mean(),
                "std": series.std(),
                "min": series.min(),
                "25%": series.quantile(0.25),
                "50%": series.quantile(0.50),
                "75%": series.quantile(0.75),
                "max": series.max(),
            }

        if pd.api.types.is_string_dtype(series):
            return {
                "top_values": series.value_counts(
                    dropna=True
                ).head(5).to_dict()
            }

        return {}