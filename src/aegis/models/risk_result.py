from datetime import datetime
from dataclasses import dataclass
from ..models.assessment_result import AssessmentResult


@dataclass
class RiskResult:

    risk_level: str
    risk_score: float

    rainfall_assessment: AssessmentResult | None
    dem_assessment: AssessmentResult | None

    reasons: list[str]
    recommended_actions: list[str]

    confidence: float


    calculated_at: datetime