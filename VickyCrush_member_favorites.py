from colorama import Fore, Back, Style, init
# Initialize colorama
init()
# # Print colored text
# print(Fore.RED + "This is red text.")
# print(Fore.GREEN + "This is green text.")
# print(Back.YELLOW + "This text has a yellow background.")
# print(Style.BRIGHT + "This is bright text.")
# print(Style.RESET_ALL + "This resets all styles.")
print(Fore.BLACK + Back.YELLOW + Style.BRIGHT)
# ----- above for colors --------------------

import requests
from bs4 import BeautifulSoup
import wikipedia
import warnings
import re
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")
import VickyCrush_storage
import VickyCrush_storage_functions


"""

do we want to create our FAVORITE list ???

there is a little script , to generate OUR FAMOUS people LIST.

it prints a name .

we then hit "y" or "n" in order to add the ENTRY to our list 

there is 1200 entries.

we are 5 people.

that's 250 entries per person to create a list of people we KNOW !!
its 500 clicks per team member to click 1x y and 1 x ENTER

should be maximum 10 - 15 mins for each

we then have a nice LIST to consider , may be as an easy LIST :) 

Shall I do it ?? 

"""


# !!!! OPTION LOAD from LOCAL FILE !!!!
all_wiki_people = [VickyCrush_storage.famous_people, VickyCrush_storage.actors, VickyCrush_storage.scientists, VickyCrush_storage.sports_people, VickyCrush_storage.celebrities, VickyCrush_storage.nobel_price_winners, VickyCrush_storage.musicians, VickyCrush_storage.famous_people_1, VickyCrush_storage.famous_people_2]

entries_number = 0
for wiki_list in all_wiki_people:
    entries_number += len(wiki_list)
    candidate_list_full = wiki_list
    # get_all_Favorits(candidate_list_full)
    # print(candidate_list_full)

print (f"\nWe now have {entries_number} entries")


member_favorite_list = []
person_count = 0
for x in range(len(candidate_list_full)):
    person = candidate_list_full[x][0]
    birth_data = candidate_list_full[x][1].split("in ")

    birth_date = birth_data[0]
    try:
        birth_town = birth_data[1]
    except IndexError:
        birth_town = "t.b.a"

    profession_info = candidate_list_full[x][2]

    # person_count += 1
    # if person_count == 250:
    #     break

    print(f"\n--> {person_count}. {person} <--")





    # # QUESTION 3
    splitted_profession_info = profession_info.split(" ")
    professions = []
    for word in splitted_profession_info:
        if len(word) > 4:
            professions.append(word)

    # QUESTION 1
    print(f"born {birth_date} - town {birth_town}")
    print(f"profession (keywords): {professions}\n")

    user_input = input("add to favorites ? y/n ")

    if user_input == "y":
        member_favorite_list.append(candidate_list_full[x])

    print(member_favorite_list)







