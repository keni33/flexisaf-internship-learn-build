from contextlib import contextmanager
from collections.abc import Generator
from typing import TextIO

@contextmanager
def sales_files(
    csv_path: str,
    output_path: str,
) -> Generator[tuple[TextIO, TextIO], None, None]:
    """
    Open the input CSV and output report file.

    The files are automatically closed when the
    with-block finishes.
    """

    print("Opening sales files...")

    try:
        with (
            open(csv_path, "r", encoding="utf-8") as input_file,
            open(output_path, "w", encoding="utf-8") as output_file,
        ):
            yield input_file, output_file

    finally:
        print("Sales files closed.")
