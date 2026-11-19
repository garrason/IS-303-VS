from pathlib import Path

import pandas as pd


def main():
    raw_path = Path(__file__).with_name("video_games_raw.csv")
    cleaned_path = raw_path.with_name("video_games_cleaned.csv")
    games = pd.read_csv(raw_path)

    print("VIDEO GAME CATALOG MANAGER")
    if games.empty:
        print("There are no games to inspect.")
        return

    # Use zero-based row numbers so row 4 matches the assignment example.
    while True:
        try:
            
            row_number = int(input("Enter a row number to inspect: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 0 <= row_number < len(games):
            break
        print(f"Please enter a row number from 0 to {len(games) - 1}.")

    selected_game = games.iloc[row_number]
    print("\nSelected Game:")
    for column in ["Title", "Platform", "Genre", "Rating"]:
        print(f"{column}: {selected_game[column]}")
    print(f"Current Status: {selected_game['Status']}")

    statuses = ("Backlog", "Playing", "Completed", "Dropped")
    while True:
        new_status = input("Enter a new status: ").strip().title()
        if new_status in statuses:
            break
        print(f"Please enter one of these statuses: {', '.join(statuses)}.")

    games.at[selected_game.name, "Status"] = new_status

    games["Recommended"] = "No"
    meets_criteria = (games["Rating"] >= 8) & (games["Price"] <= 40)
    games.loc[meets_criteria, "Recommended"] = "Yes"

    recommended_games = games.query("Recommended == 'Yes'")
    print("\nRecommended Games:")
    print(recommended_games[["Title", "Platform", "Price", "Rating"]])

    games.to_csv(cleaned_path, index=False)
    print("\nThe catalog has been updated.")
    print(f"Saved as {cleaned_path.name}.")


if __name__ == "__main__":
    main()
