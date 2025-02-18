import pytest
from fetcher import DataFetcher


@pytest.mark.asyncio
async def test_fetch_stock_data():
    fetcher = DataFetcher()
    data = await fetcher.fetch_stock_data("TCS.NS")

    assert data.symbol == "TCS.NS"
    assert data.price > 0
    assert data.volume >= 0
