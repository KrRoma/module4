import vk_api
from bs4 import *

token='vk1.a.aHITjEv-uajU2UXZnquEtSnysUmNs7R3y2WNn8LljDX9lHgiJSDqV7XFgYsJQOfFdV7RYS6hdsBAc7SMNSh5n2j-uWYSIzMLag2aUZ1YqlrVcKX6V53vkbQedy9BZrvfCaE1pkTdoRVhQIveYgrYUbt-3C0iCH-9u5ZcUUXxB8-iJx3GQCOCdYvu7PdtmNCr-OnkYMru9IG5Rsk7V0bIeg'

vk=vk_api.VkApi(token=token)
vk._auth_token()

while True:
    messages=vk.method('messages.getConversations',{'count': 20,'filter':'unanswered'})

    user_id=messages['items'][0]['last_message']['from_id']
    message_id=id=messages['items'][0]['last_message']['id']
    message_text=id=messages['items'][0]['last_message']['text']
    message_text=message_text.lower
    if message_text=='планеты':
        vk.method('messages.send',{'peer_id':user_id, 'random_id':message_id, 'message':''})

