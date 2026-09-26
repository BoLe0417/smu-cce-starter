"""Data-fetching functions adapted from the project notebooks."""

import pandas as pd
import yfinance as yf


def get_financials(ticker):
    """Return the latest income statement, balance sheet, and cash flow."""
    stock = yf.Ticker(ticker)
    return {
        "Income Statement": stock.financials,
        "Balance Sheet": stock.balance_sheet,
        "Cash Flow": stock.cashflow,
    }


def get_news(ticker):
    """Return up to five recent news articles as a DataFrame."""
    articles = yf.Ticker(ticker).news or []
    rows = []

    for article in articles[:5]:
        content = article.get("content", article)
        provider = content.get("provider", {})
        link = content.get("canonicalUrl") or content.get("clickThroughUrl") or {}
        rows.append(
            {
                "Title": content.get("title") or "No title",
                "Description": content.get("description") or content.get("summary", ""),
                "Publisher": provider.get("displayName") or content.get("publisher", ""),
                "Published": (
                    content.get("pubDate")
                    or content.get("displayTime")
                    or content.get("providerPublishTime", "")
                ),
                "Link": (link.get("url") or content.get("link", ""))
                if isinstance(link, dict)
                else content.get("link", ""),
            }
        )

    return pd.DataFrame(rows)


def get_price(ticker):
    """Return the current share price, or None when it is unavailable."""
    info = yf.Ticker(ticker).info
    return info.get("currentPrice") or info.get("regularMarketPrice")


def get_analyst_ratings(ticker):
    """Return the most recent ten analyst recommendations."""
    recommendations = yf.Ticker(ticker).recommendations
    if recommendations is None:
        return pd.DataFrame()
    return recommendations.tail(10)