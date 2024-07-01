# Square POS Tip Calculator

## Purpose

The Square POS Tip Calculator is a Python application designed to fetch transaction data from the Square API, categorize tips, and calculate payouts after applying specific deduction rates. This tool is useful for businesses that use Square POS systems and need to manage and distribute tips efficiently.

## Features

- Fetch transactions from the Square API within a specified date range.
- Categorize tips into dine-in, takeout, and gratuity.
- Calculate payouts after applying deduction rates for each category.
- Debug and verbose modes for detailed output.

## Requirements

To run the Square POS Tip Calculator, you need the following:

- Python 3.6 or higher
- A Square API account and access token
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yumpire/squaretools.git
    cd squaretools
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your Square API credentials in a configuration file or environment variables.

2. Update the deduction rates in `config.py` if needed:
    ```python
    DINE_IN_DEDUCTION_RATE = 0.95
    TAKEOUT_DEDUCTION_RATE = 0.85
    GRATUITY_DEDUCTION_RATE = 0.90
    ```

## Usage

Run the application with the following command:
