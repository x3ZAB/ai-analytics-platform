from pathlib import Path

from backend.ingestion.csv_reader import CSVReader
from backend.ingestion.excel_reader import ExcelReader
from backend.ingestion.header_normalizer import HeaderNormalizer

class IngestionService:

    def __init__(self):
        self.csv_reader = CSVReader()
        self.excel_reader = ExcelReader()
        self.normalizer = HeaderNormalizer()

    def ingest(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("File not found")

        extension = path.suffix.lower()

        if extension == ".csv":
            df, mapping = self.csv_reader.read(file_path)

        elif extension in [".xlsx", ".xls"]:
            df = self.excel_reader.read(file_path)

            mapping = self.normalizer.normalize(
                df.columns.tolist()
            )

            df = df.rename(columns=mapping)

        else:
            raise ValueError(
                f"Unsupported file format: {extension}"
            )

        # Standard ingestion result
        return {
            "file_name": path.name,
            "file_type": extension,
            "rows": len(df),
            "columns": df.columns.tolist(),
            "header_mapping": mapping,
            "data": df,
        }


service = IngestionService()

result = service.ingest("data/samples/students.csv")

print("File:", result["file_name"])
print("Type:", result["file_type"])
print("Rows:", result["rows"])
print("Columns:", result["columns"])
print("Mapping:", result["header_mapping"])
print("\nData:")
print(result["data"])


if __name__ == "__main__":
    service = IngestionService()

    result = service.ingest("data/samples/students.csv")

    print("File:", result["file_name"])
    print("Type:", result["file_type"])
    print("Rows:", result["rows"])
    print("Columns:", result["columns"])
    print("Mapping:", result["header_mapping"])
    print("\nData:")
    print(result["data"])