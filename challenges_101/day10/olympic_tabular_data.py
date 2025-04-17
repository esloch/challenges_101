#Olympics Host Cities - www.101computing.net/olympics-host-cities-csv-challenge
"""
 List all the Winter Olympic Games
 List all the Olympic Games that were hosted in the United States
 Find out how many times did London (UK) host the Olympic Games
 Let the user enter a year and find out which city hosted the Olympic Games on the year they entered.
"""
from typing import Optional

def summerOlympics(
    _season: Optional[str] = None,
    _country: Optional[str] = None, 
    _city: Optional[str] = None, 
    _year: Optional[str] = None
    ):

    file = open("/opt/services/challenges_101/challenges_101/day10/data/olympics.csv","r")

    country_hosted = 0
    olympic_winter = []
    olympic_USA = []
    olympic_year = []    

    for line in file:
        data = line.split(",")
        year = data[0]
        city = data[1]
        country = data[2]
        season = data[3]

        if not _season and not _country and not _city and not _year:
            print(season + " - " + year + " - " + city + " - " + country)

        if season==_season:
            olympic_winter.append((season, year, city, country))

        if country==_country:
            olympic_USA.append((season, year, city, country))

        if city==_city:
            country_hosted += 1

        for y in _year:
            if year==y:
                olympic_year.append((season, year, city, country))

    if any (olympic_winter):
        print("List of host cities of Winter Olympics")
        for country in olympic_winter:
            print(country)
        print(50 * "-")

    if any (olympic_USA):
        print("List of host cities of Olympics in USA")
        for country in olympic_USA:
            print(country)
        print(50 * "-")

    if _city=="London":
        print("Number of times " + _city + " hosted Summer Olympics: " + str(country_hosted))
        print(50 * "-")

    if any (olympic_year):
        print(f"List of host cities of Olympics in " + "{}".format(_year))
        for y in olympic_year:
            print(y)
        print(50 * "-")
            
    file.close()
# summerOlympics()
# summerOlympics(_season="Winter")
# summerOlympics(_country="United Kingdom")
# summerOlympics(_city="London")
summerOlympics(_year=["1904","1908","1900"])
