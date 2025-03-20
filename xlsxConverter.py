import sys
import openpyxl
import json
import csv
import pandas as pd
import argparse

def xlsx_to_json_openpyxl(xlsx_file, json_file):
    try:
        df = pd.read_excel(xlsx_file)
        df.to_json(json_file, orient='records', indent=4) # Orient records creates an array of json objects
        print(f"Conversion successful: {xlsx_file} -> {json_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

def xlsx_to_csv_openpyxl(xlsx_file, csv_file):
    try:
        df = pd.read_excel(xlsx_file)
        df.to_csv(csv_file, index=False)
        print(f"Conversion successful: {xlsx_file} -> {csv_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert XLSX to JSON and CSV.")
    parser.add_argument("input_file", help="Input XLSX file.")
    parser.add_argument("-j", "--json", metavar="json_output_file", help="Output JSON file.")
    parser.add_argument("-c", "--csv", metavar="csv_output_file", help="Output CSV file.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()

    if args.verbose:
        print(f"Converting {args.input_file}...")
    
    if args.json:
        xlsx_to_json_openpyxl(args.input_file, args.json)
    if args.csv:
        xlsx_to_csv_openpyxl(args.input_file, args.csv)

    if not args.json and not args.csv:
        print("Error: You must specify at least one output format (-j for JSON, -c for CSV).")
        sys.exit(1)

    if args.verbose:
        print("Conversion complete.")
