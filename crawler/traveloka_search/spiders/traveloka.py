import scrapy
import requests
import json
from ..sele_crawler import open_selenium

headers = {
    'authority': 'www.traveloka.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.traveloka.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-domain': 'flight',
    'x-route-prefix': 'en-vn'
}

body = {
    "fields": [],
    "clientInterface": "desktop",
    "data": {
        "currency": "VND",
        "isReschedule": False,
        "locale": "en_VN",
        "numSeats": {
            "numAdults": 2,
            "numChildren": 0,
            "numInfants": 0
        },
        "seatPublishedClass": "ECONOMY",
        "destinationAirportOrArea": "SINA",
        "flexibleTicket": False,
        "flightDate": {
            "year": 2023,
            "month": 2,
            "day": 12
        },
        "sourceAirportOrArea": "XKLA",
        "newResult": True,
        "seqNo": None,
        "searchId": "f72d8c23-7dca-4853-963a-7cc232f1cde2",
        "visitId": "7a919381-aa64-4752-a276-21c2ac57aea5",
        "utmId": None,
        "utmSource": None,
        "searchSpecRoutesTotal": 1,
        "trackingContext": {
            "entrySource": ""
        },
        "searchSpecRouteIndex": 0
    }
}


class TravelokaSpider(scrapy.Spider):
    name = "traveloka"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_requests(self):
        cookies = open_selenium()
        yield scrapy.Request(
            url="https://www.traveloka.com/api/v2/flight/search/oneway",
            method='POST',
            callback=self.parse, body=json.dumps(body), headers=headers, cookies=open_selenium())

    def parse(self, response, **kwargs):
        self.logger.info("response header: {}".format(response.headers.items))
        f = open("response.json", "w")
        f.write(response.text)
        f.close()
