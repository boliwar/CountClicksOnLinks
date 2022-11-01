import requests
import urllib.parse
import os
from dotenv import load_dotenv
import argparse


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('url', nargs='?')
    return parser

def shorten_link(url, bitly_access_token):
    headers = {"Authorization": f"Bearer {bitly_access_token}"}
    shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                                json={"long_url": url},
                                headers=headers)
    shorten_res.raise_for_status()
    short_url = shorten_res.json().get("link")
    return short_url

def is_bitlink(url, bitly_access_token):
    headers = {"Authorization": f"Bearer {bitly_access_token}"}
    url_components = urllib.parse.urlparse(url)
    bitlink_res = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url_components.netloc}{url_components.path}", headers=headers)
    return bitlink_res.ok

def count_clicks(url, bitly_access_token):
    headers = {"Authorization": f"Bearer {bitly_access_token}"}
    url_components = urllib.parse.urlparse(url)
    clicks_res = requests.get(f"https://api-ssl.bitly.com//v4/bitlinks/{url_components.netloc}{url_components.path}/clicks/summary", headers=headers)
    clicks_res.raise_for_status()
    clicks_count = clicks_res.json()["total_clicks"]
    return clicks_count

def main():
    load_dotenv()
    bitly_access_token = os.environ['BITLY_ACCESS_TOKEN']

    parser = create_parser()
    command_line_arguments = parser.parse_args()

    input_url = command_line_arguments.url

    try:
        if not is_bitlink(input_url, bitly_access_token):
            short_url = shorten_link(input_url, bitly_access_token)
            print(f"Битлинк: {short_url}")
        else:
            sum_clicks = count_clicks(input_url, bitly_access_token)
            print(f"По вашей ссылки прошли {sum_clicks} раза")
    except requests.exceptions.HTTPError:
        print(f'Wrong URL: {input_url}')


if __name__ == "__main__":
    main()
