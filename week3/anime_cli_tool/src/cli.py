import argparse
import json
import sys
from pathlib import Path
from .pipeline import process_dataset, calculate_means

def main():
    parser = argparse.ArgumentParser(description="Generic CLI Data processing Toolkit")
    parser.add_argument("--input", required=True, help="path to input CSV file")
    parser.add_argument("--group-by", required=True, help="Column name to group data by")
    parser.add_argument("--target", required=True, help="Numeric column name to comput statistics on")
    parser.add_argument("--report", default="invalid_report.json", help="path to output invalid records JSON report")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File '{args.input}'...")
       # 1. This is your existing line that runs the pipeline
    grouped_data, invalid_records, stats = process_dataset(
        str(input_path), args.group_by, args.target)

    # 2. This handles saving your invalid report if errors are found
    if invalid_records:
        report_data = [
            {"row": inv.row_number, "reason": inv.reason, "data": inv.raw_data}
            for inv in invalid_records
        ]
        with open(args.report, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4)
        print(f"⚠️ Found {stats.invalid_rows} invalid rows. Report saved to {args.report}")
    else:
        print("✅ No invalid rows found. Dataset is clean!")

    # 3. ADD THESE LINES RIGHT HERE TO PRINT RESULTS TO YOUR TERMINAL:
    means = calculate_means(grouped_data)
    sorted_results = sorted(means.items(), key=lambda x: x[1], reverse=True)

    print(f"\n--- Processing Complete ---")
    print(f"Total Rows Processed: {stats.total_rows}")
    print(f"Valid Rows: {stats.valid_rows}")
    print(f"Invalid Rows Logged: {stats.invalid_rows}")

    print(f"\nResults (Grouped by '{args.group_by}', Mean of '{args.target}'):")
    print("-" * 40)
    for group, avg in sorted_results:
        print(f"  {group}: {avg:.2f}")
    print("-" * 40)

if __name__ == "__main__":
    main()