from backend.ingestion.excel_reader import ExcelReader


def test_read_excel():
    reader = ExcelReader()

    df = reader.read("data/samples/students.xlsx")

    assert len(df) == 3
    assert df.columns.tolist() == ["Name", "Age", "Major", "GPA"]


def test_missing_excel():
    reader = ExcelReader()

    try:
        reader.read("data/samples/not_found.xlsx")
    except FileNotFoundError:
        assert True
    else:
        assert False


def test_empty_excel(tmp_path):
    empty_file = tmp_path / "empty.xlsx"
    empty_file.touch()

    reader = ExcelReader()

    try:
        reader.read(str(empty_file))
    except ValueError as error:
        assert str(error) == "Excel file is empty"
    else:
        assert False