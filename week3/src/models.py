from dataclasses import dataclass, field
from typing import Dict, Any
@dataclass(frozen=True)
class InvalidRecord:
    row_number: int
    raw_data: Dict[str, str]
    reason: str

@dataclass
class ProcessingStats:
    total_rows: int = 0
    valid_rows: int = 0
    invalid_rows: int = 0


