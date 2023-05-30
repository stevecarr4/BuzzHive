from data_loader import load_data
from data_validator import validate_data
from data_analyzer import analyze_data
from data_visualizer import visualize_data
from data_saver import save_analysis_results
from combine_data import combine_data

def main():
    # File paths for the three data sources
    honeypot_data_file = 'data/honeypot_data.csv'
    honeypot_data2_file = 'data/honeypot_data2.csv'
    honeypot_data3_file = 'data/honeypot_data3.csv'

    # Load the data from the three sources
    honeypot_data = load_data(honeypot_data_file)
    honeypot_data2 = load_data(honeypot_data2_file)
    honeypot_data3 = load_data(honeypot_data3_file)

    if honeypot_data is not None and honeypot_data2 is not None and honeypot_data3 is not None:
        # Validate the data from each source
        validate_data(honeypot_data)
        validate_data(honeypot_data2)
        validate_data(honeypot_data3)

        # Combine the data from the three sources
        combined_data = combine_data(honeypot_data, honeypot_data2, honeypot_data3)

        # Analyze the combined data
        analyze_data(combined_data)

        # Visualize the combined data
        visualize_data(combined_data)

        # Save the analysis results
        save_analysis_results(combined_data)

if __name__ == "__main__":
    main()
