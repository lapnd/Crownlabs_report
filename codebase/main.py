import data_collect as collect
import data_process as process
import plotgen as plot
import datetime 

def main():
    thanos_URL = "https://thanos.crownlabs.polito.it" 
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 1, 26)

    data = collect.collect_VM_creation_data(thanos_URL, start_date, end_date)
    processed_data = process.process_VM_creation_data(data)
    plot.plot_cumulative_graph(processed_data)

if __name__ == "__main__":
    main()