import pandas as pd

from backend.profiling.data_quality_warning import (
    DataQualityWarningEngine,
)


def test_high_missing_values():
    series = pd.Series([
        "AI",
        None,
        None,
        None,
        "CS"
    ])

    engine = DataQualityWarningEngine()

    warnings = engine.check(series)

    assert "High missing values" in warnings


def test_constant_column():
    series = pd.Series([
        "AI",
        "AI",
        "AI",
        "AI"
    ])

    engine = DataQualityWarningEngine()

    warnings = engine.check(series)

    assert "Constant column" in warnings


def test_no_warning():
    series = pd.Series([
        "AI",
        "CS",
        "Data",
        "AI"
    ])

    engine = DataQualityWarningEngine()

    warnings = engine.check(series)

    assert warnings == []