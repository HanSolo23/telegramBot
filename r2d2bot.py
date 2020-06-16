import requests
from misc import token
import json

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    proxies = {
        'http': '35.187.58.241:3128',
        'https': '185.25.206.192:8080'
    }
    response = requests.get(url, proxies=proxies)
    return response.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        #username = last_object['message']['from']['username']
        message_text = last_object['message']['text']
        message = {
            'chat_id': chat_id,
            #'username': username,
            'text': message_text
        }
        return message
    return None


def send_message(chat_id, text='wait...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    proxies = {
        'http': '35.187.58.241:3128',
        'https': '185.25.206.192:8080'
    }
    requests.get(url, proxies=proxies)


def main():
    #answer = get_message()
    #chat_id = answer['chat_id']
    #text = answer['text']
    #username = answer['username']
    #if 'привет' in text:
        #send_message(chat_id, 'привет')
    #newdict = get_updates()

    #with open('updates.json', 'w', encoding='utf8') as file:
        #json.dump(newdict, file, indent=2, ensure_ascii=False)

    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            #username = answer['username']
            text = answer['text']
            if text == 'привет' or text == 'Привет':
                send_message(chat_id, 'Привет, как дела?')
            elif text == 'хорошо' or text == 'Хорошо':
                send_message(chat_id, 'Это же великолепно!')
            elif text == 'плохо' or text == 'Плохо':
                send_message(chat_id, 'Это печально:(')
        else:
            continue


if __name__ == '__main__':
    main()
