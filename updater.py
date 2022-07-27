import json
import os
import main
import aspose.words as aw

def update_raspisanie():
    options = aw.saving.ImageSaveOptions(aw.SaveFormat.PNG)
    with open("raspis.json", "rt", encoding="utf-8") as file:
        settings = json.load(file)
        
    for i in os.listdir("course_doc"):
        doc = aw.Document(f"course_doc/{i}")
        group = i.split('.')[0].upper().replace(' ', '')
        doc.save(f"courses/{i[0]}/{group}.png", options)  
        photo = f"courses/{i[0]}/{group}"       
        print(photo)
        photo = main.send(photo=photo, render=True)
        settings["list"][group] = photo
        with open("raspis.json", "wt", encoding="utf-8") as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
                    
    print('Расписание обнавлено')
    

