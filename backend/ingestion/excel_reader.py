import pandas as pd
from pathlib import Path


class ExcelReader:
    def read(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("Excel file not found")

        if path.stat().st_size == 0:
            raise ValueError("Excel file is empty")

        return pd.read_excel(path)


reader = ExcelReader()

df = reader.read("data/samples/students.xlsx")

print(df)
print("\nColumns:")
print(df.columns.tolist())


if __name__ == "__main__":
    reader = ExcelReader()

    df = reader.read("data/samples/students.xlsx")

    print(df)
    print("\nColumns:")
    print(df.columns.tolist())