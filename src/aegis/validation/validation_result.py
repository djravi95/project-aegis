from dataclasses import dataclass
from datetime import datetime

@dataclass
class ValidationResult:

    status:str
    validated:list[str]
    missing:list[str]
    warnings:list[str]
    validation_time:datetime
    