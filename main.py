import asyncio
from monitor import StockMonitor
from alerts import AlertCondition, AlertType

async def main():
    monitor = StockMonitor(["TCS.NS", "RELIANCE.NS"])

    # Add alert for TCS
    monitor.alert_manager.add_alert(AlertCondition(
        symbol="TCS.NS",
        alert_type=AlertType.PRICE_THRESHOLD,
        threshold=4000.0,
        comparison="above"
    ))

    await monitor.monitor_stocks()

if __name__ == "__main__":
    asyncio.run(main())
