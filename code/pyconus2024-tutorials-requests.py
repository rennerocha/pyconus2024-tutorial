import requests
from parsel import Selector

response = requests.get("https://us.pycon.org/2024/schedule/tutorials/")

sel = Selector(text=response.text)
for tutorial in sel.css(".calendar a::text").getall():
    print(tutorial)
