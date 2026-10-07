import csv
from collections.abc import Iterator
from typing import TextIO

from sales_processor.models import SaleRecord

def read_sales(file: TextIO) -> Iterator[SaleRecord]:
    """Read sales records one at a time from a CSV file."""
    reader = csv.DictReader(file)

    for row in reader:
        yield SaleRecord(
            region=row["Region"],
            country=row["Country"],
            item_type=row["Item Type"],
            sales_channel=row["Sales Channel"],
            order_priority=row["Order Priority"],
            order_date=row["Order Date"],
            order_id=row["Order ID"],
            ship_date=row["Ship Date"],
            units_sold=int(row["Units Sold"]),
            unit_price=float(row["Unit Price"]),
            unit_cost=float(row["Unit Cost"]),
            total_revenue=float(row["Total Revenue"]),
            total_cost=float(row["Total Cost"]),
            total_profit=float(row["Total Profit"]),
        )
