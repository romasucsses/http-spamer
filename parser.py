import requests
from bs4 import BeautifulSoup

for page_number in range(0, 416):
    url_data = f"https://www.wireclub.com/search?LocationId=&type=0&Gender=1&AgeMin=19&AgeMax=120&LocalSearch=false" \
               f"&Page={page_number}"

    response = requests.get(url_data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        div_srch_results = soup.find("div", id="SearchResults")
        div_list = div_srch_results.find("div", class_="entity-list")
        list_people = div_srch_results.find_all("div", attrs={"data-url": True})
        for each_people in list_people:
            data = each_people.get("data-url")
            file_data = data.replace("/users/", "")
            print(file_data)
            with open('users_urls.txt', 'a') as file:
                file.write(file_data + '\n')

