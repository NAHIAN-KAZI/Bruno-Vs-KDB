#This code will read the data from the CSV file, create a radar chart for each player, and save the radar chart as a PNG file. 
#You can then add this code to your GitHub repo along with the CSV file.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the CSV file
df = pd.read_csv("KevinDeBruyne.csv")

# Get the list of player names
player_names = df["player_name"].tolist()

# Get the list of statistics
statistics = df.columns[1:]

# Create a radar chart for each player
for i, player_name in enumerate(player_names):
    values = df[statistics].iloc[i].tolist()

    # Create the radar chart
    plt.figure(figsize=(8, 6))
    plt.subplot(111, projection="radar")

    # Add the data
    plt.plot(statistics, values, label=player_name)

    # Add the grid
    plt.grid(True)

    # Add the labels for each axis
    plt.xticks(range(len(statistics)), statistics, rotation=45)

    # Add the title
    plt.title(f"Radar Chart of {player_name}")

    # Save the radar chart as a PNG file
    plt.savefig(f"{player_name}_radar_chart.png")

