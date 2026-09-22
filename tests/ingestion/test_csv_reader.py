from backend.ingestion.csv_reader import CSVReader


def test_read_csv():
    reader = CSVReader()

    df, mapping = reader.read("data/samples/students.csv")

    assert len(df) == 3
    assert df.columns.tolist() == ["name", "age", "major", "gpa"]
    assert mapping["Name"] == "name"



def test_missing_csv():
    reader = CSVReader()

    try:
        reader.read("data/samples/not_found.csv")
    except FileNotFoundError:
        assert True
    else:
        assert False






def test_empty_csv(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.touch()

    reader = CSVReader()

    try:
        reader.read(str(empty_file))
    except ValueError as error:
        assert str(error) == "CSV file is empty"
    else:
        assert False




def test_semicolon_delimiter(tmp_path):
    csv_file = tmp_path / "semicolon.csv"

    csv_file.write_text(
        "Name;Age;Major;GPA\n"
        "Ahmed;20;AI;3.2\n"
        "Mona;21;CS;3.7\n"
    )

    reader = CSVReader()
    df, mapping = reader.read(str(csv_file))

    assert len(df) == 2
    assert df.columns.tolist() == ["name", "age", "major", "gpa"]


def test_utf8_bom(tmp_path):
    csv_file = tmp_path / "utf8_bom.csv"

    csv_file.write_text(
        "Name,Age,Major,GPA\n"
        "أحمد,20,AI,3.2\n",
        encoding="utf-8-sig"
    )

    reader = CSVReader()
    df, mapping = reader.read(str(csv_file))

    assert len(df) == 1
    assert df.iloc[0]["name"] == "أحمد"