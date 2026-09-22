import csv
from pathlib import Path

import pandas as pd

from backend.ingestion.header_normalizer import HeaderNormalizer

class CSVReader:
    def read(self, file_path: str) -> tuple[pd.DataFrame, dict[str, str]]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("CSV file not found")

        if path.stat().st_size == 0:
            raise ValueError("CSV file is empty")

        encodings = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]

        for encoding in encodings:
            try:
                with open(path, "r", encoding=encoding) as file:
                    sample = file.read(4096)

                dialect = csv.Sniffer().sniff(sample)

                df = pd.read_csv(
                    path,
                    sep=dialect.delimiter,
                    encoding=encoding
                )

                normalizer = HeaderNormalizer()
                mapping = normalizer.normalize(df.columns.tolist())

                df = df.rename(columns=mapping)

                return df, mapping

            except UnicodeDecodeError:
                continue

        raise ValueError("Could not decode the CSV file")


reader = CSVReader()

df, mapping = reader.read("data/samples/students.csv")

print(df)
print("\nColumns:")
print(df.columns.tolist())

print("\nHeader mapping:")
print(mapping)

if __name__ == "__main__":
    reader = CSVReader()

    df, mapping = reader.read("data/samples/students.csv")

    print(df)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nHeader mapping:")
    print(mapping)