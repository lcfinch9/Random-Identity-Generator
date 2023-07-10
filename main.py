#### ---- SETUP ---- ####

## -- Library -- ##

import random

## -- Constants -- ##

FIRST_NAMES = ["Gabriella", "Martin", "Lara", "Ewan", "Lydia", "Alexandra", "Reuben", "Velma", "Bradley", "Katie", "Zak", "Hazel", "Summer", "Leo", "Ben", "Maisie", "Katherine", "Charlotte", "Alisha", "George", "Tommy", "Theodore", "Josephine", "Eve", "Isabel", "Issa", "Mark", "Carl", "Dominic", "Stephanie", "Jennifer", "Joel", "Stephen", "Danny", "Christina", "Lois", "Vincent", "Alfred", "Anthony", "Margie", "Oscar", "Samantha", "Olivia", "Eric", "Victoria", "Kiki", "Jackson", "Daisy", "Beatrice", "Curtis", "Grover", "Scarlett", "Owen", "Louise", "Clara", "Harvey", "Robin", "Jason", "Jimmy", "Isla", "Esme", "Maria", "Nathaniel", "Natasha", "Declan", "Garfield", "Brandon", "Sean", "Sonny", "Margaret", "Andrew", "Muhammed", "Scott", "Warren", "Leah", "Lilly", "Lewis", "Nicholas", "Elise", "Charlie", "Peter", "Sara", "Archie", "Michelle", "Ellen", "Grace", "Taylor", "Steven", "Sebastian", "Kyle", "Timothy", "Jonathan", "Tiffany", "Danielle", "Mollie", "Sofia", "Zoe", "Melissa", "Marcus", "Naomi"]
LAST_NAMES = ["Hodges", "Hopkins", "Jimenez", "Hammond", "Lee", "Warren", "Pena", "Schroeder", "Daniel", "Wagner", "Spencer", "Tran", "Lambert", "Clayton", "Perry", "Ortega", "Frazier", "Woods", "Hale", "Flores", "Holland", "McGregor", "Cannon", "James", "Burns", "Pearson", "Wade", "Stewart", "Thomas", "Cox", "Shelton", "Schmidt", "Sandoval", "Walton", "Dunne", "Figueroa", "Schofield", "Smith", "Chan", "Smart", "Lawson", "Russell", "Bates", "Gray", "Santos", "Jackson", "Alexander", "Davis", "Miranda", "Stevens", "Marsh", "French", "Knowles", "Curry", "Richards", "Reyes", "Foster", "Brennan", "Rodgers", "Joyce", "Brooks", "McDonald", "Todd", "Steele", "Barker", "Rossi", "Garcia", "McGee", "Craig", "Parker", "Holt", "Houghton", "O\'Brien", "Ramsey", "Powell", "Roderick", "Kelly", "Doherty", "Barnett", "Townsend", "Solis", "Hayes", "Rivas", "Ross", "Chambers", "Griffin", "Baldwin", "Hughes", "Fernandez", "Terry", "Gibson", "Ortiz", "Swanson", "White", "Adams", "Hawkins"]
AREA_CODES = {"New York, NY": 212, "Los Angeles, CA": 213, "Chicago, IL": 773, "Houston, TX": 281, "Phoenix, AZ": 602, "Philadelphia, PA": 267, "San Antonio, TX": 210, "San Diego, CA": 619, "Dallas, TX": 214, "San Jose, CA": 408, "Austin, TX": 512, "Jacksonville, FL": 904, "Fort Worth, TX": 817, "San Francisco, CA": 415, "Columbus, OH": 614, "Charlotte, NC": 704, "Indianapolis, IN": 463, "Seattle, WA": 206, "Denver, CO": 720, "Washington, DC": 202, "Boston, MA": 617, "El Paso, TX": 915, "Detroit, MI": 313, "Nashville, TN": 615, "Portland, OR": 503}

#### ---- GENERATE NAME ---- ####

def generate_name(names=FIRST_NAMES):
    return random.choice(names)

#### ---- GENERATE LOCATION ---- ####

def generate_location():
    random_loc = random.choice(list(AREA_CODES.keys()))
    return random_loc

#### ---- GENERATE PHONE ---- ####

def generate_phone(location):
    area_code = str(AREA_CODES[location])
    middle = str(random.randint(100, 999))
    last = str(random.randint(1000, 9999))
    return area_code + "-" + middle + "-" + last

#### ---- GENERATE IDENTITY ---- ####

def generate_identity(first=None, middle=None, last=None, location=None, min_age=10, max_age=100):

    ## -- Name -- ##

    if first == None:
        fname = generate_name()
    else:
        fname = first
    if middle == None:
        mname = generate_name()
    else:
        mname = middle
    if last == None:
        lname = generate_name(LAST_NAMES)
    else:
        lname = last

    ## -- Details -- ##

    if location == None:
        location = generate_location()
    phone = generate_phone(location)
    age = random.randint(min_age, max_age)

    ## -- Display -- ##

    print(fname + " " + mname + " " + lname + ", " + str(age))
    print("========================")
    print(phone)
    print(location + "\n")

#### ---- OUTPUT ---- ####

## -- Fully random -- ##

generate_identity()

## -- Child -- ##

generate_identity(min_age=1, max_age=12)

## -- Hyphenated last name -- ##

lname = random.choice(LAST_NAMES) + "-" + random.choice(LAST_NAMES)
generate_identity(last=lname)

## -- New location -- ##

generate_identity(location="Dallas, TX")
