from pathlib import Path
import pandas as pd

# Read the CSV from the same folder as this Python file.
csv_path = Path(__file__).with_name("cfb.csv")
football_data = pd.read_csv(csv_path)

season = int(input("Enter a year to analyze that CFB season: "))

season_data = football_data.query("Season == @season")

if season_data.empty:
    print(f"No results found for the {season} CFB season.")
else:
    # Each dictionary value is an empty list of teams.
    win_categories = {
        "10 or more wins": [],
        "8–9 wins": [],
        "6–7 wins": [],
        "Fewer than 6 wins": []}
    
    # Process one row at a time.
    for index, row in season_data.iterrows():
        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            win_categories["10 or more wins"].append(team)
        elif wins >= 8:
            win_categories["8–9 wins"].append(team)
        elif wins >= 6:
            win_categories["6–7 wins"].append(team)
        else:
            win_categories["Fewer than 6 wins"].append(team)

    print(f"\nCollege Football Results for {season}")

    for category, teams in win_categories.items():
        print(f"\n{category}:")

        for team in teams:
            print(f"  {team}")