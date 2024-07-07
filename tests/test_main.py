"""
This module contains tests for the main application.
"""
from src.main import main

def test_main(capsys):
    """Test the main function."""    
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
