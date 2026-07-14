import logging
from datetime import datetime
from typing import Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Allowed transaction categories
ALLOWED_CATEGORIES = {
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Entertainment"
}


def validate_required_fields(payload: dict[str, Any]) -> list[str]:
    """
    Validate that all required fields are present.

    Args:
        payload: Transaction payload.

    Returns:
        List of validation error messages.
    """
    required_fields = [
        "transaction_id",
        "date",
        "amount",
        "category"
    ]

    errors = []

    for field in required_fields:
        if field not in payload:
            errors.append(f"Missing required field: {field}")

    return errors


def validate_date(date_str: str) -> str | None:
    """
    Validate that the date follows YYYY-MM-DD format.

    Args:
        date_str: Date string.

    Returns:
        Error message or None.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return None
    except ValueError:
        return "Invalid date. Expected format YYYY-MM-DD."


def validate_amount(amount: Any) -> str | None:
    """
    Validate transaction amount.

    Args:
        amount: Transaction amount.

    Returns:
        Error message or None.
    """
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        return "Amount must be numeric."

    if amount <= 0:
        return "Amount must be greater than zero."

    return None


def validate_category(category: str) -> str | None:
    """
    Validate transaction category.

    Args:
        category: Transaction category.

    Returns:
        Error message or None.
    """
    if category not in ALLOWED_CATEGORIES:
        return (
            f"Invalid category. "
            f"Allowed values: {', '.join(sorted(ALLOWED_CATEGORIES))}"
        )

    return None


def validate_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Validate an entire transaction payload.

    Args:
        payload: Transaction payload dictionary.

    Returns:
        Dictionary containing validation status and errors.
    """
    logger.info("Starting payload validation.")

    errors = validate_required_fields(payload)

    if errors:
        logger.warning("Payload is missing required fields.")
        return {
            "valid": False,
            "errors": errors
        }

    date_error = validate_date(payload["date"])
    if date_error:
        errors.append(date_error)

    amount_error = validate_amount(payload["amount"])
    if amount_error:
        errors.append(amount_error)

    category_error = validate_category(payload["category"])
    if category_error:
        errors.append(category_error)

    if errors:
        logger.warning("Payload validation failed.")
    else:
        logger.info("Payload validation successful.")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }