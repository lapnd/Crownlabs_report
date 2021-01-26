import json 
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_cumulative_graph(outJson):

    dates = [datetime.fromtimestamp(i['timestamp']) for i in outJson["results"]]
    dates = mdates.date2num(dates)
    values = [i['value'] for i in outJson['results']]

    df = pd.DataFrame({'dates':dates, 'values':values})
    df['dates']  = [pd.to_datetime(i) for i in df['dates']]

    fig, ax = plt.subplots()
    ax.plot_date(dates, values)
    plt.xticks(rotation=30)
    #plt.axis([0,15,0,3500])

    fig.savefig('number_of_vm_access_over_time.png', dpi=300)

def plot_cumulative_week_graph(outJson):

    startTime = datetime.fromtimestamp(outJson['results'][0]['timestamp'])
    firstVMCount = outJson['results'][0]['value']
    dates = []
    values = []

    for i in outJson['results']:
        currTime = datetime.fromtimestamp(i['timestamp'])

        if currTime.isocalendar()[1] != startTime.isocalendar()[1]:
            dates.append(startTime)
            values.append(i['value'] - firstVMCount)

            startTime = currTime
            firstVMCount = int(i['value'])
            
    fig, ax = plt.subplots()
    ax.bar(dates, values)
    plt.xticks(rotation=30)
    #plt.axis([0,15,0,700])

    fig.show()
    fig.savefig('number_of_vm_access_every_week.png', dpi=300)
