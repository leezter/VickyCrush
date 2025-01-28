
import requests
from bs4 import BeautifulSoup
import wikipedia
import warnings
import re
warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")
import VickyCrush_storage



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

