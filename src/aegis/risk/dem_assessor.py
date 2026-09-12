from ..models.evidence import Evidence
from ..models.assessment_result import AssessmentResult
from ..config.risk_threshold import LOW_ELEVATION
from ..config.risk_weights import HIGH_DEM_SCORE,LOW_DEM_SCORE



class DEMAssessor:

     def assess(self,evidence:Evidence):

        dem = evidence.value

        if dem <= LOW_ELEVATION:
            level = "HIGH SUSCEPTIBILITY"

        else: level = "LOW SUSCEPTIBILITY"

        if level=="HIGH SUSCEPTIBILITY":
            score = HIGH_DEM_SCORE
        else:score=LOW_DEM_SCORE

        if score==HIGH_DEM_SCORE:
            reason = f"Elevation is below {LOW_ELEVATION}m, increasing flood susceptibility."
        else: reason = f"Elevation is above {LOW_ELEVATION}m, reducing flood susceptibility."  


        return AssessmentResult(

            evidence_name="DEM",
            score=score,
            level=level,
            reason=reason

        )
          
            