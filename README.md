# multi-KPI-health-check-automation
Python automation for multi-KPI health checks (Traffic, Throughput, Latency)


# Multi-KPI Health Check Automation

## Overview
This project automates health checks for multiple telecom KPIs using Python.
It processes multiple Excel files and evaluates key performance indicators such as:

- Traffic
- Downlink Throughput
- Latency

The script generates a consolidated summary report and logs execution details.

---

## Problem Statement
Manual KPI health checks across multiple sites/files are time-consuming and error-prone.
Engineers typically spend hours validating traffic, throughput, and latency KPIs.

---

## Solution
A Python-based automation that:
- Reads multiple Excel files from a folder
- Dynamically evaluates KPIs using config-driven logic
- Handles missing or invalid data gracefully
- Generates a single summary report
- Logs execution for audit and debugging

---

## KPIs Evaluated
| KPI | Logic |
|----|------|
| Traffic | Zero / Non-zero / Missing |
| DL Throughput | LOW (<5 Mbps) / OK |
| Latency | HIGH (>100 ms) / OK |

---

## Project Structure
multi-kpi-health-check-automation/
├── analyze_multi_kpi.py
├── config.json
├── input_files/
│ ├── sample_site_1.xlsx
│ └── sample_site_2.xlsx
├── output/
│ └── kpi_summary.xlsx
├── kpi_health.log
└── README.md




---

## How to Run
1. Place Excel files inside `input_files/`
2. Update KPI column names in `config.json`
3. Run: python analyze_multi_kpi.py


Output

Consolidated KPI summary Excel file
KPI status flags for each file
Execution logs for traceability


Technologies Used

Python
Pandas
Excel Automation
Logging
JSON Configuration


Impact

Reduced manual KPI validation from hours to minutes
Improved accuracy and consistency
Reusable across different KPI datasets




