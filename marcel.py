head_line = f"\t\t\t{'*' * 10} WELCOME TO THE VICKY CRUSHES GAME {'*' * 10}"
    length_head_line = len(head_line)
    print(f"\t\t\t{'*' * length_head_line}\n{head_line}\n\t\t\t{'*' * length_head_line}")
    user_input = input("\t\t\t   Pass your name and hit Enter to enter the game mode ").upper()
    cowsay.ghostbusters(f"HELLO {user_input}\nPlease read\ninstructions\ncarefully!!!")
    print()
    print_note_ghost = ("\n\t\t\t\t\tThe game will randomly pick a celebrity."
                  "\n\t\t\t  You have to answer 3 questions about the celebrity."
                  "\n\t\tYou get points for each right answer which will show at the end."
                  "\n\t\t  Each question has sa lightly different pointing system."
                )
    print(print_note_ghost)
    input(f"\n\t\t\t\t\tPress Enter if you are good to go")
    cowsay.kitty(f"{user_input}\nget ready\nto answer the\nfirst question")
    print_note_cat_1 = ("\n\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH YEAR"
                  "\n\t\t\t  If you get the correct year you get 20 points."
                  "\n\t\tIf you guess within a range of 25 years + /- you get 10 points."
                  "\n\t\tIf you guess within a range of 50 years + / - you get 5 points."
                  )
    print(print_note_cat_1)
    input("\n\t\t\t\t\tPress Enter for the next question")
    cowsay.kitty(f"{user_input}\nget ready\nto answer the\nsecond question")
    print_note_cat_2 = ("\n\t\t\t\t\tGUESS THE CELEBRETY'S BIRTH PLACE"
                      "\n\t\t\t  If you get the correct city you get 20 points."
                      "\n\t\t\tIf you guess correct country you get 10 points."
                      )
    print(print_note_cat_2)
    input("\n\t\t\t\t\tPress Enter for the next question")
    cowsay.kitty(f"{user_input}\nget ready\nto answer the\nthird question")
    print_note_cat_3 = ("\n\t\t\t\t\tGUESS THE CELEBRETY'S OCCUPATION"
                      "\n\t\t\t  If you get the correct occupation you get 20 points."
                      )
    print(print_note_cat_3)
    input("\n\t\t\t\t\tPress Enter to see the final score")
