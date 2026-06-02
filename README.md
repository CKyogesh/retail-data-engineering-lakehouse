# Retail Acquisition Data Engineering Pipeline

## Overview

This project demonstrates an end-to-end Data Engineering solution built using Databricks, Apache Spark, Python, SQL, and AWS S3.

The business scenario simulates a large retail company acquiring a smaller retail organization and consolidating data from both companies into a unified Lakehouse platform.

The solution implements the Medallion Architecture (Bronze, Silver, Gold) to support scalable analytics and reporting.

---

## Architecture

Source Systems
       │
       ▼
 AWS S3 Landing Zone
       │
       ▼
 Bronze Layer
 (Raw Data)
       │
       ▼
 Silver Layer
 (Cleansed Data)
       │
       ▼
 Gold Layer
 (Business Metrics)
       │
       ▼
 Dashboards & Analytics

---

## Technology Stack

- Databricks
- Apache Spark
- Python
- SQL
- AWS S3
- Delta Lake
- Lakehouse Architecture
- Medallion Architecture
- Power BI

---

## Key Features

### Data Ingestion

- Load raw CSV files from AWS S3
- Schema validation
- Data quality checks

### Bronze Layer

- Store raw datasets
- Preserve source system structure
- Enable auditability

### Silver Layer

- Cleanse and standardize data
- Handle null values
- Remove duplicates
- Standardize formats

### Gold Layer

- Build business-ready datasets
- Customer metrics
- Product metrics
- Sales KPIs
- Executive reporting datasets

---

## Business Objectives

- Consolidate data from acquired companies
- Create a single source of truth
- Improve reporting accuracy
- Enable scalable analytics

---

## Sample Metrics

- Total Revenue
- Revenue by Region
- Top Selling Products
- Customer Retention
- Monthly Sales Growth

---

## Skills Demonstrated

- Data Engineering
- ETL Development
- Data Modeling
- Data Warehousing
- Lakehouse Architecture
- Apache Spark
- Databricks
- AWS Cloud
- SQL Development
- Data Quality Management

---

## Future Enhancements

- CI/CD Pipeline using GitHub Actions
- Automated Data Quality Framework
- Streaming Data Pipeline
- Data Governance Integration
- Orchestration using Apache Airflow

---

## Author

Yogesh Khairnar
Data Engineer | AWS Certified Cloud Practitioner