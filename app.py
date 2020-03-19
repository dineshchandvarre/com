from get import GetMethods
import json


class Services:
    def get_ips(self, host, name, password):

        with open('config.json') as config_file:
            cfg = json.load(config_file)

        host_tokens = host.split('/')
        assest_path = host_tokens[0]

        headers = {
            'Authorization': "Basic " + password,
        }

        response = GetMethods.get_response(cfg["host"] + assest_path, headers)

        response.json()
        print(response.json())


if __name__ == '__main__':
    # Pass host and team name as parameters
    Services().get_ips("", "", "")