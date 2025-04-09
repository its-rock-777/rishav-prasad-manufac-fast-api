from pydantic import BaseModel
from typing import Optional

class SensorData(BaseModel):
    timestamp: str
    sensor_1: float
    sensor_2: float
    sensor_3: float
    sensor_4: Optional[float] = None
