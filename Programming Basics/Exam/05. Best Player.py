best_player_name = ""
best_player_goals = 0
hat_tricks = False

while True:
   name_player = input()

   if name_player == "END":
       break

   current_number_of_goals = int(input())

   if current_number_of_goals > best_player_goals:
        best_player_goals = current_number_of_goals
        best_player_name = name_player

        if current_number_of_goals >= 3:
            hat_tricks = True

            if current_number_of_goals >= 10:
                break

print(f"{best_player_name} is the best player!")

if hat_tricks:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
