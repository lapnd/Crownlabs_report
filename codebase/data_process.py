import json 
from datetime import datetime

def process_VM_creation_data(jsonData):
    vmAccessCount = 1
    result = []

    # Iterating through the json 
    # list 
    for i in range(1, len(jsonData['data']['result'][0]['values'])): 
        if jsonData['data']['result'][0]['values'][i][1] != jsonData['data']['result'][0]['values'][i-1][1] :
            vmAccessCount += 1

        value = {
            "timestamp": int(jsonData['data']['result'][0]['values'][i][0]),
            "value": vmAccessCount
        }

        result.append(value)

    outJson = {
        "results": result
    }

    with open('VM_creation_data_processed.json', 'w') as outfile:
        json.dump(outJson, outfile)

    return outJson
