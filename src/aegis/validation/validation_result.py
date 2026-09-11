from dataclasses import dataclass
from datetime import datetime

@dataclass
class ValidationResult:

    status:str
    validation_details:dict[str,str]
    warnings:list[str]
    validation_time:datetime
    