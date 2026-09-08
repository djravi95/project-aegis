from dataclasses import dataclass

@dataclass

class AssessmentResult:

    evidence_name:str
    score:float
    level:str
    reason:str 