from datetime import datetime
from .evidence import Evidence
import csv


class RainfallCollector:
    """Collect rainfall evidence for a district"""

    def collect(self, district:str)-> Evidence:
            latest_row = None

            with open("data/sample/rainfall.csv",newline="") as file:
                reader = csv.DictReader(file)

            
                for row in reader:
                    if row["district"].strip().lower()==district.strip().lower():
                        latest_row = row

                if latest_row is None:
                     return None

                return Evidence(
                    name="Rainfall",
                    value=float(latest_row["rainfall_mm"]),
                    unit="mm",
                    source=latest_row["source"],
                    collected_at=datetime.now(),
                    location=latest_row["district"],
                    status="Collected",
                    confidence=1.0, 
                )
        
