import random

print("Geography teacher")
print("Guess the capital of the country asked, if you are correct you earn 10 points, if you give the incorrect answer you lose 5 points. You start with 0 points, you lose if you reach -50 and you win when you reach 50 points. Choose wisely, you can have negative points! Have fun!")
# points counter

points = 0

#dictionaries
countries_capitals_europe = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Austria": "Vienna",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Ukraine": "Kiev",
    "United Kingdom": "London",
    "Vatican City": "Vatican City"
}

countries_capitals_americas = {
    "Antigua and Barbuda": "St. John's",
    "Argentina": "Buenos Aires",
    "Bahamas": "Nassau",
    "Barbados": "Bridgetown",
    "Belize": "Belmopan",
    "Bolivia": "La Paz",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Costa Rica": "San José",
    "Cuba": "Havana",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "Ecuador": "Quito",
    "El Salvador": "San Salvador",
    "Grenada": "St. George's",
    "Guatemala": "Guatemala City",
    "Guyana": "Georgetown",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Jamaica": "Kingston",
    "Mexico": "Mexico City",
    "Nicaragua": "Managua",
    "Panama": "Panama City",
    "Paraguay": "Asunción",
    "Peru": "Lima",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Suriname": "Paramaribo",
    "Trinidad and Tobago": "Port of Spain",
    "United States": "Washington D.C.",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}

countries_capitals_asia = {
    "Afghanistan": "Kabul",
    "Armenia": "Yerevan",
    "Azerbaijan": "Baku",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Bhutan": "Thimphu",
    "Brunei": "Bandar Seri Begawan",
    "Cambodia": "Phnom Penh",
    "China": "Beijing",
    "Cyprus": "Nicosia",
    "Georgia": "Tbilisi",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Israel": "Jerusalem",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Nur-Sultan",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Lebanon": "Beirut",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Malé",
    "Mongolia": "Ulaanbaatar",
    "Myanmar (Burma)": "Naypyidaw",
    "Nepal": "Kathmandu",
    "North Korea": "Pyongyang",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palestine": "Ramallah",
    "Philippines": "Manila",
    "Qatar": "Doha",
    "Russia": "Moscow",
    "Saudi Arabia": "Riyadh",
    "Singapore": "Singapore",
    "South Korea": "Seoul",
    "Sri Lanka": "Colombo",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Thailand": "Bangkok",
    "Timor-Leste (East Timor)": "Dili",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "United Arab Emirates": "Abu Dhabi",
    "Uzbekistan": "Tashkent",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a"
}

countries_capitals_oceania = countries_capitals = {
    "Australia": "Canberra",
    "Fiji": "Suva",
    "Kiribati": "South Tarawa",
    "Marshall Islands": "Majuro",
    "Micronesia": "Palikir",
    "Nauru": "Yaren District",
    "New Zealand": "Wellington",
    "Palau": "Ngerulmud",
    "Papua New Guinea": "Port Moresby",
    "Samoa": "Apia",
    "Solomon Islands": "Honiara",
    "Tonga": "Nuku'alofa",
    "Tuvalu": "Funafuti",
    "Vanuatu": "Port Vila"
}

countries_capitals_africa = {
    "Algeria": "Algiers",
    "Angola": "Luanda",
    "Benin": "Porto-Novo",
    "Botswana": "Gaborone",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Bujumbura",
    "Cabo Verde": "Praia",
    "Cameroon": "Yaoundé",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Comoros": "Moroni",
    "Democratic Republic of Congo": "Kinshasa",
    "Republic of Congo": "Brazzaville",
    "Djibouti": "Djibouti",
    "Egypt": "Cairo",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Ghana": "Accra",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Ivory Coast": "Yamoussoukro",
    "Kenya": "Nairobi",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Mali": "Bamako",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Namibia": "Windhoek",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "Rwanda": "Kigali",
    "São Tomé and Príncipe": "São Tomé",
    "Senegal": "Dakar",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria (executive) and Cape Town (legislative) and Bloemfontein (judicial)",
    "South Sudan": "Juba",
    "Sudan": "Khartoum",
    "Tanzania": "Dodoma",
    "Togo": "Lomé",
    "Tunisia": "Tunis",
    "Uganda": "Kampala",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"
}
# selecting continent

continent = input("Select Europe, Americas, Asia, Oceania or Africa: ")

if continent == "Europe" or continent == "europe":
    countries_capitals = countries_capitals_europe

elif continent == "Americas" or continent == "americas":
    countries_capitals = countries_capitals_americas

elif continent == "Oceania" or continent == "oceania":
    countries_capitals = countries_capitals_oceania

elif continent == "Asia" or continent == "asia": 
    countries_capitals = countries_capitals_asia

elif continent == "Africa" or continent == "africa":
    countries_capitals = countries_capitals_africa

# main loop
while points < 50: 
    random_country = random.choice(list(countries_capitals.keys())) # random country selection
    user_input = input("What is the capital of " + random_country + "? ") # user input
    
    if user_input == countries_capitals[random_country]: # if user input is correct
        points += 10
        print("Correct! You won 10 points! Your score now is: {}".format(points))
        
    else: # if user input is incorrect
      points -= 5
      print("Incorrect! The correct answer was: {}".format(countries_capitals[random_country]) + ". You lose 5 points! Your score now is: {}".format(points))

    if points >= 50:
        print("Congratulations! You have won the game!")
        break
    if points < -50:
        print("You lose the game!")
        break


# ask for users name and assign points to each one and ask to each one
# handle south africa
# handle invalid continent
# create dificulty levels
# create a gui - tkinter
# add "learn more about" option
# handle repetitions
# handle invalid inputs
