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

def get_birth_info_and_sentence(url_list):
    candidate_list_full = []
    candidate_birth_town_profession = []

    for url in url_list:

        # Define the URL for German Wikipedia
        # url = "https://de.wikipedia.org/wiki/Melchior_Ndadaye"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for paragraphs that might contain the birth info and the name
            paragraphs = soup.find_all('p')

            birth_info = None
            full_sentence_after_birth = None
            person_name = None

            for paragraph in paragraphs:
                text = paragraph.get_text()

                # Look for the birth info pattern and name before the bracket (e.g., Kate Garry Hudson (* 19. April 1979 in Los Angeles, Kalifornien))
                birth_info_match = re.search(r'([A-Za-zäöüß]+(?: [A-Za-zäöüß]+)*) \(\* (.*?)\)', text)
                if birth_info_match:
                    person_name = birth_info_match.group(1)  # Capture the name before the bracket
                    birth_info = birth_info_match.group(2)  # Capture the birth info in the bracket

                    # Extract the full sentence after the birth info (after the closing parenthesis)
                    remaining_text = text.split(')', 1)[1].strip()
                    if remaining_text:
                        full_sentence_after_birth = remaining_text.split('.')[0].strip()  # Extract full sentence until the first period

                    break  # Stop searching after finding the birth info and the sentence


            # Print the extracted information
            if person_name:
                # print(f"Name: {person_name}")
                candidate_birth_town_profession.append(person_name)
            else:
                # print("Name not found.")
                a = 1
            if birth_info:
                # print(f"Birth Info: {birth_info}")
                candidate_birth_town_profession.append(birth_info)
            else:
                # print("Birth Info not found.")
                a = 0
            if full_sentence_after_birth:
                # print(f"Full Sentence after birth info: {full_sentence_after_birth}")
                candidate_birth_town_profession.append(full_sentence_after_birth)
            else:
                # print("Follow-up sentence not found.")
                a = 2

        else :
            a = 5
            # print(f"Failed to retrieve the page. Status code: {response.status_code}")

        if len(candidate_birth_town_profession) == 3:
            candidate_list_full.append(candidate_birth_town_profession)

        candidate_birth_town_profession = []

    return candidate_list_full

def get_xxxx_amount_wiki_people():


    # ------- DO NOT TOUCH ----------------------------------------
    # Define the URL
    # 1 famous people url
    url = "https://de.wikipedia.org/w/index.php?limit=500&offset=500&profile=default&search=famous+people&title=Spezial:Suche&ns0=1"
    # ------- DO NOT TOUCH ----------------------------------------

    url_list = []
    # Send a GET request to the URL
    response = requests.get(url)

    potential_wiki_cadidate = []
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Look for all search result links
        links = soup.find_all('a', href=True)

        # Loop through each link and check if it contains a valid Wikipedia article
        for link in links:
            href = link['href']

            # Filter out non-article links
            if href.startswith('/wiki/') and not href.startswith('/wiki/Spezial:'):
                # Build the full URL
                full_link = "https://de.wikipedia.org" + href
                title = link.get_text(strip=True)  # Get the link text (title)

                # Print the title and link
                # print(f"Title: {title}, Link: {full_link}")
                url_list.append(full_link)

                # print(f"{title}_______{href[6:]}")
                name_surname = title.split(" ")
                href_name_surname = href[6:].split("_")
                try:
                    if len(name_surname) < 4 and name_surname[0] == href_name_surname[0] and name_surname[1] == \
                            href_name_surname[1]:
                        potential_wiki_cadidate.append(title)
                except IndexError:
                    pass

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    # print(potential_wiki_cadidate)


    return url_list



def main():
    print("VickyCrush_folder_stuff rules:")
    print("\nThe game will randomly pick people from wikipedia.\nIt will test your knowledge about them")
    print("\n1-10 players\n1-10 wiki people - knowledge questions\nHINT: This is a fast game. skip or try !\nThe amount of points in the End will show a winner!")
    input("\nAll good ? ready to go ? hit -ENTER- ")
    print("\n!!! wait a second - data is loading !!!")
    print("\nwiki is very slow.\nwe get and validate up to 1000 entries -\ntakes a minute or 2 -\n")

    # !!!! OPTION LOAD FRESH FROM WIKI !!!!
    # url_list = get_xxxx_amount_wiki_people()
    # candidate_list_full = get_birth_info_and_sentence(url_list)

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
