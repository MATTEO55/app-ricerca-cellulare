"""
Phone number search service - Business logic for phone number operations.
"""

from typing import Dict, Any, Optional
from src.utils import (
    validate_phone_number,
    format_phone_number,
    get_operator_by_prefix,
    clean_phone_number
)


class PhoneNumberService:
    """Service class for phone number operations"""
    
    @staticmethod
    def search_number(phone_number: str) -> Optional[Dict[str, Any]]:
        """
        Search for phone number information.
        
        Args:
            phone_number: Phone number to search
        
        Returns:
            dict: Phone number information or None if invalid
        """
        # Clean the phone number
        clean_number = clean_phone_number(phone_number)
        
        # Validate format
        if not validate_phone_number(clean_number):
            return None
        
        # Get operator information
        prefix = clean_number[:4]
        operator = get_operator_by_prefix(prefix)
        
        if not operator:
            return None
        
        return {
            'original': phone_number,
            'formatted': format_phone_number(clean_number),
            'clean': clean_number,
            'prefix': prefix,
            'operator': operator['name'],
            'country': operator['country'],
            'is_valid': True
        }
    
    @staticmethod
    def validate(phone_number: str) -> Dict[str, Any]:
        """
        Validate phone number and return validation result.
        
        Args:
            phone_number: Phone number to validate
        
        Returns:
            dict: Validation result
        """
        clean_number = clean_phone_number(phone_number)
        is_valid = validate_phone_number(clean_number)
        
        return {
            'original': phone_number,
            'clean': clean_number,
            'is_valid': is_valid,
            'message': 'Valid phone number' if is_valid else 'Invalid phone number format'
        }
    
    @staticmethod
    def format_for_display(phone_number: str) -> str:
        """
        Format phone number for display.
        
        Args:
            phone_number: Phone number to format
        
        Returns:
            str: Formatted phone number
        """
        clean_number = clean_phone_number(phone_number)
        return format_phone_number(clean_number) if validate_phone_number(clean_number) else phone_number
