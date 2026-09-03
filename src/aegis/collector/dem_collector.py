from .evidence import Evidence
from datetime import datetime
import csv


class DemCollector:
    """Used for collecting DEM Data"""

    def collect(self,district:str)-> Evidence:
        latest_row = None

        with open("data/sample/dem.csv",newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["district"].strip().lower()==district.strip().lower():
                    latest_row = row

            if latest_row is None:
                return None
            

            return Evidence(
                name="DEM",
                value=float(latest_row["elevation_m"]),
                unit="m",
                source=latest_row["source"],
                collected_at=datetime.now(),
                location=latest_row["district"],
                status="Collected",
                confidence=1.0,
)
                
