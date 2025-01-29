from app import calculate_sum, app


def test_positive_sum():
    """Test case for positive numbers."""
    assert calculate_sum(10, 5) == 15


def test_negative_sum():
    """Test case for negative numbers."""
    assert calculate_sum(-5, -7) == -12


def test_mixed_sum():
    """Test case for mixed positive and negative numbers."""
    assert calculate_sum(-3, 7) == 4


def test_zero_sum():
    """Test case for zero as input."""
    assert calculate_sum(0, 0) == 0


def test_invalid_filter_value():
    """Test case for invalid filter value."""
    client = app.test_client()
    response = client.get('/sum/result/invalid')
    assert response.status_code == 404
