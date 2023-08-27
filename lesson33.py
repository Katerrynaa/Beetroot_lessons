# task 1
#1.1
import requests 
def download(url, path):
    url = "https://www.wikipedia.org/"
    r = requests.get(url, allow_redirects=True)
    open('robots.txt', 'wb').write(r.content)
    print(f'robots.txt downloaded to {path}')

wikipedia_url = "https://www.wikipedia.org/"
path = "wikipedia_robots.txt"
download(wikipedia_url, path)

twitter_url = "https://twitter.com/"
path2 = "twitter.robots.txt"
download(twitter_url, path2)

#1.2
url = "https://www.wikipedia.org/"
r = requests.get(url, allow_redirects=True)
open("robots.txt", 'wb').write(r.content)

url = "https://twitter.com/"
r1 = requests.get(url, allow_redirects=True)
open("robots1.txt", "wb").write(r1.content)

print('wikipedia file downloaded and saved to file')
print('twitter file downloaded and saved to file')

# task 3
import requests
api_key = "https://www.weatherapi.com/"
city = input("Enter your name city: ")
url = f"https://www.weatherapi.com/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.text
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Temperature: {temp}")
    print(f"Description: {desc}")
