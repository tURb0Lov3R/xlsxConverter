# xlsxConverter

`xlsxConverter` provides a robust and flexible command-line tool for converting XLSX files to CSV and JSON formats. This tool streamlines data transformation and integration processes, making it ideal for developers and data analysts who need to efficiently work with data across various systems and applications.

## Features

* **XLSX to CSV Conversion:** Easily convert XLSX files to CSV format for compatibility with various data analysis and spreadsheet applications.
* **XLSX to JSON Conversion:** Transform XLSX data into JSON format for seamless integration with web applications and APIs.
* **Command-Line Interface:** Simple and efficient command-line usage for quick data conversions.
* **Cross-Platform Compatibility:** Works on various operating systems supporting Python 3.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/tURb0Lov3R/xlsxConverter.git](https://www.google.com/search?q=https://github.com/tURb0Lov3R/xlsxConverter.git)
    cd xlsxConverter
    ```
2.  **Install Dependencies (add depedencies):**
    ```bash
    # For example:
    # pip install openpyxl
    ```

## Usage

To use `xlsxConverter`, simply execute the Python script with the input and output file paths, along with the desired conversion option.

```bash
python3 xlsxConverter.py <INPUT_FILE.xlsx> -<option> <OUTPUT_FILE>
```
### Options

-j: Convert XLSX to JSON format.

-c: Convert XLSX to CSV format.

## Examples:

Convert data.xlsx to data.json:
```bash
python3 xlsxConverter.py data.xlsx data.json -j
```
Convert report.xlsx to report.csv:
```bash
python3 xlsxConverter.py report.xlsx report.csv -c
```

