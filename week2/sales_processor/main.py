from pathlib import Path

from analysis import (
fastest_delivery_country,
highest_sales_country,
lowest_profit_country,
most_requested_item,
item_types_sold,
)
from context_managers import sales_files
from decorators import measure_time
from readers import read_sales

CSV_PATH = Path(
"C:/Users/Okekeni Ude/OneDrive/Desktop/"
"Flexisaf/flexisaf-internship-learn-build/"
"week2/data/100 Sales Records.csv"
)

OUTPUT_PATH = Path(
"C:/Users/Okekeni Ude/OneDrive/Desktop/"
"Flexisaf/flexisaf-internship-learn-build/"
"week2/sales-processor/record.txt"
)

@measure_time
def run_analysis() -> None:
    """Read the sales CSV and generate the analysis report."""

    with sales_files(
        str(CSV_PATH),
        str(OUTPUT_PATH),
    ) as (input_file, output_file):

        records = list(read_sales(input_file))

        highest_country, highest_revenue = (
            highest_sales_country(records)
        )

        fastest_country, fastest_days = (
            fastest_delivery_country(records)
        )

        requested_item, request_count = (
            most_requested_item(records)
        )

        lowest_country, lowest_profit = (
            lowest_profit_country(records)
        )

        items = item_types_sold(records)

        report = (
            "SALES ANALYSIS REPORT\n"
            "=====================\n\n"
            f"Highest sales country: "
            f"{highest_country} "
            f"(${highest_revenue:,.2f})\n\n"
            f"Fastest delivery country: "
            f"{fastest_country} "
            f"({fastest_days:.2f} days)\n\n"
            f"Most requested item: "
            f"{requested_item} "
            f"({request_count} records)\n\n"
            f"Lowest profit country: "
            f"{lowest_country} "
            f"(${lowest_profit:,.2f})\n\n"
            f"Types of items sold: "
            f"{', '.join(sorted(items))}\n"
        )

        print(report)
        output_file.write(report)


if __name__ == "__main__":
    run_analysis()

