import pytest
from script import filter_data, aggregate_data

mock_data = [
    {"price": "100", "rating": "4.5"},
    {"price": "200", "rating": "4.6"},
    {"price": "300", "rating": "4.8"}
]

def test_filter_gt():
    result = filter_data(mock_data, "price>150")
    assert len(result) == 2

def test_aggregate_avg():
    result = aggregate_data(mock_data, "price=avg")
    assert result == 200
