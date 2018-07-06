import requests

def line(me):
    line_notify_token = 'TOKEN'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '\n' + me
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

line('💩')