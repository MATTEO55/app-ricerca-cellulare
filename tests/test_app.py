"""
Tests for the main application module.
"""

import pytest
from app import main, __version__


def test_version():
    """Test that version is properly defined"""
    assert __version__ == "0.1.0"


def test_main_runs():
    """Test that main function runs without errors"""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised {type(e).__name__} unexpectedly!")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
