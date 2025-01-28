scoreboard = {} # scoreboard as an empty dictionary

# Function to update the scoreboard
def update_scoreboard(player, score):
    """Add the player's score to the scoreboard.
    If the player is not already on the scoreboard, add them with a score of 0 first.
    Then add the new score to their total."""
    if player not in scoreboard:
        scoreboard[player] = 0
    scoreboard[player] = scoreboard[player] + score


def display_scoreboard():
    """Display the final scoreboard sorted by scores in descending order."""
    # Scoreboard header
    print("\n--- Scoreboard ---")

    # Check if the scoreboard is not empty
    if scoreboard:
        # Sort the scoreboard dictionary into a list of tuples, ordered by the score (second item in each tuple)
        # 'key=lambda x: x[1]' tells the sorted function to use the second element (the score) as the sorting key
        # 'reverse=True' ensures that the list is sorted in descending order (highest score first)
        sorted_scores = sorted(scoreboard.items(), key=lambda x: x[1], reverse=True)

        # Loop through the sorted scores and display them with their rank
        # 'enumerate' automatically adds a rank (starting from 1) to each tuple (player, score)
        for rank, (player, score) in enumerate(sorted_scores, start=1):
            # Print the rank, player name, and score in a formatted string
            print(f"{rank}. {player}: {score} points")

    # Print the scoreboard footer
    print("------------------------\n")

def main():
    update_scoreboard("Lee", 10)
    update_scoreboard("Marco", 15)
    update_scoreboard("Marcel", 20)
    update_scoreboard("Richard", 20)
    update_scoreboard("Natalia", 20)
    display_scoreboard()


if __name__ == "__main__":
    main()
