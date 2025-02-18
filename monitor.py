import asyncio
from fetcher import DataFetcher
from cache import CacheManager
from alerts import AlertManager, AlertCondition, AlertType
from config import FETCH_INTERVAL

class StockMonitor:
    def __init__(self, symbols):
        self.fetcher = DataFetcher()
        self.cache = CacheManager()
        self.alert_manager = AlertManager()
        self.symbols = symbols

    async def monitor_stocks(self):
        while True:
            for symbol in self.symbols:
                try:
                    data = await self.fetcher.fetch_stock_data(symbol)
                    await self.cache.set_stock_data(symbol, data.dict())
                    self.alert_manager.check_alerts(data)
                except Exception as e:
                    print(f"Error fetching data for {symbol}: {e}")

            await asyncio.sleep(FETCH_INTERVAL)  # Wait before next fetch cycle
