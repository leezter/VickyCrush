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


def get_all_answers_keywords(candidate_list_full):
    """
    The function creates a KEYWORD_List for the Answers
    :param summary
    :return:
    answer_3_keywords
    """
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

        person_count += 1
        if person_count == 250:
            break

        print(f"\n--> {person_count}. {person} <--")



        # QUESTION 1
        print(f"QUESTION 1:\n(correct YEAR: 100 points / correct CENTURY:  50 points)\nWhen was {person} born?\nAnswer (keywords): {birth_date}")

        # # QUESTION 2
        print(f"\nQUESTION 2:\n(correct TOWN: 100 points / correct COUNTRY:  50 points)\nWhat was {person} birth Town?\nAnswer (keywords): {birth_town}")

        # # QUESTION 3
        splitted_profession_info = profession_info.split(" ")
        professions = []
        for word in splitted_profession_info:
            if len(word) > 4:
                professions.append(word)

        print(f"\nQUESTION 3:\n(2 correct KEYWORDS: 100 points / 1 correct KEYWORD:  50 points)\nWhat was {person} known for ?\nAnswer (keywords): {professions}")




def main():
    print("VickyCrush_folder_stuff rules:")
    print("\nThe game will randomly pick people from wikipedia.\nIt will test your knowledge about them")
    print("\n1-10 players\n1-10 wiki people - knowledge questions\nHINT: This is a fast game. skip or try !\nThe amount of points in the End will show a winner!")
    input("\nAll good ? ready to go ? hit -ENTER- ")
    print("\n!!! wait a second - data is loading !!!")
    print("\nwiki is very slow.\nwe get and validate up to 1000 entries -\ntakes a minute or 2 -\n")


    # !!!! OPTION LOAD FRESH FROM WIKI !!!!
    # url_list = VickyCrush_storage_functions.get_xxxx_amount_wiki_people()
    # candidate_list_full = VickyCrush_storage_functions.get_birth_info_and_sentence(url_list)

    # candidate_list_full = VickyCrush_storage.candidate_list_full
    # get_all_answers_keywords(candidate_list_full)
    # print(candidate_list_full)

    # !!!! OPTION LOAD from LOCAL FILE !!!!
    all_wiki_people = [VickyCrush_storage.famous_people, VickyCrush_storage.actors, VickyCrush_storage.scientists, VickyCrush_storage.sports_people, VickyCrush_storage.celebrities, VickyCrush_storage.nobel_price_winners, VickyCrush_storage.musicians, VickyCrush_storage.famous_people_1, VickyCrush_storage.famous_people_2]

    entries_number = 0
    for wiki_list in all_wiki_people:
        entries_number += len(wiki_list)
        candidate_list_full = wiki_list
        get_all_answers_keywords(candidate_list_full)
        # print(candidate_list_full)

    print (f"\nWe now have {entries_number} entries")



if __name__ == "__main__":
    main()
