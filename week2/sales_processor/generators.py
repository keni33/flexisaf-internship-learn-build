from collections.abc import Iterator

from sales_processor.models import SaleRecord


def filter_by_country(
    records: Iterator[SaleRecord],
    country: str,
) -> Iterator[SaleRecord]:
    """Yield only records belonging to the requested country."""
    for record in records:
        if record.country.casefold() == country.casefold():
            yield record

def calculate_delivery_days(
    records: Iterator[SaleRecord],
) -> Iterator[SaleRecord]:
    """Yield records without altering their order."""
    for record in records:
        yield record


def filter_by_country(
    records: Iterator[SaleRecord],
    country: str,
) -> Iterator[SaleRecord]:
    """Yield only records belonging to the selected country."""
    for record in records:
        if record.country.casefold() == country.casefold():
            yield record


def filter_by_item(
    records: Iterator[SaleRecord],
    item_type: str,
) -> Iterator[SaleRecord]:
    """Yield only records matching the selected item type."""
    for record in records:
        if record.item_type.casefold() == item_type.casefold():
            yield record