import json

from vk_api.keyboard import VkKeyboard, VkKeyboardColor


#Создание кнопок
def get_but(type = "text", text = None, link = None, color = None, pay = None):
    if type == "text":
        return {
                    "action": {
                        "type": f"{type}",
                        "payload": "{\"button\": \"" + "1" + "\"}",
                        "label": f"{text}",
                        "link": f"{link}"
                    },
                    "color": f"{color}"   
                }
    
    if type == "location":
        return {
                    "action": {
                        "type": f"{type}",
                        "payload": "{\"button\": \"" + "1" + "\"}",
                    } 
                }
        
    if type == "vkpay":
        return {
                    "action": {
                        "type": f"{type}",
                        "payload": "{\"button\": \"" + "1" + "\"}",
                        "hash": f"{pay}"
                    } 
                }
        
    if type == "open_link":
        return {
                    "action": {
                        "type": f"{type}",
                        "payload": "{\"button\": \"" + "1" + "\"}",
                        "label": f"{text}",
                        "link": f"{link}"
                    }
                }
        
#Обработка кнопок
def dumper(keyboard):
    keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


# -----------------------------------------------------------
# Цвета кнопок: 
# positive - зелёный
# negative - красный
# secondary - серый
# primary - синий
#
# Виды кнопок:
# text - обычный текст
# open_link - гиперссылка 
#
# -----------------------------------------------------------

#keyboard_1.add_callback_button(
#    label="Покажи pop-up сообщение",
#    color=VkKeyboardColor.SECONDARY,
#    payload={"type": "show_snackbar", "text": "Это исчезающее сообщение на экране"},
#)

keyboard_main = VkKeyboard(one_time=False, inline=True)     
keyboard_main.add_callback_button(
    label="📋 Расписание",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "timetable"},
)    
    
keyboard_course = VkKeyboard(one_time=False, inline=True)
keyboard_course.add_callback_button(
    label="1",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "course_1"},
)
keyboard_course.add_callback_button(
    label="2",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "course_2"},
)
keyboard_course.add_callback_button(
    label="3",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "course_3"},
)
keyboard_course.add_callback_button(
    label="4",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "course_4"},
)

keyboard_1course = VkKeyboard(one_time=False, inline=True)
keyboard_1course.add_callback_button(
    "ИП",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "ИП_button"},
    )
keyboard_1course.add_callback_button(
    "11АТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11АТ_button"},
    )
keyboard_1course.add_callback_button(
    "11ИТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11ИТ_button"},
    )
keyboard_1course.add_callback_button(
    "К",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "К_button"},
    )
keyboard_1course.add_line()
keyboard_1course.add_callback_button(
    "11МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11МР_button"},
    )
keyboard_1course.add_callback_button(
    "11МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11МЭ_button"},
    )
keyboard_1course.add_callback_button(
    "11ТМ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11ТМ_button"},
    )
keyboard_1course.add_line()
keyboard_1course.add_callback_button(
    "МТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "МТ_button"},
    )
keyboard_1course.add_line()
keyboard_1course.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_K = VkKeyboard(one_time=False, inline=True)
keyboard_K.add_callback_button(
    "11К",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11К_button"},
    )
keyboard_K.add_callback_button(
    "12К",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "12К_button"},
    )
keyboard_K.add_line()
keyboard_K.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_MT = VkKeyboard(one_time=False, inline=True)
keyboard_MT.add_callback_button(
    "11МТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11МТ_button"},
    )
keyboard_MT.add_callback_button(
    "12МТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "12МТ_button"},
    )
keyboard_MT.add_line()
keyboard_MT.add_callback_button(
    "13МТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "13МТ_button"},
    )
keyboard_MT.add_callback_button(
    "14МТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "14МТ_button"},
    )
keyboard_MT.add_line()
keyboard_MT.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_IP = VkKeyboard(one_time=False, inline=True)
keyboard_IP.add_callback_button(
    "11ИП",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "11ИП_button"},
    )
keyboard_IP.add_callback_button(
    "12ИП",
    color=VkKeyboardColor.POSITIVE,
    payload={"type": "12ИП_button"},
    )
keyboard_IP.add_line()
keyboard_IP.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_2course = VkKeyboard(one_time=False, inline=True)
keyboard_2course.add_callback_button(
    "21МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "21МР_button"},
    )
keyboard_2course.add_callback_button(
    "22МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "22МР_button"},
    )
keyboard_2course.add_callback_button(
    "21МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "21МЭ_button"},
    )
keyboard_2course.add_line()
keyboard_2course.add_callback_button(
    "21РА",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "21РА_button"},
    )
keyboard_2course.add_callback_button(
    "21ТМ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "21ТМ_button"},
    )
keyboard_2course.add_callback_button(
    "21РТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "21РТ_button"},
    )
keyboard_2course.add_line()
keyboard_2course.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_3course = VkKeyboard(one_time=False, inline=True)
keyboard_3course.add_callback_button(
    "31К",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31К_button"},
    )
keyboard_3course.add_callback_button(
    "32К",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "32К_button"},
    )
keyboard_3course.add_callback_button(
    "31МС",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31МС_button"},
    )
keyboard_3course.add_line()
keyboard_3course.add_callback_button(
    "31МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31МЭ_button"},
    )
keyboard_3course.add_callback_button(
    "32МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "32МЭ_button"},
    )
keyboard_3course.add_callback_button(
    "31РТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31РТ_button"},
    )
keyboard_3course.add_line()
keyboard_3course.add_callback_button(
    "МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "МР_button"},
    )
keyboard_3course.add_callback_button(
    "31П",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31П_button"},
    )
keyboard_3course.add_line()
keyboard_3course.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_MR = VkKeyboard(one_time=False, inline=True)
keyboard_MR.add_callback_button(
    "31МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "31МР_button"},
    )
keyboard_MR.add_callback_button(
    "32МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "32МР_button"},
    )
keyboard_MR.add_callback_button(
    "33МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "33МР_button"},
    )
keyboard_MR.add_line()
keyboard_MR.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )

keyboard_4course = VkKeyboard(one_time=False, inline=True)
keyboard_4course.add_callback_button(
    "41АТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "41АТ_button"},
    )
keyboard_4course.add_callback_button(
    "41ТО",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "41ТО_button"},
    )
keyboard_4course.add_callback_button(
    "41РТ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "41РТ_button"},
    )
keyboard_4course.add_line()
keyboard_4course.add_callback_button(
    "41МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "41МЭ_button"},
    )
keyboard_4course.add_callback_button(
    "42МЭ",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "42МЭ_button"},
    )
keyboard_4course.add_line()
keyboard_4course.add_callback_button(
    "41МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "41МР_button"},
    )
keyboard_4course.add_callback_button(
    "42МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "42МР_button"},
    )
keyboard_4course.add_callback_button(
    "43МР",
    color=VkKeyboardColor.PRIMARY,
    payload={"type": "43МР_button"},
    )
keyboard_4course.add_line()
keyboard_4course.add_callback_button(
    "Отмена",
    color=VkKeyboardColor.NEGATIVE,
    payload={"type": "Отмена_button"},
    )


def render(course):
    print(course)
    if course == '1':
        return keyboard_1course.get_keyboard()
        
    elif course == '2': 
        return keyboard_2course.get_keyboard()    
    
    elif course == '3': 
        return keyboard_3course.get_keyboard()   

    elif course == '4': 
        return keyboard_4course.get_keyboard()   


link = {
    "one_time" : True,
    "buttons" : [
        [get_but('open_link', 'Привет', "https://www.youtube.com/watch?v=_p9RYmIw6mM")]
    ]
}

location = {
    "one_time" : True,
    "buttons" : [
        [get_but('location')]
    ]
}

bye = {
    "one_time" : True,
    "buttons" : [
        [get_but('пока', 'positive'), get_but('пока', 'negative')],
        [get_but('пока', 'secondary'), get_but('пока', 'primary')]
    ]
}


#Переменные для вызова кнопок
link = dumper(link)
bye = dumper(bye)
location = dumper(location)
