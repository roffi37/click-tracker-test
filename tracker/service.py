import os
import requests

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("API_TOKEN")


def shorter_url_api(clicked_url):
	url = "https://url-shortener-service.p.rapidapi.com/shorten"

	payload = {"url": f"https://{clicked_url}"}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": f"{TOKEN}",
		"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
	}

	response = requests.post(url=url, data=payload, headers=headers)

	return response.json().get("result_url")
