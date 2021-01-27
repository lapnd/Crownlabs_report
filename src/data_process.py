import json 
from datetime import datetime
from tqdm import tqdm

def process_VM_creation_data(jsonData):
    startVMValue = int(jsonData['data']['result'][0]['values'][0][1])
    vmCount = startVMValue
    result = []

    # Iterating through the json 
    # list 
    with tqdm(total=len(jsonData['data']['result'][0]['values']), desc="Processing VM creation data: ") as pbar:
        for i in jsonData['data']['result'][0]['values']: 
            vmDiff = int(i[1]) - startVMValue

            if vmDiff > 0:
                vmCount += vmDiff

            value = {
                "timestamp": int(i[0]),
                "value": vmCount
            }

            result.append(value)

            pbar.update(1)
            startVMValue = int(i[1])

    pbar.update(1)
    outJson = {
        "results": result
    }

    with open('../report/data/VM_creation_data_processed.json', 'w') as outfile:
        json.dump(outJson, outfile)

    return outJson

def process_VM_access_data(jsonData):
    vmAccessCount = 1
    result = []

    # Iterating through the json 
    # list 
    with tqdm(total=len(jsonData['data']['result'][0]['values']), desc="Processing VM access data:   ") as pbar:
        for i in range(1, len(jsonData['data']['result'][0]['values'])): 
            if jsonData['data']['result'][0]['values'][i][1] != jsonData['data']['result'][0]['values'][i-1][1] :
                vmAccessCount += 1

            value = {
                "timestamp": int(jsonData['data']['result'][0]['values'][i][0]),
                "value": vmAccessCount
            }

            result.append(value)
            pbar.update(1)

    pbar.update(1)
    outJson = {
        "results": result
    }

    with open('../report/data/VM_access_data_processed.json', 'w') as outfile:
        json.dump(outJson, outfile)

    return outJson