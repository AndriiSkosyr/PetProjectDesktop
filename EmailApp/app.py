from pysendpulse.pysendpulse import PySendPulse

# API initialization
if __name__ == "__main__":
    REST_API_ID = '327cac1945490a7009ada8366ec08101'
    REST_API_SECRET = 'effa7d9fccf8a1c19554b1f81cd1cde6'
    TOKEN_STORAGE = 'memcached'
    MEMCACHED_HOST = '127.0.0.1:11211'
    SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE, memcached_host=MEMCACHED_HOST)

# Send mail using SMTP
    email = {
        'subject': 'This is the test task from REST API',
        'html': '<h1>Hello, John!</h1><p>This is the test task from https://sendpulse.com/api REST API!</p>',
        'text': 'Hello, John!\nThis is the test task from https://sendpulse.com/api REST API!',
        'from': {'name': 'Andrii Skosyr', 'email': 'akaciand29@gmail.com'},
        'to': [
            {'name': 'Jane Roe', 'email': 'askosyr@gmail.com'}
        ],
        'bcc': [
            {'name': 'Richard Roe', 'email': 'akaciand29@gmail.com'}
        ]
    }
    SPApiProxy.smtp_send_mail(email)
