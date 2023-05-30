import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    """
    Visualize the data.
    """
    try:
        # Set up a plot style
        sns.set(style="whitegrid", font_scale=1.2)

        # Plotting the data
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Bar plot of attack types
        ax1 = axs[0, 0]
        attack_counts = data['Attack Type'].value_counts()
        sns.barplot(x=attack_counts.index, y=attack_counts.values, palette="viridis", ax=ax1)
        ax1.set_title('Top Attack Types', fontsize=16)
        ax1.set_xlabel('Attack Type', fontsize=12)
        ax1.set_ylabel('Count', fontsize=12)
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')

        # Pie chart of attack types
        ax2 = axs[0, 1]
        attack_counts.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Attack Type Distribution', fontsize=16)
        ax2.set_ylabel('')

        # Histogram of IP address counts
        ax3 = axs[1, 0]
        ip_counts = data['IP Address'].value_counts()
        sns.histplot(data=ip_counts, ax=ax3, bins=20)
        ax3.set_title('IP Address Counts', fontsize=16)
        ax3.set_xlabel('Count', fontsize=12)
        ax3.set_ylabel('Frequency', fontsize=12)

        # Line plot of attacks over time
        ax4 = axs[1, 1]
        attacks_by_day = data['Timestamp'].value_counts().sort_index()
        attacks_by_day.plot(ax=ax4, linewidth=2)
        ax4.set_title('Attacks Over Time', fontsize=16)
        ax4.set_xlabel('Date', fontsize=12)
        ax4.set_ylabel('Count', fontsize=12)

        # Plot Enhancement
        plt.tight_layout()
        plt.show()

    except KeyError as e:
        print("Error: Missing column", e)
