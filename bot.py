import vk_api
from vk_api import keyboard
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import json

vk_session = vk_api.VkApi(token='4541ad2c7b80486f8f66a03061eb411ac96ad59a31aa3fe452ff79a60909193eccb09ab1afc03e38b41b2')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

keyboard = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "&#128179;Баланс"
                },
                "color": "positive"
            }
        ]
    ]
}
 
main_menu_keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
main_menu_keyboard = str(keyboard.decode('utf-8'))


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.text == 'Начать':
              vk_session.method('messages.send', {
                "peer_id": event.peer_id,
                "message": "Приветственное сообщение",
                "random_id": get_random_id(),
                "keyboard": main_menu_keyboard})
            