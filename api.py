import requests
from datetime import datetime
import json
import pandas as pd
import sys

time = datetime.now()
timestamp = datetime.timestamp(time)
url = "https://yatirim.akbank.com/_vti_bin/AkbankYatirimciPortali/Hisse/Service.svc/HisseDetaylari"

req = requests.get(url=url)

returnvalue = json.loads(req.text)

data = pd.DataFrame(returnvalue['Data'])

new_data = data[data['dailyVolume'] != "0,00"]

filtered_data = new_data[new_data['Title'].str.contains(r'\.E\.', regex=True)]
if len(sys.argv) > 1:
    result = filtered_data[filtered_data['Title'].str.contains(sys.argv[1], case=False, regex=False)]
    if result.empty:
        print("Couldn\'t found")
    else:
        print(result)
else:
    print(filtered_data)