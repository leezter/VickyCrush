
import re #find_birth_year
import random #random pick of famous people for the player

def get_random_person(data):
    """ Pick a person at random from a list of celebrities """
    data = candidate_list_full
    random_person = random.choice(data)
    return random_person

def find_birth_year(text):
    """ finds the birth year in the birth_info string in results. """
    match = re.search(r'\b\d{4}\b', text) # Use regex to find 4-digit integers in the string
    if match:
        birth_year = int(match.group())
        return birth_year
    else:
        print('No integer found in wikipedia. Skipping that Question!!')
        return False
        

def get_answer_1(points, random_person):
    """ gets the answer for birth date from the user and compares with random_person
        returns the points gained in Q1. The closer the guess, the more points """

    print(f"Current Points: {points}\n")
    # Find birth year in random_person:
    name = random_person[0]
    birth_info = random_person[1]
    birth_year_result = find_birth_year(birth_info)

    # get user input, compare and give points:
    birth_year_answer = int(input(f"\nQUESTION 1: What year was {name} born?\n"))
    if birth_year_answer == birth_year_result: #correct answer
        print(f"{birth_year_result} is correct! You get 20 points!\n")
        points += 30
    elif birth_year_answer in range(birth_year_result - 10, birth_year_result + 10): # range 10 years
        print(f"{birth_year_answer} is in 10 year range! You get 15 points! Correct Answer: {birth_year_result}")
        points += 15
    elif birth_year_answer in range(birth_year_result - 50, birth_year_result + 50): # 50 year range
        print(f"{birth_year_answer} is in 50 year range! You get 10 points! Correct Answer: {birth_year_result}")
        points += 10
    elif birth_year_answer in range(birth_year_result - 100, birth_year_result + 100): # 100 year range
        print(f"{birth_year_answer} is in 100 year range! You get 5 points! Correct Answer: {birth_year_result}")
        points += 5
    else:
        print(f"{birth_year_answer} is more than 100 years apart! Correct Answer: {birth_year_result}. You get 0 points!")

    return points


def get_answer_2(points, random_person, countries, us_states):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""

    print(f"Current Points: {points}")
    # Find birth location in random_person:
    name = random_person[0]
    birth_info = random_person[1]
    location_data = birth_info.split(",")[-1].strip().lower()
    country = None
    state = None

    # Extract country/state from location_data
    for word in location_data.split():
        if word in countries:
            country = word
        elif word in us_states:
            country = "usa"
            state = word

    if not country:
        print(f"Could not find a valid country/state in the data: {location_data}")
        print("Skipping this question!")
        return points

    # Ask user for country input and check:
    location_answer = input(f"\nQUESTION 2: Where was {name} born? ").strip().lower()
    if location_answer == country or (state and location_answer == state):
        print(f"Correct! {name} was born in {location_answer}. You get 10 points!")
        points += 10
    else:
        print(f"False! {name} was born in {state if state else country}.")

    # Optional Guess if a city was extracted:
    birth_city = random_person[1].split(",")[0].split()[-1]
    if len(birth_city) > 4:
        guess_city = input(f"Get 10 Bonus Points if you know the City {name} was born.\nGuess the city: ")

        if guess_city.lower() == birth_city.lower():
            points += 10
            print(f"Great Job, {birth_city} is correct!")
        else:
            print(f"False, {name} was born in {birth_city}.")

    return points


def get_answer_3(points, random_person, profession_keywords):
    """Gets the answer for birth location from user and compares with random_person.
       Returns updated points for Question 2."""
    print(f"Current Points: {points}")
    name = random_person[0]
    profession_info = random_person[2].split()

    # find professions of the random person
    professions = [word for word in profession_info if word in profession_keywords]

    # make a guess:
    profession_guess = input(f"\nWhat is the profession of {name}, why are they famous? (Seperate with ',')\n")
    guesses = [guess.strip().lower() for guess in profession_guess.split(',')]

    for guess in guesses:
        if guess in professions:
            print(f"Correct! {guess.upper()} is a profession of {name}! You get 10 Points!")
            points += 10
        else:
            print(f"{guess} is no profession. Sorry!")

    return points


def main():

    us_states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
        "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
        "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
        "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
        "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
        "new mexico", "new york", "north carolina", "north dakota", "ohio",
        "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
        "south dakota", "tennessee", "texas", "utah", "vermont", "virginia",
        "washington", "west virginia", "wisconsin", "wyoming"
    ]
    countries = [
        "united states", "usa", "us", "united kingdom", "uk", "china", "india", "germany", "france",
        "japan", "russia", "italy", "canada", "australia", "brazil", "south korea",
        "spain", "mexico", "south africa", "netherlands", "switzerland", "turkey",
        "sweden", "saudi arabia", "argentina", "egypt", "indonesia", "norway",
        "new zealand", "greece", "israel", "thailand", "ireland", "poland",
        "portugal", "vietnam", "belgium", "denmark", "pakistan", "malaysia",
        "philippines", "singapore", "austria", "czech republic", "chile",
        "hungary", "finland", "colombia", "ukraine", "united arab emirates",
        "iran", "bangladesh", "nigeria", "morocco", "peru", "venezuela", "ecuador",
        "bolivia", "paraguay", "uruguay", "sri lanka", "nepal", "bhutan", "maldives",
        "afghanistan", "mongolia", "kazakhstan", "uzbekistan", "turkmenistan",
        "kyrgyzstan", "tajikistan", "myanmar", "laos", "cambodia", "brunei",
        "east timor", "jamaica", "haiti", "cuba", "dominican republic", "trinidad and tobago",
        "barbados", "bahamas", "fiji", "papua new guinea", "solomon islands",
        "vanuatu", "samoa", "tonga", "kiribati", "micronesia", "marshall islands",
        "palau", "seychelles", "mauritius", "madagascar", "angola", "zimbabwe",
        "zambia", "botswana", "namibia", "mozambique", "malawi", "tanzania",
        "uganda", "rwanda", "burundi", "congo", "democratic republic of the congo",
        "ghana", "ivory coast", "senegal", "mali", "guinea", "benin", "togo",
        "sierra leone", "liberia", "gambia", "cameroon", "chad", "niger",
        "central african republic", "somalia", "eritrea", "djibouti", "sudan",
        "south sudan", "ethiopia", "algeria", "tunisia", "libya", "cape verde",
        "comoros", "lesotho", "eswatini", "equatorial guinea", "gabon",
        "são tomé and príncipe", "armenia", "azerbaijan", "georgia", "albania",
        "north macedonia", "kosovo", "bosnia and herzegovina", "montenegro",
        "serbia", "croatia", "slovenia", "slovakia", "belarus", "latvia",
        "lithuania", "estonia", "iceland", "luxembourg", "monaco", "san marino",
        "andorra", "liechtenstein", "vatican city"
    ]

    profession_keywords = [
        "scientist", "sports", "soccer", "football", "celebrities people", "nobel prize winners people",
        "musicians", "actors", "actor", "president", "schauspielerin", "schauspieler",
        "philosopher", "author", "poet", "director", "producer", "comedian", "model", "entrepreneur",
        "inventor", "business magnate", "architect", "teacher", "journalist", "chef", "dancer", "photographer",
        "author", "humanitarian", "activist", "royalty", "politician", "economist", "historian",
        "psychologist", "lawyer", "doctor", "nurse", "engineer", "mathematician", "architect",
        "filmmaker", "painter", "sculptor", "designer", "fashion designer", "billionaire",
        "philanthropist", "environmentalist", "astronaut", "astronomer", "biologist", "geologist",
        "ecologist", "mathematician", "cartographer", "scientific researcher", "cryptographer",
        "linguist", "sociologist", "theologian", "neurologist", "oncologist", "orthopedic surgeon",
        "choreographer", "voice actor", "veterinarian", "pilot", "fisherman", "taxidermist", "beekeeper",
        "librarian", "social worker", "public relations specialist", "IT specialist", "web developer",
        "data scientist", "cryptocurrency expert", "youtuber", "streamer", "vlogger", "blogger", "podcaster",
        "fitness trainer", "lifeguard", "paralegal", "geographer", "pharmacist", "toxicologist",
        "nutritionist", "dietitian", "emergency medical technician", "firefighter", "paramedic",
        "police officer", "detective", "soldier", "military leader", "navy officer", "air force officer",
        "judge", "mayor", "senator", "governor", "ambassador", "diplomat", "environmental scientist",
        "climate scientist",
    ]


    #Game Start: Print Welcome Text, Rules, etc...
    # get_random_person():
    random_person = get_random_person(candidate_list_full)

    print(f"\nWelcome to VickyCrush! Your Random Person is: {random_person[0].upper()}")


    points = 0

    #Q1: Birth Date
    points = get_answer_1(points, random_person)

    #Q2: Birth Location
    points = get_answer_2(points, random_person, countries, us_states)

    #Q3: Profession/Fame
    points = get_answer_3(points, random_person, profession_keywords)
    print(f"Your Total Score is: {points}\n")


if __name__ =="__main__":
    main()

'''
Scoring System:

Q1: birth year
-> 20 points if correct
-> 10 points if in 50 year range
-> 5 points if in 100 year range

Q2: birth location:
-> 10 points if correct country
-> 10 Bonus points for a city (only if city is found)

Q3: profession
-> 10 points for each matching profession

'''
