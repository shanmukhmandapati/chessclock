import time

def chess_clock(player1_name, player2_name, initial_time):
    player1_time = initial_time
    player2_time = initial_time
    current_player = 1

    print(f"Welcome to the Chess Clock Game!")
    print(f"{player1_name} vs {player2_name}")
    print(f"Initial time for each player: {initial_time} seconds\n")

    while True:
        if current_player == 1:
            print(f"{player1_name}'s turn. Press Enter to start the clock.")
            input()
            start_time = time.time()
            input(f"{player1_name}, press Enter to stop the clock.")
            elapsed_time = time.time() - start_time
            player1_time -= elapsed_time
            current_player = 2
        else:
            print(f"{player2_name}'s turn. Press Enter to start the clock.")
            input()
            start_time = time.time()
            input(f"{player2_name}, press Enter to stop the clock.")
            elapsed_time = time.time() - start_time
            player2_time -= elapsed_time
            current_player = 1

        print(f"\n{player1_name}: {player1_time:.2f} seconds")
        print(f"{player2_name}: {player2_time:.2f} seconds\n")

        if player1_time <= 0:
            print(f"{player2_name} wins by time!")
            break
        elif player2_time <= 0:
            print(f"{player1_name} wins by time!")
            break

if __name__ == "__main__":
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    initial_time = int(input("Enter the initial time in seconds: "))

    chess_clock(player1_name, player2_name, initial_time)