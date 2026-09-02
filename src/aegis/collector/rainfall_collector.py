from datetime import datetime
from .evidence import Evidence


class RainfallCollector:
    """Collect rainfall evidence for a district"""

    def collect(self, district:str)-> Evidence:
        return Evidence(

            name="Rainfall",
            value=120.5,
            unit="mm",
            source="Sample Dataset",
            collected_at=datetime.now(),
            location=district,
            status="Collected",
            confidence=1.0,
        )