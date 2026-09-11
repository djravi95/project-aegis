from dataclasses import dataclass

@dataclass

class EmptyAssessmentResult:

    evidence_name:str
    score:float
    level:str
    reason:str 