# Installation Instructions

This project is easiest to run in GitHub Codespaces, but the same steps also work on a computer with Python installed.

1. Open a terminal and clone this repository:

    ```bash
    git clone https://github.com/<your-username>/smu-cce-starter.git
    cd smu-cce-starter
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

    On Windows, activate it with `.venv\Scripts\activate` instead.

3. Install the required Python packages:

    ```bash
    python -m pip install -r requirements.txt
    ```

4. Start the Streamlit application:

    ```bash
    python -m streamlit run src/app.py
    ```

    In GitHub Codespaces, open the forwarded port shown in the terminal. In the **Ports** tab, set that port's visibility to **Public**, then select **Open in Browser**. The app retrieves current data from Yahoo Finance, so an internet connection is required.

## Code Walkthrough

- `notebooks/filings.ipynb` retrieves a company's income statement, balance sheet, and cash flow data.
- `notebooks/news.ipynb` retrieves recent news for a stock ticker.
- `notebooks/stock_price_ratings.ipynb` retrieves the current stock price and recent analyst ratings.
- `src/app.py` is the Streamlit user interface; `src/analysis.py` contains reusable data-fetching functions based on the notebooks.
- `lessons/` contains beginner-friendly course instructions for setting up Codespaces and running the project.
- `requirements.txt` lists the Python packages used by the notebooks, including `yfinance` and `pandas`.
- `README.md` provides an overview and setup guide.

The app starts with the ticker `MU`. Enter a ticker symbol, choose **filings**, **news**, or **stock price ratings**, and select **Run**. The app calls Yahoo Finance through `yfinance` and displays the results in tables or a price metric. The notebooks remain available as the original examples of each analysis.

 # Cloud Computing for Economics: Starter Repo 

  This repository contains the starter code and lesson materials for building a Python financial-data application and deploying it to AWS.

  Students will use GitHub Codespaces, Python, Jupyter notebooks, Streamlit, Git, and AWS CloudFormation.

  ## Learning outcomes

  By the end of the course, you will be able to:

   1.  Build and deploy an analytics application with a simple Front End / back-end (using AI)
   2.  Host and share the application on a cloud platform (e.g., AWS EC2 or similar) so that others can access it securely over the web
   3.  Integrate data sources and APIs into the app to enable interactive, real-time analytics
   4.  Apply cloud architecture best practices, ensuring the app demonstrates scalability, performance efficiency, and basic security
   5.  Showcase your work on GitHub as part of a personal portfolio, demonstrating practical cloud and analytics skills through a shareable, explorable repository

  
  ## Repository structure

  ```text
  .
  ├── lessons/          # Step-by-step course instructions
  ├── notebooks/        # Starter financial-data notebooks
    ├── src/              # Streamlit app and reusable analysis functions
  ├── requirements.txt  # Python dependencies
  └── README.md         # Course overview