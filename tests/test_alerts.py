from alerts import AlertManager, AlertCondition, AlertType
from fetcher import StockData
from datetime import datetime

def test_alert_trigger():
    alert_mgr = AlertManager()
    alert_condition = AlertCondition(
        symbol="TCS.NS",
        alert_type=AlertType.PRICE_THRESHOLD,
        threshold=4000.0,
        comparison="above"
    )
    alert_mgr.add_alert(alert_condition)

    stock_data = StockData(
        symbol="TCS.NS",
        price=4100.0,
        volume=5000,
        timestamp=datetime.now(),
        high=4150.0,
        low=3900.0,
        open=4000.0,
        close=4100.0
    )

    alert_mgr.check_alerts(stock_data)
