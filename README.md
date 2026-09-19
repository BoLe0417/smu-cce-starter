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

4. Open the `notebooks/` folder in VS Code. Open a notebook, select a Python kernel if prompted, and run its cells from top to bottom. The notebooks retrieve current data from Yahoo Finance, so an internet connection is required.

## Code Walkthrough

- `notebooks/filings.ipynb` retrieves a company's income statement, balance sheet, and cash flow data.
- `notebooks/news.ipynb` retrieves and prints recent news for a stock ticker.
- `notebooks/stock_price_ratings.ipynb` retrieves the current stock price and recent analyst ratings.
- `lessons/` contains beginner-friendly course instructions for setting up Codespaces and running the project.
- `requirements.txt` lists the Python packages used by the notebooks, including `yfinance` and `pandas`.
- `README.md` provides an overview and setup guide.

To use the project, open one of the notebooks, run the import and function-definition cells, then run the final example cell with a ticker such as `MU` or `GOOG`. Each notebook calls Yahoo Finance through `yfinance`, processes the returned data, and displays the result as text or tables in the notebook. Run the notebooks independently depending on the type of financial information you need.

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
  ├── requirements.txt  # Python dependencies
  └── README.md         # Course overview