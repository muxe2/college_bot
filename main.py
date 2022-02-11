import json
import urllib.request

import fitz
import pdfplumber
import requests
from html2image import Html2Image
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import buttons
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

def messages_edit(event, f_toggle, msg, kbrd, attch = None):
    if msg:
        if "КУРС" in msg:  
            attch = "photo-209576287_457239930"       
    vk_api.messages.edit(
                        peer_id=event.obj.peer_id,
                        message=msg,
                        attachment=attch,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=(kbrd if f_toggle else kbrd).get_keyboard(),
                    )
    return not f_toggle
    
def main():  
    f_toggle: bool = False
    for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    msg = event.obj.message["text"].lower()
                    id = event.obj.message["from_id"]                                                
                    if "update" in msg:
                        send_photo(id, "Обновление...")
                        update_raspisanie()
                        send_photo(id, "Расписание обновлено")
                    
                    if "начать" in msg: 
                        vk.method("messages.send", {"peer_id": id, "message": '', "attachment": "photo-209576287_457239928", 'keyboard': kb.keyboard_main.get_keyboard(), "random_id": 0})
                     
            elif event.type == VkBotEventType.MESSAGE_EVENT:      
                event_type = event.object.payload.get("type")           
                if event_type in buttons.slov:
                    messages_edit(event, f_toggle, buttons.slov[event_type]['msg'], buttons.slov[event_type]['kb'], buttons.slov[event_type]['attch'])
                    
                else:    
                    if event in CALLBACK_TYPES:
                        vk.messages.sendMessageEventAnswer(
                            event_id=event.object.event_id,
                            user_id=event.object.user_id,
                            peer_id=event.object.peer_id,
                            event_data=json.dumps(event.object.payload),
                        )   
                                                
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
 

    
  
    






























