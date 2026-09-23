import pandas as pd

from backend.profiling.column_profiler import ColumnProfiler


def test_column_profiler():
    series = pd.Series(
        ["AI", "CS", "AI", None, "AI"],
        name="major"
    )

    profiler = ColumnProfiler()

    result = profiler.profile(series)

    assert result["name"] == "major"
    assert result["type"] == "categorical"
    assert result["null_count"] == 1
    assert result["missing_percentage"] == 20.0
    assert result["unique_count"] == 2
    assert result["sample_values"] == ["AI", "CS", "AI", "AI"]