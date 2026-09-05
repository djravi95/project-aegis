from ..models.evidence_package import EvidencePackage
from .validation_result import ValidationResult
from ..config.required_evidence import REQUIRED_EVIDENCE
from datetime import datetime   


class ValidationEngine:
    """Validates evidences before risk assessment"""

    def validate(self,package: EvidencePackage)-> ValidationResult:
            
            validated = []
            missing = []
            warnings = []
            status =""

            for evidence_name in REQUIRED_EVIDENCE:

                evidence = package.evidences.get(evidence_name)

                if evidence is not None:
                    validated.append(evidence_name)

                elif evidence is None:
                    missing.append(evidence_name)
                    warnings.append(f"Requires evidence '{evidence_name}' is missing.")


            if not missing:

                     status="VALID"

            elif not validated:

                     status="INVALID"

            else: status = "PARTIAL"

            return ValidationResult(

                   status=status,
                   validated=validated,
                   missing=missing,
                   warnings=warnings,
                   validation_time=datetime.now() 
                 
            )

