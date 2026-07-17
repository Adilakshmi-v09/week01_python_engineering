# Transaction Payload Validator

## Overview

This project validates transaction-like JSON payloads using Python. It checks whether a transaction contains all required fields and validates the transaction ID, date, amount, and category.

The project follows clean engineering practices with:

* Modular validation functions
* Type hints and docstrings
* Structured validation responses
* Logging for validation events
* Unit testing using pytest
* JSON-driven test data validation

## Project Structure

```text
week01_python_engineering/
│
├── validators.py
├── test_validators.py
├── sample_payloads.json
├── requirements.txt
└── README.md
```

## Features

* Validate required transaction fields
* Validate transaction ID format
* Validate date format (`YYYY-MM-DD`)
* Validate transaction amount
* Validate allowed transaction categories
* Return structured validation errors
* Logging for validation status
* Unit tests using pytest
* Parameterized testing using JSON payload data

## Requirements

* Python 3.10 or above
* pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Validator

Import the validator and call the `validate_payload()` function:

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

Example output:

```python
{
    "valid": True,
    "errors": []
}
```

## Running Tests

Run all tests:

```bash
py -m pytest -v
```

The test suite includes:

* Static unit tests for individual validation rules
* JSON-driven parameterized tests using `sample_payloads.json`

Current test coverage:

```
20 tests passed
```

## Validation Rules

* All required fields must be present:

  * transaction_id
  * date
  * amount
  * category

* Transaction ID:

  * Must be a string
  * Must not be empty

* Date:

  * Must follow `YYYY-MM-DD` format

* Amount:

  * Must be numeric
  * Must be greater than zero

* Category:

  * Must belong to the allowed categories:

    * Food
    * Travel
    * Shopping
    * Bills
    * Entertainment

## Testing Approach

The project uses two types of tests:

### Static Unit Tests

Static test cases verify specific validation rules:

* Missing required fields
* Invalid date format
* Invalid numeric values
* Unexpected categories
* Successful payload validation

### JSON-Driven Tests

Additional payload scenarios are stored in `sample_payloads.json`.

The test suite loads these payloads and uses `pytest.mark.parametrize` to execute the validator against multiple inputs.

This approach keeps test data separate from test logic and allows new scenarios to be added easily.

## Assumptions

* Input payload must be a Python dictionary.
* Date format is fixed as `YYYY-MM-DD`.
* Category validation is case-insensitive.
* Transaction amount must always be positive.
* Validation functions do not modify the original payload.
* Logs contain validation information without exposing sensitive transaction details.

## Expected Output

### Successful Validation

```python
{
    "valid": True,
    "errors": []
}
```

### Validation Failure

```python
{
    "valid": False,
    "errors": [
        "Invalid date. Expected format YYYY-MM-DD."
    ]
}
```
