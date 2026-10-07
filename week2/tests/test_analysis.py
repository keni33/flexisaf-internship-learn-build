from sales_processor.analysis import (
    highest_sales_country,
    lowest_profit_country,
    most_requested_item,
)
from sales_processor.models import SaleRecord


def create_records() -> list[SaleRecord]:
    return [
        SaleRecord(
            region="Africa",
            country="Nigeria",
            item_type="Fruits",
            sales_channel="Online",
            order_priority="M",
            order_date="1/1/2010",
            order_id="1",
            ship_date="1/3/2010",
            units_sold=10,
            unit_price=10.0,
            unit_cost=5.0,
            total_revenue=100.0,
            total_cost=50.0,
            total_profit=50.0,
        ),
        SaleRecord(
            region="Africa",
            country="Ghana",
            item_type="Fruits",
            sales_channel="Online",
            order_priority="M",
            order_date="1/1/2010",
            order_id="2",
            ship_date="1/4/2010",
            units_sold=5,
            unit_price=10.0,
            unit_cost=6.0,
            total_revenue=50.0,
            total_cost=30.0,
            total_profit=20.0,
        ),
    ]


def test_highest_sales_country() -> None:
    records = create_records()

    country, revenue = highest_sales_country(records)

    assert country == "Nigeria"
    assert revenue == 100.0


def test_lowest_profit_country() -> None:
    records = create_records()

    country, profit = lowest_profit_country(records)

    assert country == "Ghana"
    assert profit == 20.0


def test_most_requested_item() -> None:
    records = create_records()

    item, count = most_requested_item(records)

    assert item == "Fruits"
    assert count == 2