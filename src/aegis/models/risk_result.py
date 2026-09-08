from datetime import datetime
from dataclasses import dataclass


@dataclass
class RiskResult:
    overall_risk_level: str
    overall_risk_score: float
    evidence_scores: dict[str, float]
    confidence: float
    reasons: list[str]
    recommended_actions: list[str]
    mandatory_evidence_used: list[str]
    calculated_at: datetime