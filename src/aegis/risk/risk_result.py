from dataclasses import dataclass
from datetime import datetime

@dataclass
class RiskResult:

    risk_level: str
    confidence: float
    reasons: list[str]
    recommendation: str
    calculated_at: datetime