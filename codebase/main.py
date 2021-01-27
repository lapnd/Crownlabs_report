import data_collect as collect
import data_process as process
import plotgen as plot
from datetime import datetime 

def main():
    thanos_URL = "http://10.100.99.4:9090" 
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 1, 26)

    # collect data from thanos
    vm_creation_data = collect.collect_VM_creation_data(thanos_URL, start_date, end_date)
    vm_access_data = collect.collect_VM_access_data(thanos_URL, start_date, end_date)

    # process data
    vm_creation_data_processed = process.process_VM_creation_data(vm_creation_data)
    
    # plot processed data
    plot.plot_cumulative_graph(vm_creation_data_processed)
    plot.plot_cumulative_week_graph(vm_creation_data_processed)

if __name__ == "__main__":
    main()