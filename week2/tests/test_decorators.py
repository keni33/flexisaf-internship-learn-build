from sales_processor.decorators import measure_time

def test_measure_time() -> None:
    @measure_time
    def add_numbers() -> int:
        return 2 + 3

    result = add_numbers()

    assert result == 5