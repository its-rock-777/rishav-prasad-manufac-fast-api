import csv
from typing import List
from models.data_model import SensorData

def parse_csv(file_path: str) -> List[SensorData]:
    data = []
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            item = SensorData(
                timestamp=row["timestamp"],
                sensor_1=float(row["sensor_1"]),
                sensor_2=float(row["sensor_2"]),
                sensor_3=float(row["sensor_3"]),
                sensor_4=float(row["sensor_4"]) if row.get("sensor_4") else None,
            )
            data.append(item)
    return data
