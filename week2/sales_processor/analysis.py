from collections import defaultdict
from collections.abc import Iterable, Iterator
from datetime import datetime

from sales_processor.models import SaleRecord


def highest_sales_country(
    records: Iterable[SaleRecord],
) -> tuple[str, float]:
    """Return the country with the highest total revenue."""

    country_sales: dict[str, float] = defaultdict(float)

    for record in records:
        country_sales[record.country] += record.total_revenue

    highest_country = max(
        country_sales,
        key=country_sales.get,
    )

    return highest_country, country_sales[highest_country]


def lowest_profit_country(
    records: Iterable[SaleRecord],
) -> tuple[str, float]:
    """Return the country with the lowest total profit."""

    country_profit: dict[str, float] = defaultdict(float)

    for record in records:
        country_profit[record.country] += record.total_profit

    lowest_country = min(
        country_profit,
        key=country_profit.get,
    )

    return lowest_country, country_profit[lowest_country]


def most_requested_item(
    records: Iterable[SaleRecord],
) -> tuple[str, int]:
    """Return the item type that appears most often."""

    item_counts: dict[str, int] = defaultdict(int)

    for record in records:
        item_counts[record.item_type] += 1

    most_requested = max(
        item_counts,
        key=item_counts.get,
    )

    return most_requested, item_counts[most_requested]


def item_types_sold(
    records: Iterable[SaleRecord],
) -> set[str]:
    """Return all unique item types sold."""

    items: set[str] = set()

    for record in records:
        items.add(record.item_type)

    return items


def delivery_days(record: SaleRecord) -> int:
    """Calculate the number of days between ordering and shipping."""

    order_date = datetime.strptime(
        record.order_date,
        "%m/%d/%Y",
    )

    ship_date = datetime.strptime(
        record.ship_date,
        "%m/%d/%Y",
    )

    return (ship_date - order_date).days


def fastest_delivery_country(
    records: Iterable[SaleRecord],
) -> tuple[str, float]:
    """Return the country with the lowest average delivery time."""

    delivery_totals: dict[str, int] = defaultdict(int)
    delivery_counts: dict[str, int] = defaultdict(int)

    for record in records:
        days = delivery_days(record)

        delivery_totals[record.country] += days
        delivery_counts[record.country] += 1

    average_delivery: dict[str, float] = {}

    for country in delivery_totals:
        average_delivery[country] = (
            delivery_totals[country]
            / delivery_counts[country]
        )

    fastest_country = min(
        average_delivery,
        key=average_delivery.get,
    )

    return fastest_country, average_delivery[fastest_country]


def analyse_sales(
    records: Iterator[SaleRecord],
) -> dict[str, object]:
    """Analyse all sales in one pass through the generator."""

    country_revenue: dict[str, float] = defaultdict(float)
    country_profit: dict[str, float] = defaultdict(float)

    country_delivery_total: dict[str, int] = defaultdict(int)
    country_delivery_count: dict[str, int] = defaultdict(int)

    item_counts: dict[str, int] = defaultdict(int)
    item_types: set[str] = set()

    for record in records:
        # Revenue
        country_revenue[record.country] += record.total_revenue

        # Profit
        country_profit[record.country] += record.total_profit

        # Items
        item_counts[record.item_type] += 1
        item_types.add(record.item_type)

        # Delivery
        days = delivery_days(record)

        country_delivery_total[record.country] += days
        country_delivery_count[record.country] += 1

    highest_country = max(
        country_revenue,
        key=country_revenue.get,
    )

    lowest_profit_country = min(
        country_profit,
        key=country_profit.get,
    )

    most_requested_item = max(
        item_counts,
        key=item_counts.get,
    )

    average_delivery = {
        country: (
            country_delivery_total[country]
            / country_delivery_count[country]
        )
        for country in country_delivery_total
    }

    fastest_country = min(
        average_delivery,
        key=average_delivery.get,
    )

    return {
        "highest_sales_country": (
            highest_country,
            country_revenue[highest_country],
        ),
        "fastest_delivery_country": (
            fastest_country,
            average_delivery[fastest_country],
        ),
        "most_requested_item": (
            most_requested_item,
            item_counts[most_requested_item],
        ),
        "lowest_profit_country": (
            lowest_profit_country,
            country_profit[lowest_profit_country],
        ),
        "item_types": item_types,
    }
