import json
import datetime
import requests as requests

def collect_VM_creation_data(thanos_URL, start_date, end_date):

    first = True
    delta = datetime.timedelta(days=1)
    result = {}

    while start_date <= end_date:
        URL = thanos_URL + "/api/v1/query_range?query=count(kube_pod_info%7Bpod%3D~%22virt-launcher.*%22%7D)&dedup=true&partial_response=true&start=" + datetime.timestamp(start_date) + "&end=" + datetime.timestamp(start_date + delta) + "&step=10&max_source_resolution=0s&_=1611676797922"
        
        response = requests.get(URL)
        response_json = json.loads(response.text)

        if first == True:
            result = response_json
            first = False
        else:
            for i in range(0, len(response_json['data']['result'][0]['values']) - 1):
                result['data']['result'][0]['values'].append(response_json['data']['result'][0]['values'][i])

        start_date += delta
    
    return result