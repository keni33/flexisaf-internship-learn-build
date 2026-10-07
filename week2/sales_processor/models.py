from dataclasses import dataclass

@dataclass
class SaleRecord:
    region: str
    country: str
    item_type: str
    sales_channel: str
    order_priority: str
    order_date: str
    order_id: str
    ship_date: str
    units_sold: int
    unit_price: float
    unit_cost: float
    total_revenue: float
    total_cost: float
    total_profit: float