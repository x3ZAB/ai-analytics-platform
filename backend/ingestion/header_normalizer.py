import re


class HeaderNormalizer:
    def normalize(self, headers: list[str]) -> dict[str, str]:
        mapping = {}

        for header in headers:
            normalized = header.strip().lower()
            normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
            normalized = normalized.strip("_")

            mapping[header] = normalized

        return mapping