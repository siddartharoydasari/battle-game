import random
import time

def game():
    Player1_HP = 100
    Player2_HP = 100
    Player1_defending = False
    Player2_defending = False
    turn = 1
    print("Game Starting...")
    
    while(Player1_HP > 0 and Player2_HP > 0):
        print("\n------Turn Start-------")
        print('Player 1 HP:', Player1_HP)
        print('Player 2 HP:', Player2_HP)

        if(turn == 1):
            print("Player 1's Turn")
            action = input("Choose attack or defend: ")
            action = random.choice(['attack', 'defend'])
            if(action == 'attack'):
                damage = random.randint(10, 20)  # Random attack damage between 10 and 20
                print("Generating attack.....💥")
                time.sleep(2)
                if(Player2_defending):  # If Player 2 is defending, reduce damage by half
                    damage = damage // 2
                    Player2_defending = False
                Player2_HP -= damage  # Apply damage to Player 2
                print("Player 1 has attacked Player 2 for", damage, "damage!⚔️")
            else:
                Player1_defending = True  # Player 1 is defending this turn
            turn = 2  # Switch turn to Player 2

        else:
            print("Player 2's Turn")
            action = input("Choose attack or defend: ")
            action = random.choice(['attack', 'defend'])
            if(action == 'attack'):
                damage = random.randint(10, 20)  # Random attack damage between 10 and 20
                print("Generating attack.....💥")
                time.sleep(2)
                if(Player1_defending):  # If Player 1 is defending, reduce damage by half
                    damage = damage // 2
                    Player1_defending = False
                Player1_HP -= damage  # Apply damage to Player 1
                print("Player 2 has attacked Player 1 for", damage, "damage!⚔️")
            else:
                Player2_defending = True  # Player 2 is defending this turn
            turn = 1  # Switch turn to Player 1

    # Check for winner
    if(Player1_HP > 0):
        print('Player 1 is the winner🏆')
        return 'Player 1'
    else:
        print('Player 2 is the winner🏆')
        return 'Player 2'

game()
