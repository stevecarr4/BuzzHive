import os
import pandas as pd

def save_analysis_results(data):
    """
    Save analysis results to a CSV file.
    """
    try:
        # Perform analysis and store the results in a dictionary
        analysis_results = {
            'Attack Type Counts': data['Attack Type'].value_counts(),
            'Common Attack Types': data['Attack Type'].value_counts().head(5),
            'IP Address Counts': data['IP Address'].value_counts(),
            # Add additional analysis results here
        }

        # Create a DataFrame from the analysis results
        df = pd.DataFrame(analysis_results)

        # Set the file path for saving the results in the "results" folder
        results_folder = 'results'
        file_path = os.path.join(results_folder, 'analysis_results.csv')

        # Save the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        print("Analysis results saved to", file_path)

    except KeyError as e:
        print("Error: Missing column", e)
