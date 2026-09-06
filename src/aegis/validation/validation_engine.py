from ..models.evidence_package import EvidencePackage
from .validation_result import ValidationResult
from ..config.required_evidence import REQUIRED_EVIDENCE
from datetime import datetime   


class ValidationEngine:
    """Validates evidences before risk assessment"""

    def validate(self,package: EvidencePackage)-> ValidationResult:

            validation_details ={}
            warnings =[]

            for evidence_name in REQUIRED_EVIDENCE:

                evidence = package.evidences.get(evidence_name)

                if evidence is not None:
                    validation_details[evidence_name] = "VALID"

                else:
                     validation_details[evidence_name] = "MISSING"
                     warnings.append(f"Required evidence '{evidence_name}' is missing.")

        
            statuses =list(validation_details.values())
            valid_count = statuses.count("VALID")
            missing_count = statuses.count("MISSING")
                        
            if valid_count==len(REQUIRED_EVIDENCE):
                 overall_status="VALID"

            elif missing_count == len(REQUIRED_EVIDENCE):

                     overall_status="INVALID"

            else: overall_status = "PARTIAL"

            return ValidationResult(

                   status=overall_status,
                   validation_details=validation_details,
                   warnings=warnings,
                   validation_time=datetime.now() 
                 
            )

