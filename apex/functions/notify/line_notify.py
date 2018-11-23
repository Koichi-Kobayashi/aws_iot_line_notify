# -*- coding: utf-8 -*-

import requests
import conf


def create_message(button_event):
    if button_event['clickType'] == 'SINGLE':
        msg = conf.clickType_single
    elif button_event['clickType'] == 'DOUBLE':
        msg = conf.clickType_double
    else:
        msg = conf.clickType_long

    return msg


def lambda_handler(event, context):
    url = "https://notify-api.line.me/api/notify"
    token = conf.token
    headers = {"Authorization": "Bearer " + token}

    button_event = event['deviceEvent']['buttonClicked']
    payload = {"message": create_message(button_event)}

    r = requests.post(url, headers=headers, params=payload)


if __name__ == '__main__':
    event = ''
    lambda_handler(event, None)

