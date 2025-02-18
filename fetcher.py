import yfinance as yf
from pydantic import BaseModel
from datetime import datetime


class StockData(BaseModel):
    symbol: str
    price: float
    volume: int
    timestamp: datetime
    high: float
    low: float
    open: float
    close: float


class DataFetcher:
    async def fetch_stock_data(self, symbol: str) -> StockData:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d", interval="1m")
        if data.empty:
            raise ValueError(f"No stock data found for {symbol}")

        latest = data.iloc[-1]
        return StockData(
            symbol=symbol,
            price=latest["Close"],
            volume=int(latest["Volume"]),
            timestamp=datetime.now(),
            high=latest["High"],
            low=latest["Low"],
            open=latest["Open"],
            close=latest["Close"],
        )
