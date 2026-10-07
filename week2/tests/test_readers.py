from io import StringIO
from sales_processor.readers import read_sales


def test_read_sales() -> None:
    csv_data = """Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
Middle East and North Africa,Saudi Arabia,Baby Food,Offline,M,5/23/2010,12345,5/27/2010,100,255.28,159.42,25528,15942,9586
"""

    file = StringIO(csv_data)

    records = list(read_sales(file))

    assert len(records) == 1
    assert records[0].country == "Saudi Arabia"
    assert records[0].item_type == "Baby Food"