from ..models.validation_result import ValidationResult
from ..models.risk_result import RiskResult


class TerminalPresenter:
    """Displays Project Aegis results in the terminal."""

    def display(self, package, validation_result, risk_result):

        print("=" * 60)
        print(f"{'PROJECT AEGIS':^60}")
        print("=" * 60)
        print()

        print(f"{'District':<20}: {package.district}")
        print(f"{'Analysis Time':<20}: {package.analysis_time}")
        print()

        # Evidence Summary
        print("-" * 60)
        print("Evidence Summary")
        print("-" * 60)

        for evidence_name, evidence in package.evidences.items():

            if evidence is None:
                print(f"{'Name':<20}: {evidence_name}")
                print(f"{'Status':<20}: Missing")
                print()
                continue

            print(f"{'Name':<20}: {evidence.name}")
            print(f"{'Value':<20}: {evidence.value} {evidence.unit}")
            print(f"{'Source':<20}: {evidence.source}")
            print(f"{'Location':<20}: {evidence.location}")
            print(f"{'Status':<20}: {evidence.status}")
            print(f"{'Confidence':<20}: {evidence.confidence}")
            print()

        # Validation Summary
        print("-" * 60)
        print("Validation Summary")
        print("-" * 60)

        for evidence_name, status in validation_result.validation_details.items():

            if status == "VALID":
                symbol = "✓"
            else:
                symbol = "✗"

            display_name = evidence_name.upper()

            print(f"{display_name:<20}: {symbol} {status}")

        print()
        print(f"{'Overall Status':<20}: {validation_result.status}")
        print()

        # Warnings
        print("-" * 60)
        print("Warnings")
        print("-" * 60)

        if not validation_result.warnings:
            print("None")
        else:
            for warning in validation_result.warnings:
                print(f"• {warning}")

        print()

        # Risk Assessment
        print("-" * 60)
        print("Risk Assessment")
        print("-" * 60)

        if risk_result.risk_level == "NOT CALCULATED":

            print(f"{'Status':<20}: NOT CALCULATED")
            print(f"{'Reason':<20}: Mandatory evidence is missing.")
            print()
            print("No risk score was calculated.")

        else:

            print(f"{'Overall Risk':<20}: {risk_result.risk_level}")
            print(f"{'Risk Score':<20}: {risk_result.risk_score} / 100")
            print(f"{'Confidence':<20}: {risk_result.confidence}")

            print()
            print("Risk Contribution")
            print("-" * 60)

            print(
                f"{'Rainfall':<20}: "
                f"{risk_result.rainfall_assessment.score}"
            )

            print(
                f"{'DEM':<20}: "
                f"{risk_result.dem_assessment.score}"
            )

            print()
            print("Rainfall Assessment")
            print("-" * 60)
            print()

            print(
                f"{'Level':<20}: "
                f"{risk_result.rainfall_assessment.level}"
            )

            print(
                f"{'Score':<20}: "
                f"{risk_result.rainfall_assessment.score}"
            )

            print(
                f"{'Reason':<20}: "
                f"{risk_result.rainfall_assessment.reason}"
            )

            print()
            print("DEM Assessment")
            print("-" * 60)
            print()

            print(
                f"{'Level':<20}: "
                f"{risk_result.dem_assessment.level}"
            )

            print(
                f"{'Score':<20}: "
                f"{risk_result.dem_assessment.score}"
            )

            print(
                f"{'Reason':<20}: "
                f"{risk_result.dem_assessment.reason}"
            )

        print()

        # Recommended Actions
        print("-" * 60)
        print("Recommended Actions")
        print("-" * 60)

        for action in risk_result.recommended_actions:
            print(f"• {action}")

        print()
        print("=" * 60)