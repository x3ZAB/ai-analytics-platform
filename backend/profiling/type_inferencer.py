import pandas as pd


class TypeInferencer:

    def infer(self, series: pd.Series) -> str:

        if pd.api.types.is_bool_dtype(series):
            return "boolean"

        if pd.api.types.is_numeric_dtype(series):
            return "numeric"

        if pd.api.types.is_datetime64_any_dtype(series):
            return "datetime"

        if pd.api.types.is_string_dtype(series):

            numeric_values = pd.to_numeric(
                series,
                errors="coerce"
            )

            if numeric_values.notna().all():
                return "numeric"

            non_null = series.dropna()

            if not non_null.empty:
                datetime_values = pd.to_datetime(
                    non_null,
                    errors="coerce",
                    format="mixed"
                )

                if datetime_values.notna().all():
                    return "datetime"

            value_counts = series.value_counts(dropna=True)

            if len(value_counts) < len(series):
                return "categorical"

            return "text"

        return "text"