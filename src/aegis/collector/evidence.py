from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass
class Evidence:
    """
    Represents a single piece of evidence collected
    for flood risk assessment.
    """
    name:str
    value:Any
    unit:str
    source:str
    collected_at: datetime
    location:str
    status:str
    confidence:float = 1.0 #Range: 0.0-1.0

    