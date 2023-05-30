import os
import pandas as pd

def analyze_data(data):
    """
    Analyze the data and perform advanced analysis.
    """
    try:
        # Analyze trends
        attack_counts = data['Attack Type'].value_counts()
        print("\nAttack Type Counts:")
        print(attack_counts)

        # Identify common attack types
        common_attacks = attack_counts.head(5)
        print("\nMost Common Attack Types:")
        print(common_attacks)

        # Trace IP addresses
        ip_addresses = data['IP Address'].value_counts()
        print("\nIP Address Counts:")
        print(ip_addresses)

        # Perform additional analysis here
        
        # Create the results directory if it doesn't exist
        results_dir = 'results'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        # Save analysis results to a CSV file
        analysis_results = {
            'Attack Type Counts': attack_counts,
            'Common Attack Types': common_attacks,
            'IP Address Counts': ip_addresses,
        }

        df = pd.DataFrame(analysis_results)
        df.to_csv(os.path.join(results_dir, 'analysis_results.csv'), index=False)
        print("Analysis results saved to analysis_results.csv in the results folder.")

    except KeyError as e:
        print("Error: Missing column", e)
