# Transaction Payload Validator

## Overview

This project validates transaction-like JSON payloads using Python. It checks whether a transaction contains all required fields and validates the date, amount, and category.

## Project Structure

```
week01_python_engineering/
│
├── validators.py
├── test_validators.py
├── sample_payloads.json
├── requirements.txt
└── README.md
```

## Features

* Validate required fields
* Validate date format (YYYY-MM-DD)
* Validate transaction amount
* Validate allowed transaction categories
* Return clear validation errors
* Unit tests using pytest
* Logging for validation events

## Requirements

* Python 3.10 or above
* pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Validator

Import the validator and call:

```python
from validators import validate_payload

payload = {
    "transaction_id": "TX001",
    "date": "2026-07-14",
    "amount": 250,
    "category": "Food"
}

result = validate_payload(payload)
print(result)
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Or run only the validator tests:

```bash
pytest test_validators.py -v
```

## Validation Rules

* All required fields must exist.
* Date must follow YYYY-MM-DD.
* Amount must be numeric and greater than zero.
* Category must be one of:

  * Food
  * Travel
  * Shopping
  * Bills
  * Entertainment

## Assumptions

* Input payload is a Python dictionary.
* Date format is fixed as YYYY-MM-DD.
* Categories are case-sensitive.
* Transaction amount must be positive.

## Expected Output

Successful validation:

```python
{
    "valid": True,
    "errors": []
}
```

Validation failure:

```python
{
    "valid": False,
    "errors": [
        "Invalid date. Expected format YYYY-MM-DD."
    ]
}
```
