"""A beginner-friendly Streamlit interface for the finance notebooks."""

import streamlit as st

from analysis import get_analyst_ratings, get_financials, get_news, get_price


st.set_page_config(page_title="Stock Analysis", layout="wide")
st.title("Stock Analysis")
st.write("Explore company filings, recent news, or stock price and analyst ratings.")

ticker = st.text_input("Ticker symbol", value="MU", help="For example: MU, GOOG, or AAPL")
analysis_type = st.selectbox(
    "Analysis type",
    ["filings", "news", "stock price ratings"],
)

if st.button("Run", type="primary"):
    ticker = ticker.strip().upper()
    if not ticker:
        st.error("Enter a ticker symbol first.")
    else:
        try:
            with st.spinner(f"Loading {analysis_type} for {ticker}..."):
                if analysis_type == "filings":
                    results = get_financials(ticker)
                    st.subheader(f"Financial filings for {ticker}")
                    for name, table in results.items():
                        st.write(f"**{name}**")
                        if table is None or table.empty:
                            st.info(f"No {name.lower()} data is available.")
                        else:
                            st.dataframe(table, use_container_width=True)

                elif analysis_type == "news":
                    articles = get_news(ticker)
                    st.subheader(f"Recent news for {ticker}")
                    if articles.empty:
                        st.info("No recent news was found.")
                    else:
                        st.dataframe(articles, use_container_width=True, hide_index=True)

                else:
                    price = get_price(ticker)
                    st.subheader(f"Price and analyst ratings for {ticker}")
                    if price is None:
                        st.metric("Current price", "Unavailable")
                        st.info("The current share price is not available for this ticker.")
                    else:
                        st.metric("Current price", f"${price:,.2f}")

                    ratings = get_analyst_ratings(ticker)
                    st.write("**Latest analyst recommendations**")
                    if ratings.empty:
                        st.info("No analyst recommendations were found.")
                    else:
                        st.dataframe(ratings, use_container_width=True)
        except Exception as error:
            st.error(f"Could not load data for {ticker}. Check the ticker and try again.")
            st.caption(f"Details: {error}")