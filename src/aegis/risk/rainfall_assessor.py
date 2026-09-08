from ..models.evidence import Evidence
from ..models.assessment_result import AssessmentResult
from ..config.risk_threshold import LOW_RAINFALL,HIGH_RAINFALL
from ..config.risk_scores import LOW_RAINFALL_SCORE,HIGH_RAINFALL_SCORE,MEDIUM_RAINFALL_SCORE

class RainfallAssessor:

    """
    Assesses rainfall evidence and returns its contribution
    to the overall flood risk.
    """

    

    def assess(self,evidence: Evidence):

        rainfall = evidence.value

        if rainfall < LOW_RAINFALL:

            level = "LOW"

        elif rainfall <= HIGH_RAINFALL:
            level = "MEDIUM"

        else:
            level = "HIGH"


        if level=="HIGH":
            score = HIGH_RAINFALL_SCORE
        elif level =="MEDIUM":
            score = MEDIUM_RAINFALL_SCORE
        else: score = LOW_RAINFALL_SCORE


        if level=="LOW":
            reason = f"Rainfall below {LOW_RAINFALL}mm"
        elif level == "MEDIUM":
            reason = f"Rainfall between {LOW_RAINFALL}mm and {HIGH_RAINFALL}mm"
        else: reason = f"Rainfall exceeded {HIGH_RAINFALL} mm"


        return AssessmentResult(

            evidence_name="Rainfall",
            score=score,
            level=level,
            reason=reason
        )



    




