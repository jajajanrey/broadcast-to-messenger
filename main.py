""" Import required libraries """
import json
import requests

from time import sleep


FB_BASE_URL = "https://graph.facebook.com/v2.6/me/messages?access_token={page_access_token}"


def send_message(url, message, psid, messaging_type):
    headers = {'Content-Type': 'application/json'}
    recipient = {'id': str(psid)}
        
    payload = {
        'messaging_type': messaging_type,
        'recipient': recipient,
        'message': message
    }

    result = requests.post(url,
        data=json.dumps(payload),
        headers=headers)

    return result

    
def main(message, FB_ids, page_access_token, messaging_type="UPDATE"):
    """ Broadcast messages to messenger. """

    if not type(message) is str or \
        not type(FB_ids) is str or \
        not type(page_access_token) is str:
        return {
            "code": 400,
            "message": "Params must be string"
        }
    try:
        message = json.loads(message)
        FB_ids = json.loads(FB_ids)
    except Exception:
        return {
            "code": 400,
            "message": "Bad parameters"
        }

    fb_url_formatted = FB_BASE_URL.format(
        page_access_token=page_access_token)

    if type(FB_ids) is list:
        for x in range(0, len(FB_ids)):
            send_message(
                url=fb_url_formatted,
                message=message,
                psid=FB_ids[x],
                messaging_type=messaging_type)

            ''' sleep for 1.5s since maximum request per second is 250 '''
            if x % 200 == 0:
                sleep(1.5)

    return {
        "code": 200,
        "message": "Successfully broadcasted messages"
    }
