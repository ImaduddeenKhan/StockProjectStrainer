import pytest
import asyncio
from cache import CacheManager


@pytest.mark.asyncio
async def test_cache_operations():
    cache = CacheManager()

    stock_data = {"symbol": "TCS.NS", "price": 3500.0}

    await cache.set_stock_data("TCS.NS", stock_data)
    cached_data = await cache.get_stock_data("TCS.NS")

    assert cached_data["symbol"] == "TCS.NS"
    assert cached_data["price"] == 3500.0
