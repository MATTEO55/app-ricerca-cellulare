"""
Utilities module - Common utility functions for the application.
"""

import re
from typing import Optional, Dict, Any


def validate_phone_number(phone_number: str) -> bool:
    """
    Validate Italian mobile phone number.
    
    Args:
        phone_number: Phone number string to validate
    
    Returns:
        bool: True if valid, False otherwise
    
    Example:
        >>> validate_phone_number("3312345678")
        True
    """
    # Italian mobile numbers: start with 3 and have 10 digits total
    pattern = r'^3[0-9]{9}$'
    return bool(re.match(pattern, phone_number))


def format_phone_number(phone_number: str) -> str:
    """
    Format phone number for display.
    
    Args:
        phone_number: Phone number string
    
    Returns:
        str: Formatted phone number
    
    Example:
        >>> format_phone_number("3312345678")
        "331 2345678"
    """
    if not validate_phone_number(phone_number):
        return phone_number
    
    return f"{phone_number[:3]} {phone_number[3:10]} {phone_number[10:]}"


def get_operator_by_prefix(prefix: str) -> Optional[Dict[str, Any]]:
    """
    Get mobile operator information by number prefix.
    
    Args:
        prefix: Phone number prefix (first 4 digits)
    
    Returns:
        dict: Operator information or None if not found
    
    Note:
        This is a placeholder. In production, this would query a database.
    """
    # Italian mobile operators and their prefixes
    operators = {
        '3301': {'name': 'Vodafone', 'country': 'Italy'},
        '3302': {'name': 'Vodafone', 'country': 'Italy'},
        '3303': {'name': 'Vodafone', 'country': 'Italy'},
        '3310': {'name': 'TIM', 'country': 'Italy'},
        '3311': {'name': 'TIM', 'country': 'Italy'},
        '3312': {'name': 'TIM', 'country': 'Italy'},
        '3313': {'name': 'TIM', 'country': 'Italy'},
        '3315': {'name': 'Wind Tre', 'country': 'Italy'},
        '3316': {'name': 'Wind Tre', 'country': 'Italy'},
        '3317': {'name': 'Wind Tre', 'country': 'Italy'},
        '3320': {'name': 'Iliad', 'country': 'Italy'},
        '3321': {'name': 'Iliad', 'country': 'Italy'},
    }
    
    return operators.get(prefix)


def clean_phone_number(phone_number: str) -> str:
    """
    Remove spaces, dashes, and parentheses from phone number.
    
    Args:
        phone_number: Phone number string
    
    Returns:
        str: Cleaned phone number
    
    Example:
        >>> clean_phone_number("(331) 234-5678")
        "3312345678"
    """
    return re.sub(r'[\s\-\(\)]', '', phone_number)


def is_valid_email(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email: Email string to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
