import requests
from parsel import Selector

response = requests.get('https://us.pycon.org/2024/schedule/tutorials/')

sel = Selector(text=response.body)
for tutorial in sel.css('.calendar a::text').getall():
    print(tutorial)