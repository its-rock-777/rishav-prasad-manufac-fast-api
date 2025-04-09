from typing import List
from models.data_model import SensorData

def analyze_data(data: List[SensorData]):
    count = len(data)
    sensor1_avg = sum(d.sensor_1 for d in data) / count
    sensor2_avg = sum(d.sensor_2 for d in data) / count
    sensor3_avg = sum(d.sensor_3 for d in data) / count

    return {
        "total_records": count,
        "sensor_1_avg": round(sensor1_avg, 2),
        "sensor_2_avg": round(sensor2_avg, 2),
        "sensor_3_avg": round(sensor3_avg, 2),
    }
