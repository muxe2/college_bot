import json

import requests
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import config
import kb
import updater

vk = VkApi(token = config.TOKEN)
vk_api = vk.get_api()
CALLBACK_TYPES = ("show_snackbar", "open_link", "open_app")
longpoll = VkBotLongPoll(vk, group_id=config.GROUP_ID)


def send(id:int=None, text:str=None, photo:str=None, keyboard:str=None, render:bool=False) -> str:
    if photo and render:
        photoUpload = vk.method("photos.getMessagesUploadServer")
        photoRequests = requests.post(photoUpload['upload_url'], files={
                                      'photo': open(f'{photo}.png', 'rb')}).json()
        photoMethod = vk.method('photos.saveMessagesPhoto', {
                                'photo': photoRequests['photo'],
                                'server': photoRequests['server'],
                                'hash': photoRequests['hash']})[0]
        photo = "photo{}_{}".format(photoMethod["owner_id"], photoMethod["id"])
        return photo

    else:
        vk.method("messages.send", {"peer_id": id, "message": text,
                  "attachment": str(photo), 'keyboard': keyboard, "random_id": 0})


def messages_edit(event, f_toggle:bool, text:str=None, keyboard:str=None, photo:str=None, unknown:bool=None) -> bool:
    if text and "КУРС" in text:
        photo = "photo-209576287_457239930"
    vk_api.messages.edit(
        peer_id=event.obj.peer_id,
        message=text,
        attachment=photo,
        conversation_message_id=event.obj.conversation_message_id,
        keyboard=keyboard if unknown else (
            keyboard if f_toggle else keyboard).get_keyboard(),
    )
    return not f_toggle


def main():
    f_toggle = False
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                msg = event.obj.message["text"].lower()
                id = event.obj.message["from_id"]
                if msg != '':
                     send(id, '', "photo-209576287_457239928",
                         kb.keyboard_main_admin.get_keyboard() if id in config.ADMINS else kb.keyboard_main.get_keyboard())

          
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            event_type = event.object.payload.get("type")
            event_text = event.object.payload.get('text')

            if event_type in kb.slov:
                messages_edit(event, f_toggle, kb.slov[event_type]['msg'],
                              kb.slov[event_type]['kb'], kb.slov[event_type]['attch'])
            
            elif event_type == 'Отмена_button':
                messages_edit(event, f_toggle, text = '', photo = "photo-209576287_457239928",
                              keyboard = kb.keyboard_main_admin if event.object.user_id in config.ADMINS else kb.keyboard_main
                              )    
                
            else:
                if event_type in CALLBACK_TYPES:
                    vk_api.messages.sendMessageEventAnswer(
                        event_id=event.object.event_id,
                        user_id=event.object.user_id,
                        peer_id=event.object.peer_id,
                        event_data=json.dumps(event.object.payload),
                    )
                    
                    if event_text == 'Расписание обновиться через 30 секунд':
                        updater.update_raspisanie()
                        


                else:
                    button = event.object.payload.get("type")
                    group = button.replace("_button", '')
                    course = list(group)[0]
                    with open('raspis.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    messages_edit(event, f_toggle, f"Расписание для {group}", kb.render(
                        course), data['list'][group], unknown=True)


if __name__ == '__main__':
    print("DigestBot has been started")
    main()



