import csv
from typing import Iterator,Tuple, Dict, List, Callable
from collections import defaultdict
from models import InvalidRecord, ProcessingStats

def stream_csv(file_path: str) ->Iterator[Tuple[int, Dict[str,str]]]:
    """Generator that lazily yields row number and row dictionary from a CSV file."""
    with open(file_path, mode='r', encoding='utf-8', errors='replace')as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            yield idx, row
def process_dataset(
        file_path: str,
        group_col: str, 
        value_col: str
) -> Tuple[Dict[str,List[float]], List[InvalidRecord], ProcessingStats]:
    """Generic processing pipeline: streams data, validates numeric types, and groups values by a specified categorical column"""
    grouped_data = defaultdict(list)
    invalid_records: List[InvalidRecord] = []
    stats = ProcessingStats()
    for row_num, row in stream_csv(file_path):
        stats.total_rows += 1
        #Check if required column  in this specific CSV   
        if group_col not  in row or value_col not in row:
            invalid_records.append(InvalidRecord(row_number=row_num, raw_data=row, reason=f"Missing required columns ({group_col} or {value_col})"))
            stats.invalid_rows += 1
            continue
        try:
            #Clean and validate fields generically
            raw_val = row[value_col].strip()
            if raw_val.lower() in ('unknown', 'n/a', '', 'null'):
                raise ValueError(f"Value '{raw_val}' is invalid or missing.")
            numeric_val = float(raw_val)
            category = row[group_col].strip()
            if not category:
                category = "Unknown"
            grouped_data[category].append(numeric_val)
            stats.valid_rows += 1
        except (ValueError, TypeError) as e:
            invalid_records.append(InvalidRecord(row_number=row_num, raw_data=row, reason=str(e)))
            stats.invalid_rows += 1

    return grouped_data, invalid_records, stats
def calculate_means(grouped_data: Dict[str, List[float]]) -> Dict[str, float]:
    """Computes average for each group."""
    return{
        group: sum(values) / len(values)
        for group, values in grouped_data.items() if values
    }