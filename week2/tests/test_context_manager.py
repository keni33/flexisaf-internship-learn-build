from pathlib import Path
from sales_processor.context_managers import sales_files

def test_sales_files(tmp_path: Path) -> None:
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.txt"

    input_file.write_text("Country,Total Revenue\nNigeria,100")

    with sales_files(
        str(input_file),
        str(output_file),
    ) as (infile, outfile):

        content = infile.read()

        assert "Nigeria" in content
        assert not outfile.closed

    assert outfile.closed