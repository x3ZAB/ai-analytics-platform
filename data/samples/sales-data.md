# Sample Sales Data Specification

## Purpose

This document defines the expected structure of the sales dataset used by the MVP.

## Required Columns

| Column | Type | Description |
|---|---|---|
| order_id | string | Unique order identifier |
| date | date | Order date |
| customer | string | Customer identifier/name |
| product | string | Product name |
| category | string | Product category |
| region | string | Sales region |
| quantity | integer | Number of units sold |
| revenue | decimal | Sales revenue |
| cost | decimal | Cost associated with the sale |
| profit | decimal | Profit from the sale |

## Required Fields

The dataset must contain all required columns:

- order_id
- date
- customer
- product
- category
- region
- quantity
- revenue
- cost
- profit

## Basic Validity Rules

- `order_id` must be present.
- `date` must be a valid date.
- `quantity` must be numeric.
- `revenue` must be numeric.
- `cost` must be numeric.
- `profit` must be numeric.
- Required columns must not be missing.
- Column names should be normalized before further processing.

## Data Quality

The ingestion and profiling phases must detect:

- Missing values
- Duplicate records
- Invalid data types
- Invalid values
- Basic outliers

## Source

The MVP is focused on Sales Analytics.