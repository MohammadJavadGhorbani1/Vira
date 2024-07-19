import requests

def send_sms(recipient , code):
    api_key = 'etjhykgjhrt'
    response = requests.post(url='https://api2.ippanel.com/api/v1' , headers={
        'api_key':api_key
    } , json={
        {
            "code": "zd7xxxxf5h",
            "sender": "+983000505",
            "recipient": recipient,
            "variable": {
                "confirm_code": code
            }
        }
    })
    return response