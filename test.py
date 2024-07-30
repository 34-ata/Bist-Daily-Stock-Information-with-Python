import requests
from datetime import datetime
import json
import pandas as pd

time = datetime.now()
timestamp = datetime.timestamp(time)
url = "https://yatirim.akbank.com/_vti_bin/AkbankYatirimciPortali/Hisse/Service.svc/HisseDetaylari"

req = requests.get(url=url)

returnvalue = json.loads(req.text)

data = pd.DataFrame(returnvalue['Data'])

print(data)
		
	