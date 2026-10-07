from sales_processor.models import SaleRecord
from sales_processor.generators import filter_by_country


def test_filter_by_country() -> None:
    records = [
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
        )
    ]

    result = list(filter_by_country(records, "Nigeria"))

    assert len(result) == 1
    assert result[0].country == "Nigeria"