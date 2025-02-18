from enum import Enum
from pydantic import BaseModel

class AlertType(Enum):
    PRICE_THRESHOLD = "price_threshold"

class AlertCondition(BaseModel):
    symbol: str
    alert_type: AlertType
    threshold: float
    comparison: str  # "above" or "below"

class AlertManager:
    def __init__(self):
        self.alerts = []

    def add_alert(self, condition: AlertCondition):
        self.alerts.append(condition)

    def check_alerts(self, stock_data):
        for alert in self.alerts:
            if alert.comparison == "above" and stock_data.price > alert.threshold:
                print(f"🚨 ALERT: {stock_data.symbol} price is ABOVE {alert.threshold}!")
            elif alert.comparison == "below" and stock_data.price < alert.threshold:
                print(f"🚨 ALERT: {stock_data.symbol} price is BELOW {alert.threshold}!")
