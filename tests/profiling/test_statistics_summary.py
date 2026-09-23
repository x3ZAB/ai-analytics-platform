import pandas as pd

from backend.profiling.statistics_summary import StatisticsSummaryEngine


def test_numeric_statistics():
    series = pd.Series([10, 20, 30, 40, 50])

    engine = StatisticsSummaryEngine()

    result = engine.summarize(series)

    assert result["mean"] == 30
    assert result["min"] == 10
    assert result["50%"] == 30
    assert result["max"] == 50


def test_categorical_statistics():
    series = pd.Series([
        "AI",
        "CS",
        "AI",
        "AI",
        "CS",
        "Data"
    ])

    engine = StatisticsSummaryEngine()

    result = engine.summarize(series)

    assert result["top_values"]["AI"] == 3
    assert result["top_values"]["CS"] == 2
    assert result["top_values"]["Data"] == 1