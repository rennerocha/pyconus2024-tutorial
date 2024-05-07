# Gathering data from the web using Python
## PyCon US 2024 - 16 / 05 / 2024

## About the tutorial

Information is abundant and readily available on the internet. However, the sheer amount of data can be overwhelming and time-consuming to navigate through. That's where web scraping comes in - a powerful tool used to extract data from websites and turn it into a usable format.

In this tutorial, we will explore the basics of web scraping and how to implement it using Scrapy (a Python framework). Whether you are a data analyst, programmer, or researcher, this tutorial will equip you with the fundamental skills needed to create your own web scraper and extract valuable information from websites.

## Before the tutorial

Clone this repository so you will get access to the presentation and also for the code solution of the suggested exercises:
https://github.com/rennerocha/pyconus2024-tutorial

During the tutorial it is expected that you try to solve some small exercises using [Scrapy](https://scrapy.org), a web scraping framework. It will be the only required library to be installed (any other dependencies should be installed together with it).

Follow the [Scrapy installation guide](https://docs.scrapy.org/en/latest/intro/install.html) according your platform and ensure that you are able to run the `scrapy version` in your terminal and see `Scrapy 2.11.1` as result (with no errors).

In Linux platform I suggest the use of a virtual environment. If everything is right, it should be a few commands to have everything up and running:

```
$ git clone https://github.com/rennerocha/pyconus2024-tutorial pyconus2024-tutorial
$ cd pyconus2024-tutorial
$ python -m venv .venv
$ source .venv/bin/activate
$ cd code
$ pip install -r requirements
```