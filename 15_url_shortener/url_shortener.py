from typing import Final
import requests

# Constants
API_KEY: Final[str] = 'YOUR_KEY'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


# Function to shorten any link with a custom name
def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link, }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    # Gets the relevant information we need
    if url_data := data.get('url'):
        if url_data['status'] == 7:   # 7 means that OK - the link has been shortned 
            short_link: str = url_data['shortLink']
            print('Link:', short_link)
        else:
            print('Error status:', url_data['status'])

        # To handle the error some new part of code must be added 
        # Since there is the need to have a account in cutt.ly, I will skip it. 

def main():
    # Take user input
    link: str = input('Enter a link: ')

    # Shorten the link
    shorten_link(link)


if __name__ == '__main__':
    main()
