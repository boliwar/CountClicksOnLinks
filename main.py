import requests
import urllib.parse
import os
from dotenv import load_dotenv
import argparse


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('url', nargs='?')
    return parser

def shorten_link(url, headers):
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                                json={"long_url": url},
                                headers=headers)
    shorten_res.raise_for_status()
    short_url = shorten_res.json().get("link")
    return short_url

def is_bitlink(url, headers):
    url_components = urllib.parse.urlparse(url)
    bitlink_res = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url_components.netloc}{url_components.path}", headers=headers)
    return bitlink_res.ok

def count_clicks(url, headers):
    url_components = urllib.parse.urlparse(url)
    clicks_res = requests.get(f"https://api-ssl.bitly.com//v4/bitlinks/{url_components.netloc}{url_components.path}/clicks/summary", headers=headers)
    clicks_res.raise_for_status()
    clicks_count = clicks_res.json()["total_clicks"]
    return clicks_count

def main():
    load_dotenv()
    bitly_access_token = os.environ['BITLY_ACCESS_TOKEN']
    headers = {"Authorization": f"Bearer {bitly_access_token}"}

    # input_url = input("Введите ссылку: ")
    parser = createParser()
    namespace = parser.parse_args()

    input_url = namespace.url

    try:
        if not is_bitlink(input_url, headers):
            short_url = shorten_link(input_url, headers)
            print(f"Битлинк: {short_url}")
        else:
            sum_clicks = count_clicks(input_url, headers)
            print(f"По вашей ссылки прошли {sum_clicks} раза")
    except requests.exceptions.HTTPError:
        print(f'Wrong URL: {input_url}')


if __name__ == "__main__":
    main()
