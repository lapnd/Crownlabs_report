import json 
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

def plot_cumulative_graph(outJson, image_name, x_label, y_label):

    dates = [datetime.fromtimestamp(i['timestamp']) for i in outJson["results"]]
    #dates = mdates.date2num(dates)
    values = [i['value'] for i in outJson['results']]

    df = pd.DataFrame({'dates':dates, 'values':values})
    #df['dates']  = [datetime.fromtimestamp(i) for i in df['dates']]

    fig, ax = plt.subplots(figsize=(7,3))
    formatter = mdates.DateFormatter("%d-%m-%Y")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.WeekdayLocator(byweekday=MO)
    ax.xaxis.set_major_locator(locator)
    ax.set_title(image_name.replace("_", " ").replace(".png", ""))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.grid(True)
    
    ax.plot_date(df['dates'], df['values'])
    
    fig.savefig("../report/img/" + image_name)

def plot_cumulative_week_graph(outJson, image_name, x_label, y_label):

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
          
    df = pd.DataFrame({'dates':dates, 'values':values})
    #df['dates']  = [pd.to_datetime(i) for i in df['dates']]
  
    fig, ax = plt.subplots(figsize=(7,3))
    formatter = mdates.DateFormatter("%d-%m-%Y")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.WeekdayLocator(byweekday=MO)
    ax.xaxis.set_major_locator(locator)
    ax.set_title(image_name.replace("_", " ").replace(".png", ""))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.xticks(fontsize=5)
    plt.yticks(fontsize=5)
    plt.grid(False)
    
    ax.bar(df['dates'], df['values'])

    fig.savefig("../report/img/" + image_name)
