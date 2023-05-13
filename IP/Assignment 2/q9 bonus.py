# abhishek benwial 022 libgen
# sargun singh khurana 450 apod

import libgen_api
import requests
import webbrowser


def search_author(author: str) -> None:
    searcher = libgen_api.LibgenSearch()
    response = searcher.search_author(author)
    print("\n", response[0]["Author"], "has", len(response), "entries:", "\n")
    for i in response:
        print("Title:", i["Title"])
        print("Year:", i["Year"])
        print("Language:", i["Language"])
        print("Size:", i["Size"])
        print("Extension: ", i["Extension"])
        print("links:")
        print(i['Mirror_1'])
        print(i['Mirror_2'])
        print(i['Mirror_3'], "\n")

# print(dir(requests))
# print(dir(webbrowser))

def apod(date: str) -> None:
    key = "g4c8plkrB64PkDo9EJjoYBl8aInvxCxdtwwbj5zT" #API key to use nasa's apod api
    url = "https://api.nasa.gov/planetary/apod" # URL of the API 
    params = {"api_key": key, "hd": "True", "date": date} #dict containing API key, whether to retrieve the hd version of img, and the date for which APOD is needed.
    response = requests.get(url, params=params)# send a GET request to the API with parameters
    response_json = response.json() #to parse the API response and store it as a dict 
    print("the following is the astronomical picture of the day:")
    print("date:", response_json["date"])
    print("title:", response_json["title"])
    print("explanation:", response_json["explanation"])
    print("media_type:", response_json["media_type"])
    print("url:", response_json["url"], "\n")
    webbrowser.open(response_json["url"])


print("type 0 to search a author and all their books with download links of libgen")
print("type 1 to search APOD by NASA with link")
con = int(input("type the input: ").strip())

if not con:
    search_author(input("type the name of the author: ").title())
else:
    apod(input("\ntype the date(yyyy-mm-dd): ").strip())


# Astronomy Picture of the Day (APOD) from NASA's API using the requests library. It then takes  
# JSON response, prints  date, title, explanation, media type, and URL of APOD, and opens the URL in 
# web browser using the webbrowser library.
