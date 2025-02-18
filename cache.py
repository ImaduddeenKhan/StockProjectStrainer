import asyncio

class CacheManager:
    def __init__(self):
        self.cache = {}

    async def get_stock_data(self, symbol: str):
        """Retrieve stock data from in-memory cache"""
        return self.cache.get(symbol, None)

    async def set_stock_data(self, symbol: str, data: dict, ttl: int = 300):
        """Store stock data in cache with expiration"""
        self.cache[symbol] = data
        asyncio.create_task(self.expire_cache(symbol, ttl))

    async def expire_cache(self, symbol: str, ttl: int):
        """Simulate cache expiration after TTL"""
        await asyncio.sleep(ttl)
        if symbol in self.cache:
            del self.cache[symbol]
