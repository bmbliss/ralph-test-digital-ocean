"""Simple test runner for calc module."""

from calc import add, subtract, multiply, divide


def test_add():
    """Test add function."""
    assert add(2, 3) == 5
    assert add(-2, -3) == -5
    assert add(-2, 3) == 1
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(2.5, 3.5) == 6.0
    print("✓ All add tests passed")


def test_subtract():
    """Test subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(-2, 3) == -5
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(5.5, 2.5) == 3.0
    print("✓ All subtract tests passed")


def test_multiply():
    """Test multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, -3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0
    print("✓ All multiply tests passed")


def test_divide():
    """Test divide function."""
    assert divide(6, 3) == 2
    assert divide(-6, -3) == 2
    assert divide(-6, 3) == -2
    assert divide(5.0, 2.0) == 2.5
    assert divide(0, 5) == 0

    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

    print("✓ All divide tests passed")


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("\n✓ All tests passed successfully!")
