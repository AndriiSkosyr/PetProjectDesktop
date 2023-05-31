import requests


def send_simple_message():
    post_response = requests.post(
        "https://api.mailgun.net/v3/sandbox1e49fda3257547f4a87e344def7e694c.mailgun.org/messages",
        auth=("api", "3f8f07b3b59bbcf5406ec1847a193525-5d9bd83c-a4f9992b"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox1e49fda3257547f4a87e344def7e694c.mailgun.org>",
              "to": "Andrii Skosyr <akaciand29@gmail.com>",
              "subject": "Hello Andrii Skosyr",
              "text": "Congratulations Andrii Skosyr, you just sent an email with Mailgun!  You are truly awesome!"})
    post_response_json = post_response.json()
    print(post_response_json)


if __name__ == '__main__':
    send_simple_message()
