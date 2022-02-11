import json
import urllib.request

import fitz
import pdfplumber
import requests
from html2image import Html2Image
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

import kb

admins = []
GROUP_ID = "209576287"
vk = VkApi(token="66ad8c5a9dcaaadde5ad4b4f9840b877843066c41caf69abbe84d5db39af8b12ec7094aa96e22d47bf89d")
vk_api = vk.get_api()
CALLBACK_TYPES = ("show_snackbar", "open_link", "open_app")
longpoll = VkBotLongPoll(vk, group_id=GROUP_ID)

hti = Html2Image()


def send_photo(id, text, photo = None, photo2 = None, keyboard = None):
    if photo:
        photoUpload = vk.method("photos.getMessagesUploadServer")
        photoRequests = requests.post(photoUpload['upload_url'], files={'photo': open(f'{photo}.png', 'rb')}).json()
        photoMethod = vk.method('photos.saveMessagesPhoto', {'photo': photoRequests['photo'], 'server': photoRequests['server'], 'hash': photoRequests['hash']})[0]
        photo = "photo{}_{}".format(photoMethod["owner_id"], photoMethod["id"])
    
    if photo2:
        photoUpload = vk.method("photos.getMessagesUploadServer")
        photoRequests = requests.post(photoUpload['upload_url'], files={'photo': open(f'{photo2}.png', 'rb')}).json()
        photoMethod = vk.method('photos.saveMessagesPhoto', {'photo': photoRequests['photo'], 'server': photoRequests['server'], 'hash': photoRequests['hash']})[0]
        photo2 = "photo{}_{}".format(photoMethod["owner_id"], photoMethod["id"])
    vk.method("messages.send", {"peer_id": id, "message": text, "attachment": f"{photo},{photo2}", 'keyboard': keyboard, "random_id": 0})


def send_photo_render(photo):
    photoUpload = vk.method("photos.getMessagesUploadServer")
    photoRequests = requests.post(photoUpload['upload_url'], files={'photo': open(f'{photo}.png', 'rb')}).json()
    photoMethod = vk.method('photos.saveMessagesPhoto', {'photo': photoRequests['photo'], 'server': photoRequests['server'], 'hash': photoRequests['hash']})[0]
    photo = "photo{}_{}".format(photoMethod["owner_id"], photoMethod["id"])
    return photo


def main():
    f_toggle: bool = False
    for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    msg = event.obj.message["text"]
                    id = event.obj.message["from_id"]
                    msg_id = event.obj.message["id"]
                    
                    with open('raspis.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                                          
                    if "update" in msg:
                        update_raspisanie()
                        send_photo(id, "Расписание обновлено")
                    
                    if "ачать" in msg: 
                        vk.method("messages.send", {"peer_id": id, "message": '', "attachment": "photo-209576287_457239928", 'keyboard': kb.keyboard_main.get_keyboard(), "random_id": 0})
                     
            elif event.type == VkBotEventType.MESSAGE_EVENT:
                if event.object.payload.get("type") in CALLBACK_TYPES:
                    vk.messages.sendMessageEventAnswer(
                        event_id=event.object.event_id,
                        user_id=event.object.user_id,
                        peer_id=event.object.peer_id,
                        event_data=json.dumps(event.object.payload),
                    )
                    
                elif event.object.payload.get("type") == "timetable":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="Расписание",
                        attachment="photo-209576287_457239929",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_course if f_toggle else kb.keyboard_course).get_keyboard(),
                    )
                    f_toggle = not f_toggle 
                            
                elif event.object.payload.get("type") == "course_1":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="1 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_1course if f_toggle else kb.keyboard_1course).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                    
                elif event.object.payload.get("type") == "course_2":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="2 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_2course if f_toggle else kb.keyboard_2course).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                    
                elif event.object.payload.get("type") == "course_3":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="3 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_3course if f_toggle else kb.keyboard_3course).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                    
                elif event.object.payload.get("type") == "course_4":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="4 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_4course if f_toggle else kb.keyboard_4course).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                    
                elif event.object.payload.get("type") == "МТ_button":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="1 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_MT if f_toggle else kb.keyboard_MT).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                
                elif event.object.payload.get("type") == "ИП_button":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="1 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_IP if f_toggle else kb.keyboard_IP).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                
                elif event.object.payload.get("type") == "МР_button":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="3 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_MR if f_toggle else kb.keyboard_MR).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                        
                elif event.object.payload.get("type") == "К_button":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message="1 КУРС",
                        attachment = "photo-209576287_457239930",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_K if f_toggle else kb.keyboard_K).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                        
                elif event.object.payload.get("type") == "Отмена_button":
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        attachment= "photo-209576287_457239928",
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kb.keyboard_main if f_toggle else kb.keyboard_main).get_keyboard(),
                    )
                    f_toggle = not f_toggle
                            
                else:
                    button = event.object.payload.get("type")
                    text = button.replace("_button", '')
                    course = list(text)[0]
                    with open('raspis.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message=f"Расписание для {text}",
                        attachment = data['list'][text],
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=kb.render(course),
                    )
                    f_toggle = not f_toggle
                    
  
       
              
def update_raspisanie():
    pdfs = ['1k.pdf', '2k.pdf', '3k.pdf', '4k.pdf']
    url = ['http://www.pl130.ru/doc/19/1k.pdf', 'http://www.pl130.ru/doc/19/2k.pdf', 'http://www.pl130.ru/doc/19/3k.pdf', 'http://www.pl130.ru/doc/19/4k.pdf']
    numbers = []
    
    with open("raspis.json", "rt", encoding="utf-8") as file:
        settings = json.load(file)      
     
    for i in url:   
        file = i.split('/')[5]
        urllib.request.urlretrieve(i, f'course_pdf/{file}')
        
    for pdffile in pdfs:  
        course = list(pdffile)[0]
        pdffile = f'course_pdf/{pdffile}' 
        with pdfplumber.open(pdffile) as pdf:        
            totalpages = len(pdf.pages)
            doc = fitz.open(pdffile)
            for i in range(0, totalpages):
                pageobj = pdf.pages[i]
                group = pageobj.extract_text().split()[:5][2].replace("_", '')              
                page = doc.load_page(i)
                pix = page.get_pixmap()
                output = f"courses/{course}/{group}"
                pix.save(f"{output}.png")
                
                photo = send_photo_render(output)              
                settings["list"][group] = photo
                with open("raspis.json", "wt", encoding="utf-8") as f:  
                    json.dump(settings, f, indent=4)

if __name__ == '__main__':
    print("DigestBot has been started")
    main()
 

    
  
    






























