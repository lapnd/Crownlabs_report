import json 
from datetime import datetime
import plotgen

# Opening JSON file 
f = open('thanos_query.json',) 
  
# returns JSON object as  
# a dictionary 
jsonData = json.load(f) 

vmAccessCount = 1
result = []

# Iterating through the json 
# list 
for i in range(1, len(jsonData['data']['result'][0]['values'])): 
    if jsonData['data']['result'][0]['values'][i][1] != jsonData['data']['result'][0]['values'][i-1][1] :
        vmAccessCount += 1

    value = {
        "timestamp": int(jsonData['data']['result'][0]['values'][i][0]),
        "vmAccess": vmAccessCount
    }

    result.append(value)

outJson = {
    "vmCumulativeAccess": result
}

with open('thanos_query_processed.json', 'w') as outfile:
    json.dump(outJson, outfile)
