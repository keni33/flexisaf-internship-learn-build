# 🛠️ Generic CLI Data Processing Toolkit

A lightweight, robust, and standard-library-only command-line toolkit built in Python for streaming, validating, transforming, and aggregating moderately sized CSV and JSON datasets. 

Designed without heavy third-party data frameworks (like Pandas), this project showcases clean Python architecture utilizing **generators, dataclasses, typing, and custom exception handling**.

---

## 🚀 Features

* **Lazy Streaming Pipeline:** Uses Python generators (`yield`) to process files row-by-row, ensuring an **$O(1)$ memory footprint** regardless of file size.
* **Schema Validation & Error Reporting:** Automatically detects missing columns, invalid numeric values, and malformed rows, logging them into a structured JSON audit report without crashing the pipeline.
* **Dynamic & Reusable:** Not hardcoded to any specific dataset structure; allows users to define target columns and grouping keys dynamically via CLI flags.
* **Standard Library Only:** Built purely on core Python modules (`csv`, `json`, `argparse`, `dataclasses`, `collections`).

---

## 📁 Project Structure

```text
anime_cli_tool/
├── data/                  # Input datasets and output audit reports
│   ├── your_dataset.csv
│   └── invalid_report.json
├── src/                   # Source code
│   ├── __init__.py
│   ├── models.py          # Dataclasses and type definitions
│   ├── pipeline.py        # Core streaming, validation, and aggregation logic
│   └── cli.py             # Command-line interface entry point
├── tests/                 # Unit test suite
│   ├── __init__.py
│   └── test_pipeline.py
├── requirements.txt       # Development dependencies (e.g., pytest)
└── README.md              # Project documentation

Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
cd anime_cli_tool
Activate your Virtual Environment:

Bash
source venv/Scripts/activate  # On Windows Git Bash
# or venv\Scripts\activate     # On Windows Command Prompt
💻 Usage & CLI Commands
Run the CLI tool from your terminal by specifying the input file, the column to group by, and the target numeric column to measure.

Example Command:
Bash
python -m src.cli --input data/your_dataset.csv