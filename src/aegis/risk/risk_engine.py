from ..models.validation_result import ValidationResult
from ..models.evidence_package import EvidencePackage
from ..models.risk_result import RiskResult
from .rainfall_assessor import RainfallAssessor 
from .dem_assessor import DEMAssessor
from ..config.overall_risk_thresholds import LOW_OVERALL_RISK,HIGH_OVERALL_RISK

class RiskEngine:

    """Calculates flood risk from validated evidence"""

    def __init__(self):
        self.rainfall_assessor=RainfallAssessor()
        self.dem_assessor=DEMAssessor()


    def assess(self, package:EvidencePackage,validation_result:ValidationResult)-> RiskResult:

        if validation_result.status != "VALID":
            return RiskResult()


        rainfall_evidence = package.evidences.get("rainfall")
        dem_evidence = package.evidences.get("dem")


        rainfall_assessment = self.rainfall_assessor.assess(rainfall_evidence)
        dem_assessment = self.dem_assessor.assess(dem_evidence)


        overall_score = rainfall_assessment.score + dem_assessment.score

        






