import pytest
from most_active_cookie import *

def test_most_active_cookie():
    # Test a file with a single cookie on the specified date
    assert most_active_cookie('cookie_log.csv', '2018-12-09') == ['AtY0laUfhglK3lC7']
    
    # Test a file with multiple cookies on the specified date
    assert most_active_cookie('cookie_log.csv', '2018-12-08') == ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
    
    # Test a file with no cookies on the specified date
    assert most_active_cookie('cookie_log.csv', '2018-12-06') == []

    with pytest.raises(FileNotFoundError):
        most_active_cookie('nonexistent_file.csv', '2018-12-09')