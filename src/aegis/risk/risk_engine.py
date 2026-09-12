from ..models.validation_result import ValidationResult
from ..models.evidence_package import EvidencePackage
from ..models.risk_result import RiskResult
from .rainfall_assessor import RainfallAssessor 
from .dem_assessor import DEMAssessor
from ..config.overall_risk_thresholds import LOW_OVERALL_RISK,HIGH_OVERALL_RISK
from datetime import datetime

class RiskEngine:

    """Calculates flood risk from validated evidence"""

    def __init__(self):
        self.rainfall_assessor=RainfallAssessor()
        self.dem_assessor=DEMAssessor()


    def assess(self, package:EvidencePackage,validation_result:ValidationResult)-> RiskResult:

        if validation_result.status != "VALID":
            return RiskResult(
                risk_level= "NOT CALCULATED",
                risk_score=0,

                rainfall_assessment=None,
                dem_assessment=None,

                reasons=["Some required evidence is missing"],
                recommended_actions= ["Rerun the process"],

                confidence = 0.0,
                calculated_at=datetime.now()

            )


        rainfall_evidence = package.evidences.get("rainfall")
        dem_evidence = package.evidences.get("dem")


        rainfall_assessment = self.rainfall_assessor.assess(rainfall_evidence)
        dem_assessment = self.dem_assessor.assess(dem_evidence)


        overall_score = rainfall_assessment.score + dem_assessment.score

        if overall_score <= LOW_OVERALL_RISK:
            overall_risk_level = "LOW"

        elif overall_score <= HIGH_OVERALL_RISK:
            overall_risk_level = "MEDIUM"

        else: overall_risk_level = "HIGH"

        reasons = [rainfall_assessment.reason,dem_assessment.reason]

        if overall_risk_level=="HIGH":

            recommended_actions = [
                """Notify district emergency team.""",
                """Inspect low-lying settlements.""",
                """Increase rainfall monitoring."""
                ]

        elif overall_risk_level=="MEDIUM":

            recommended_actions = [
                """Continue monitoring.""",
                """Review weather forecasts every 6 hours."""
                ]

        else: recommended_actions = [

            """Routine monitoring."""
            ]

        return RiskResult(

            risk_level=overall_risk_level,
            risk_score=overall_score,

            rainfall_assessment= rainfall_assessment,
            dem_assessment= dem_assessment,

            reasons=reasons,
            recommended_actions=recommended_actions,

            confidence=1.0,
            calculated_at=datetime.now()

        )







