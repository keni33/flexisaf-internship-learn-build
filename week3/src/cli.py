import argparse
import json
import sys
from pathlib import Path
from pipeline import process_dataset, calculate_means

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
        grouped_data, invalid_records, stats = process_dataset(str(input_path), args.group_by, args.target)
        #Save invalid report if any errors occured
        if invalid_records:
            report_data = [{"row": inv.row_number, "reason": inv.reason, "data": inv.raw_data} 
                 for inv in invalid_records
        ]
        with open(args.report, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=4)
            print(f"Found {stats.invalid_rows} invalid rows. Report saved to{args.report}")
            #Compute and display results
            means = calculate_means(grouped_data)
            sorted_results = sorted(means.items(), key=lambda x: x[1], reverse=True)
            print(f"\nResults (Grouped by '{args.group_by}' , Mean of '{args.target}'):")
            print("-" * 40) 
            print(f"Total processed: {stats.total_rows} | Valid: {stats.valid_rows} | {stats.invalid_rows}") 


if __name__ == "__main__":
    main()