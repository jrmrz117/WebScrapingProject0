class Scrape:
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    # website that will be scraped
    page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")

    # creates a structured object from which you can extract any HTML element
    soup = BeautifulSoup(page, "html.parser")
    # heading = soup.h1
    print(soup.h1)
    # This line creates a Python list that contains all the <td> elements that have the class city
    city_list = soup.find_all("td", class_="city")
    # This will get just the text (no HTML) in the list of cities from the tag object
    for city in city_list:
        print(city.get_text())
    # How to find all vs find one
    # This helps when finding an address or phone number(s)
    phone_number = soup.find(id="call")
    print(phone_number.get_text())



