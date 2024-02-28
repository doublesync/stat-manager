import random


def realRange(start: int, end: int) -> range:
    return range(start, end + 1)


jumperList: list = {
    realRange(72, 77): [
        "Default Small",
        "Nickeil Alexander-Walker",
        "Grayson Allen",
        "Cole Anthony",
        "Ryan Arcidiacono",
        "DJ Augustin",
        "LaMelo Ball",
        "Lonzo Ball",
        "Delano Banton",
        "Dick Barnett",
        "Kent Bazemore",
        "Bradley Beal",
        "Jared Butler",
        "Trey Burke",
        "Kobe Bufkin",
        "Jalen Brunson",
        "Bruce Brown",
        "Malcolm Brogdon",
        "Avery Bradley",
        "James Bulknight",
        "Eric Bledsoe",
        "Chauncey Billups",
        "Patrick Beverley",
        "Malik Beasley",
        "Facundo Campazzo",
        "Jevon Carter",
        "Michael Carter-Williams",
        "Alex Caruso",
        "Chris Chiozza",
        "Josh Christopher",
        "Jordan Clarkson",
        "Darren Collison",
        "Mike Conley",
        "Seth Curry",
        "Stephen Curry",
        "Johnny Davis",
        "Malachi Flynn",
        "Derek Fisher",
        "Wayne Ellington",
        "Carsen Edwards",
        "Anthony Edwards",
        "Goran Dragic",
        "Ayo Dosunmu",
        "Luguentz Dort",
        "Luka Doncic",
        "Donte DiVincenzo",
        "Spencer Dinwiddie",
        "Terence Davis",
        "Bryn Forbes",
        "De’Aaron Fox",
        "Steve Francis",
        "Markelle Fultz",
        "Darius Garland",
        "Keyonte George",
        "Brandon Goodwin",
        "Eric Gordon",
        "Devonte’ Gordon",
        "Jalen Green",
        "Quentin Grimes",
        "Kyle Guy",
        "Aaron Holiday",
        "George Hill",
        "Haywood Highsmith",
        "Buddy Hield",
        "Tyler Hero",
        "Scoot Handerson",
        "Killian Hayes",
        "Jordan Hawkins",
        "Gary Harris",
        "James Harden",
        "Penny Hardaway",
        "RJ Hampton",
        "Jrue Holiday",
        "Talen Horton-Tucker",
        "Nah’Shon Hyland",
        "Kyrie Irving",
        "Jaden Ivey",
        "Frank Jackson",
        "Reggie Jackson",
        "Ty Jerome",
        "Isaiah Joe",
        "Keon Johnson",
        "Tre Jones",
        "Tyus Jones",
        "Tre Mann",
        "Terance Mann",
        "Theo Maledon",
        "Kyle Lowry",
        "Damian Lillard",
        "Kira Lewis Jr.",
        "Saben Lee",
        "Damion Lee",
        "Zach LaVine",
        "Jason Kidd",
        "Steve Kerr",
        "Cory Joseph",
        "Wesley Matthews",
        "Tyrese Maxey",
        "Skylar Mays",
        "Miles McBride",
        "CJ McCollum",
        "TJ McConnell",
        "Rodney McGruder",
        "Jordan McLaughlin",
        "Ben McLemore",
        "De’Anthony Melton",
        "Shake Milton",
        "Davion Mitchell",
        "Kendrick Nunn",
        "Frank Ntilikina",
        "Jaylen Nowell",
        "Raul Neto",
        "Andrew Nembhard",
        "Steve Nash",
        "Jamal Murray",
        "Dejounte Murray",
        "Mychal Mulder",
        "Monte Morris",
        "Ja Morant",
        "Malik Monk",
        "Josh Okogie",
        "Victor Oladipo",
        "Tony Parker",
        "Chris Paul",
        "Cameron Payne",
        "Elfrid Payton",
        "Gary Payton II",
        "Brandin Podziemski",
        "Kevin Porter Jr.",
        "Norman Powell",
        "Jason Preston",
        "Joshua Primo",
        "D’Angelo Russell",
        "Ricky Rubio",
        "Terry Rozier III",
        "Derrick Rose",
        "Rajon Rondo",
        "Nate Robinson",
        "Oscar Robertson",
        "Austin Rivers",
        "JJ Redick",
        "Jahmi’us Ramsey",
        "Immanuel Quickley",
        "Payton Pritchard",
        "Marcus Sasser",
        "Tomas Satoransky",
        "Dennis Schroder",
        "Collin Sexton",
        "Landry Shamet",
        "Anfernee Simons",
        "Marcus Smart",
        "Dennis Smith Jr.",
        "Ish Smith",
        "Nick Smith Jr",
        "Jaden Springer",
        "John Stockton",
        "John Wall",
        "Lonnie Walker IV",
        "Kemba Walker",
        "Dwyane Wade",
        "Fred VanVleet",
        "Matt Thomas",
        "Isaiah Thomas",
        "Cameron Thomas",
        "Tyrell Terry",
        "Jae’Sean Tate",
        "Edmond Sumner",
        "Jalen Suggs",
        "Cason Wallace",
        "TyTy Washington Jr.",
        "Quinndary Weatherspoon",
        "Blake Wesley",
        "Jerry West",
        "Russell Westbrook",
        "Coby White",
        "Derrick White",
        "Jason Williams",
        "Louis Williams",
        "Mark Williams",
        "Cassius Winston",
        "Trae Young",
        "Delon Wright",
    ],
    realRange(77, 81): [
        "Default Big",
        "Santi Aldama",
        "Thanasis Antetokounmpo",
        "Oshae Brissett",
        "Devontae Cacok",
        "Marquese Chriss",
        "Ousmane Dieng",
        "Robert Covington",
        "Tyler Cook",
        "Danilo Gallinari",
        "Usman Garuba",
        "Montrezi Harrell",
        "JaMychal Green",
        "Draymond Green",
        "Alize Johnson",
        "James Johnson",
        "Stanley Johnson",
        "Kai Jones",
        "Kevon Looney",
        "Trey Lyles",
        "Kenyon Martin Jr.",
        "Chimezie Metu",
        "Onyeka Okongwu",
        "Zeke Nnaji",
        "Markieff Morris",
        "Marcus Morris Sr.",
        "Eric Paschall",
        "Sam Perkins",
        "Vladimir Radmanovic",
        "Naz Reid",
        "Isaiah Stewart",
        "Jarred Vanderbilt",
        "PJ Tucker",
        "Grant Williams",
        "Zion Williamson",
        "Justise Winslow",
        "Thaddeus Young",
    ],
    realRange(82, 88): [
        "Default Big",
        "Kareem Abdul-Jabbar",
        "Precious Achiuwa",
        "Steven Adams",
        "Bam Adebayo",
        "Santi Aldama",
        "LaMarcus Aldridge",
        "Jarrett Allen",
        "Giannis Antetokounmpo",
        "Thanasis Antetokounmpo",
        "Deandre Ayton",
        "Udoka Azubuike",
        "Tony Bradley",
        "Chris Boucher",
        "Bol Bol",
        "Nemanja Bjelica",
        "Bismack Biyombo",
        "Goga Bitadze",
        "Khem Birch",
        "Davis Bertans",
        "Charles Bassey",
        "Paolo Banchero",
        "Mohamed Bamba",
        "Marvin Bagley III",
        "Elton Brand",
        "Oshae Brissett",
        "Thomas Bryant",
        "Devontae Cacok",
        "Clint Capela",
        "Vernon Carey Jr.",
        "Wendell Carter Jr.",
        "Marquese Chriss",
        "Brandon Clarke",
        "Nicolas Claxton",
        "Noah Clowney",
        "John Collins",
        "Jalen Duren",
        "Tim Duncan",
        "Kevin Duckworth",
        "Andre Drummond",
        "Ousmane Dieng",
        "Gorgui Dieng",
        "Dewayne Dedmon",
        "Anthony Davis",
        "Robert Covington",
        "DeMarcus Cousins",
        "Tyler Cook",
        "Zach Collins",
        "Joel Embiid",
        "Drew Eubanks",
        "Patrick Ewing",
        "Derrick Favors",
        "Bruno Fernando",
        "Daniel Gafford",
        "Danilo Gallinari",
        "Kevin Garnett",
        "Usman Garuba",
        "Marc Gasol",
        "Pau Gasol",
        "Taj Gibson",
        "Chet Holmgren",
        "Richaun Holmes",
        "Willy Hernangomez",
        "Taylor Henddricks",
        "Jaxson Hayes",
        "Udonis Haslem",
        "Isaiah Hartenstein",
        "Montrezi Harrell",
        "Blake Griffin",
        "JaMychal Green",
        "Draymond Green",
        "Rudy Gobert",
        "Al Horford",
        "Dwight Howard",
        "Serge Ibaka",
        "Jonathan Isaac",
        "Isaiah Jackson",
        "Jaren Jackson Jr.",
        "Alize Johnson",
        "James Johnson",
        "Stanley Johnson",
        "Nikola Jokic",
        "Damian Jones",
        "Kai Jones",
        "Dereck Lively II",
        "Rashard Lewis",
        "Alex Len",
        "Bill Laimbeer",
        "Toni Kujoc",
        "Luke Kornet",
        "Nathan Knight",
        "Maxi Kieber",
        "Walker Kessier",
        "Frank Kaminsky III",
        "Nikola Jovic",
        "DeAndre Jordan",
        "Kevon Looney",
        "Brook Lopez",
        "Robin Lopez",
        "Kevin Love",
        "Trey Lyles",
        "Karl Malone",
        "Boban Marjanovic",
        "Lauri Markkanen",
        "Kenyon Martin Jr.",
        "JaVale McGee",
        "Chimezie Metu",
        "Paul Millsap",
        "Kelly Olynyk",
        "Onyeka Okongwu",
        "Lamar Odom",
        "Charles Oakley",
        "Jusuf Nurkic",
        "Dirk Nowitzki",
        "Nerlens Noel",
        "Zeke Nnaji",
        "Mike Muscala",
        "Markieff Morris",
        "Marcus Morris Sr.",
        "Evan Mobley",
        "Shaquille O’Neal",
        "Eric Paschall",
        "Sam Perkins",
        "Mason Plumlee",
        "Jakob Poeltl",
        "Aleksej Pokusevski",
        "Michael Porter Jr.",
        "Bobby Portis Jr.",
        "Kristaps Porzingis",
        "Dwight Powell",
        "Neemias Queta",
        "Vladimir Radmanovic",
        "Dario Saric",
        "Luka Samanic",
        "Domantas Sabonis",
        "Isaiah Roby",
        "Jeremiah Robinson-Earl",
        "David Robinson",
        "Mitchell Robinson",
        "Nick Richards",
        "Naz Reid",
        "Paul Reed",
        "Zach Randolph",
        "Julius Randle",
        "Alperen Sengun",
        "Day’Ron Sharpe",
        "Pascal Siakam",
        "Ben Simmons",
        "Marko Simonovic",
        "Jabari Smith Jr.",
        "Jalen Smith",
        "Isaiah Stewart",
        "Amar’e Stoudemire",
        "Daniel Theis",
        "Tristan Thompson",
        "Xavier Tilman",
        "Chris Webber",
        "PJ Washington",
        "Moritz Wagner",
        "Franz Wagner",
        "Nikola Vucevic",
        "Jarred Vanderbilt",
        "Jonas Velanciunas",
        "Myles Turner",
        "PJ Tucker",
        "Karl-Anthony Towns",
        "Obi Toppin",
        "Isaiah Todd",
        "David West",
        "Grant Williams",
        "Robert Williams",
        "Zion Williamson",
        "Justise Winslow",
        "James Wiseman",
        "Christian Wood",
        "Thaddeus Young",
        "Omer Yurtseven",
        "Ivica Zubac",
    ],
}


def rollJumper(height: int) -> list:
    # Find the jumperList to pull from
    for heightRange, jumpers in jumperList.items():
        if height in heightRange:
            jumperRoll: str = random.choice(jumpers)
            return jumperRoll
