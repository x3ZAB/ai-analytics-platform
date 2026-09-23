import pandas as pd

from backend.profiling.type_inferencer import TypeInferencer


def test_numeric_column():
    series = pd.Series([10, 20, 30])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "numeric"


def test_boolean_column():
    series = pd.Series([True, False, True])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "boolean"


def test_datetime_column():
    series = pd.Series(
        pd.to_datetime([
            "2024-01-15",
            "2024-02-15",
            "2024-03-15"
        ])
    )

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "datetime"


def test_text_column():
    series = pd.Series([
        "Ahmed",
        "Mona",
        "Ali"
    ])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "text"


def test_numeric_string_column():
    series = pd.Series([
        "100.50",
        "200.75",
        "300.25"
    ])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "numeric"


def test_datetime_string_column():
    series = pd.Series([
        "2024-01-15",
        "2024-02-15",
        "2024-03-15"
    ])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "datetime"



def test_categorical_column():
    series = pd.Series([
        "AI",
        "CS",
        "AI",
        "CS",
        "AI"
    ])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "categorical"


def test_high_cardinality_text_column():
    series = pd.Series([
        "Ahmed is studying artificial intelligence",
        "Mona completed a machine learning course",
        "Ali works on data engineering projects",
        "Sara is learning Python and SQL"
    ])

    inferencer = TypeInferencer()

    assert inferencer.infer(series) == "text"