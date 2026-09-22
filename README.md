# AI Analytics Platform

An AI-powered data analytics platform that allows users to upload
structured datasets and interact with their data using natural language.

## Project Vision

The goal is to build a generic AI Data Analyst that can work with
different tabular datasets such as CSV and Excel files without relying
on a predefined business schema.

The platform should be able to:

- Upload CSV and Excel datasets
- Automatically understand dataset structure
- Profile data quality and column characteristics
- Answer questions about the uploaded data
- Generate real analytics and visualizations
- Detect anomalies
- Generate analytical reports

## Core Principle

The LLM is **not the source of truth**.

The AI layer is responsible for understanding user intent,
selecting the appropriate analytical tools, and explaining results.

All numerical and factual results about the dataset must come from
actual execution against the user's data.

## Current Status

### Phase 01 — Generic Data Ingestion

Completed:

- CSV ingestion
- Excel ingestion
- Delimiter detection
- Encoding fallback
- Header normalization
- Original-to-normalized header mapping
- Basic malformed-file handling
- IngestionService
- Automated ingestion tests

Current test status:

```text
11 passed
Project Structure
ai-analytics-platform/
├── backend/
│   └── ingestion/
│       ├── csv_reader.py
│       ├── excel_reader.py
│       ├── header_normalizer.py
│       └── ingestion_service.py
│
├── data/
│   └── samples/
│
├── docs/
│
├── frontend/
│
├── tests/
│   └── ingestion/
│       ├── test_csv_reader.py
│       ├── test_excel_reader.py
│       └── test_ingestion_service.py
│
├── pyproject.toml
├── .gitignore
└── AGENTS.md
Roadmap
Phase 00 — Project Foundation
Phase 01 — Generic Data Ingestion
Phase 02 — Data Profiling & Understanding
Phase 03 — Dataset Storage & Data Model
Phase 04 — Analytics Engine
Phase 05 — Visualization Engine
Phase 06 — Backend API
Phase 07 — Chat Interface
Phase 08 — LLM Fundamentals & Integration
Phase 09 — AI Data Analyst & Tool Calling
Phase 10 — Safe Natural-Language Data Querying
Phase 11 — Automatic Insights
Phase 12 — Anomaly Detection
Phase 13 — Reports
Phase 14 — Testing, Security & Reliability
Phase 15 — Deployment
Phase 16 — Future Production Improvements
Tech Stack
Current
Python
Pandas
OpenPyXL
Pytest
Planned
PostgreSQL
FastAPI
Frontend application
LLM integration
Data visualization
Development

Create and activate the project virtual environment:

python -m venv .venv
source .venv/bin/activate

Install dependencies:

python -m pip install pandas openpyxl pytest

Run tests:

pytest
Project Philosophy

This project is both a learning project and a real software project.

Each feature should be small enough to:

Understand
Implement
Test
Document
Explain in a technical interview