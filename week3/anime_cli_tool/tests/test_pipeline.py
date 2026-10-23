import unittest
import io
import sys
from pathlib import Path

# Add the root 'anime_cli_tool' directory to sys.path
root_dir = Path(__file__).resolve().parent.parent.parent # Adjust depending on how deep your folders are
sys.path.insert(0, str(root_dir))

# Now this will work:
from src.pipeline import process_dataset, calculate_means


class TestPipeline(unittest.TestCase):
    
    def test_process_dataset_valid_and_invalid(self):
        # 1. Create mock CSV data in memory using StringIO
        mock_csv_content = (
            "Category,Score\n"
            "Action,8.5\n"
            "Comedy,Unknown\n"  # Invalid: 'Unknown' score
            "Action,7.5\n"
            "Drama,9.0\n"
            "MissingColRow\n"   # Invalid: Missing column entirely
        )
        
       
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as temp:
            temp.write(mock_csv_content)
            temp_path = temp.name

        try:
            # 2. Run the processing pipeline
            grouped_data, invalid_records, stats = process_dataset(
                file_path=temp_path, 
                group_col="Category", 
                value_col="Score"
            )

            # 3. Assert stats are correct
            self.assertEqual(stats.total_rows, 5)     # 5 total rows (excluding header)
            self.assertEqual(stats.valid_rows, 3)     # Action (8.5), Action (7.5), Drama (9.0)
            self.assertEqual(stats.invalid_rows, 2)   # Comedy row + MissingColRow

            # 4. Assert aggregation grouping is correct
            self.assertIn("Action", grouped_data)
            self.assertEqual(grouped_data["Action"], [8.5, 7.5])
            self.assertEqual(grouped_data["Drama"], [9.0])

            # 5. Assert invalid records tracked the correct row numbers and reasons
            self.assertEqual(len(invalid_records), 2)
            self.assertEqual(invalid_records[0].row_number, 2)  # Comedy row
            self.assertIn("Unknown", invalid_records[0].reason)

        finally:
            # Clean up the temp file
            Path(temp_path).unlink(missing_ok=True)

    def test_calculate_means(self):
        # Test the mean calculation helper independently
        mock_grouped_data = {
            "Action": [8.0, 10.0],
            "Comedy": [5.0, 5.0, 5.0]
        }
        
        means = calculate_means(mock_grouped_data)
        
        self.assertEqual(means["Action"], 9.0)
        self.assertEqual(means["Comedy"], 5.0)

if __name__ == "__main__":
    unittest.main()