# Script to be ran on the ol' pie
import requests
import time
from sense_hat import SenseHat
from datetime import datetime

URL = "http://127.0.0.1:5000/api/data"

s = SenseHat()
 

while True:
  data = {
    "tempData": [datetime.now().isoformat(), s.get_temperature()]
  }

  requests.post(URL, json=data)
  time.sleep(1)
