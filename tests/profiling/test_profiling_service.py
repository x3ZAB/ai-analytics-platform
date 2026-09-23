import pandas as pd

from backend.profiling.profiling_service import ProfilingService


def test_profiling_service():
    df = pd.DataFrame({
        "name": ["Ahmed", "Mona", "Ahmed"],
        "age": [20, 21, 20],
        "major": ["AI", "CS", "AI"],
    })

    service = ProfilingService()

    result = service.profile(df)

    assert result["rows"] == 3
    assert result["columns_count"] == 3
    assert result["duplicate_rows"] == 1

    assert len(result["columns"]) == 3

    age_profile = next(
        column
        for column in result["columns"]
        if column["name"] == "age"
    )

    assert age_profile["type"] == "numeric"
    assert age_profile["statistics"]["mean"] == 20.333333333333332


def test_profile_students_csv():
    from backend.ingestion.ingestion_service import IngestionService

    ingestion_service = IngestionService()
    profiling_service = ProfilingService()

    ingestion_result = ingestion_service.ingest(
        "data/samples/students.csv"
    )

    result = profiling_service.profile(
        ingestion_result["data"]
    )

    assert result["rows"] == 3
    assert result["columns_count"] == 4

    columns = {
        column["name"]: column
        for column in result["columns"]
    }

    assert columns["name"]["type"] == "text"
    assert columns["age"]["type"] == "numeric"
    assert columns["major"]["type"] == "categorical"
    assert columns["gpa"]["type"] == "numeric"