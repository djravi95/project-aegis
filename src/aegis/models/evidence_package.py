from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from .evidence import Evidence

@dataclass
class EvidencePackage:
    """If every collector returns evidence, what common fields should every piece of evidence have?"""
    district:str
    analysis_time: datetime
    evidences: Dict[str,Evidence]
    collection_status:str
