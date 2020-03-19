# All get requests are defined here

import requests


class GetMethods:

    @staticmethod
    def get_response(url, headers):

        try:
            response = requests.get(url, headers)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)

        except requests.exceptions.TooManyRedirects as err:
            print("TooManyRedirects:", err)

        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)

        return response