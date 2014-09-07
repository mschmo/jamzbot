#!/usr/bin/env python
import json
import requests
import messages
from config import WEBHOOK_URL


def main(name):
    message = getattr(messages, name)
    if not message:
        raise ValueError('Invalid Message: {}'.format(name))

    jamz = message()
    text = jamz.get_message()

    if text:
        payload = {
            'text': text,
            'username': 'JamzBot',
            'icon_emoji' : ':dancingbanana:'
        }

        return requests.post(WEBHOOK_URL, data=json.dumps(payload))

if __name__ == '__main__':
    import sys
    main(sys.argv[1])