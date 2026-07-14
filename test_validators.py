import pytest

from validators import (
    validate_required_fields,
    validate_date,
    validate_amount,
    validate_category,
    validate_payload,
)


def test_missing_required_fields():
    payload = {
        "transaction_id": "TX001",
        "amount": 100
    }

    result = validate_payload(payload)

    assert result["valid"] is False
    assert "Missing required field: date" in result["errors"]
    assert "Missing required field: category" in result["errors"]


def test_invalid_date():
    payload = {
        "transaction_id": "TX001",
        "date": "2026/01/01",
        "amount": 100,
        "category": "Food"
    }

    result = validate_payload(payload)

    assert result["valid"] is False
    assert "Invalid date. Expected format YYYY-MM-DD." in result["errors"]


def test_invalid_numeric_value():
    payload = {
        "transaction_id": "TX001",
        "date": "2026-01-01",
        "amount": -50,
        "category": "Food"
    }

    result = validate_payload(payload)

    assert result["valid"] is False
    assert "Amount must be greater than zero." in result["errors"]


def test_non_numeric_amount():
    payload = {
        "transaction_id": "TX001",
        "date": "2026-01-01",
        "amount": "abc",
        "category": "Food"
    }

    result = validate_payload(payload)

    assert result["valid"] is False
    assert "Amount must be numeric." in result["errors"]


def test_unexpected_category():
    payload = {
        "transaction_id": "TX001",
        "date": "2026-01-01",
        "amount": 250,
        "category": "Medical"
    }

    result = validate_payload(payload)

    assert result["valid"] is False
    assert any("Invalid category" in error for error in result["errors"])


def test_successful_payload():
    payload = {
        "transaction_id": "TX001",
        "date": "2026-01-01",
        "amount": 250.50,
        "category": "Food"
    }

    result = validate_payload(payload)

    assert result["valid"] is True
    assert result["errors"] == []