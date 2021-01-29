import json 
from datetime import datetime
from tqdm import tqdm

def process_VM_creation_data(jsonData):
    startVMValue = int(jsonData['data']['result'][0]['values'][0][1])
    vmCount = startVMValue
    result = []

    # Iterating through the json 
    # list 
    with tqdm(total=len(jsonData['data']['result'][0]['values']), desc="Processing VM creation data:", bar_format= '{l_bar}{bar}') as pbar:
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
    with tqdm(total=len(jsonData['data']['result'][0]['values']), desc="Processing VM access data:", bar_format= '{l_bar}{bar}') as pbar:
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

def process_single_VM_access(accessJson, creationJson):
    accessJsonProcessed = []
    creationJsonProcessed = []

    with tqdm(total=1, desc="Processing single VM access data:", bar_format= '{l_bar}{bar}') as pbar:
        startTime = datetime.fromtimestamp(accessJson['results'][0]['timestamp'])
        firstCount = accessJson['results'][0]['value']
        for i in accessJson['results']:
            currTime = datetime.fromtimestamp(i['timestamp'])

            if currTime.date() != startTime.date():
                value = {
                    "date": startTime.date(),
                    "value": int(i['value']) - firstCount
                }

                accessJsonProcessed.append(value)

                startTime = currTime
                firstCount = int(i['value'])

        startTime = datetime.fromtimestamp(creationJson['results'][0]['timestamp'])
        firstCount = creationJson['results'][0]['value']
        for i in creationJson['results']:
            currTime = datetime.fromtimestamp(i['timestamp'])

            if currTime.date() != startTime.date():
                value = {
                    "date": startTime.date(),
                    "value": int(i['value']) - firstCount
                }

                creationJsonProcessed.append(value)

                startTime = currTime
                firstCount = int(i['value'])

        result = []
        for i in accessJsonProcessed:
            for j in creationJsonProcessed:
                if i['date'] == j['date']:
                    if int(j['value']) == 0:
                        value = {
                        "timestamp": int(i['date'].strftime("%s")),
                        "value": int(i['value'])
                        }
                    else :
                        value = {
                        "timestamp": int(i['date'].strftime("%s")),
                        "value": int(i['value'])/int(j['value'])
                        }

                    result.append(value)
                    break
        
        finalResult = {
            "results": result
        }
        
        pbar.update(1)

    return finalResult
