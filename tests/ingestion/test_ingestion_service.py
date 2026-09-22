from backend.ingestion.ingestion_service import IngestionService


def test_ingest_csv():
    service = IngestionService()

    result = service.ingest("data/samples/students.csv")

    assert result["file_name"] == "students.csv"
    assert result["file_type"] == ".csv"
    assert result["rows"] == 3
    assert result["columns"] == ["name", "age", "major", "gpa"]


def test_ingest_excel():
    service = IngestionService()

    result = service.ingest("data/samples/students.xlsx")

    assert result["file_name"] == "students.xlsx"
    assert result["file_type"] == ".xlsx"
    assert result["rows"] == 3
    assert result["columns"] == ["name", "age", "major", "gpa"]

def test_unsupported_file(tmp_path):
    unsupported_file = tmp_path / "students.txt"
    unsupported_file.write_text("some text")

    service = IngestionService()

    try:
        service.ingest(str(unsupported_file))
    except ValueError as error:
        assert "Unsupported file format" in str(error)
    else:
        assert False