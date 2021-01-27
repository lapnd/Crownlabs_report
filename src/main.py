import data_collect as collect
import data_process as process
import plotgen as plot
from datetime import datetime 
from tqdm import tqdm

def main():
    thanos_URL = "http://10.100.99.4:9090" 
    start_date = datetime(2021, 1, 16)
    end_date = datetime(2021, 1, 18)

    # collect data from thanos
    vm_creation_data = collect.collect_VM_creation_data(thanos_URL, start_date, end_date)
    vm_access_data = collect.collect_VM_access_data(thanos_URL, start_date, end_date)

    # process data
    vm_creation_data_processed = process.process_VM_creation_data(vm_creation_data)
    vm_access_data_processed = process.process_VM_access_data(vm_access_data)
    
    # plot processed data
    with tqdm(total=4, desc="Plot data:", bar_format= '{l_bar}{bar}') as pbar:
        plot.plot_cumulative_graph(vm_creation_data_processed, "VM_creation_comulative.png")
        pbar.update(1)
        plot.plot_cumulative_week_graph(vm_creation_data_processed, "VM_creation_cumulative_week.png")
        pbar.update(1)
        plot.plot_cumulative_graph(vm_access_data_processed, "VM_access_cumulative.png")
        pbar.update(1)
        plot.plot_cumulative_week_graph(vm_access_data_processed, "VM_access_cumulative_week.png")
        pbar.update(1)

if __name__ == "__main__":
    main()