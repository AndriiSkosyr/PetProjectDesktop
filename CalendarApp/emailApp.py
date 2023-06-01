import requests
from jproperties import Properties

configs = Properties()

with open('app_config.properties', 'rb') as config_file:
    configs.load(config_file)


def send_simple_message(to_name_to_email, subject, text):
    post_response = requests.post(configs.get("REQUEST_ADDRESS").data,
        auth=("api", configs.get("API_KEY").data),
        data={"from": configs.get("API_DOMAIN").data,
              "to": to_name_to_email,
              "subject": subject,
              "text": text})
    post_response_json = post_response.json()
    print(post_response_json)


if __name__ == '__main__':
    send_simple_message()
