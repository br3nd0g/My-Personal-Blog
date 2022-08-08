from datetime import datetime
import pytz
import json


def updateData(title, text):

    file = open("posts.json", "r")
    jsonData = json.load(file)
    file.close()

    timezone = pytz.timezone('Europe/London')
    frmtdTime = datetime.now(timezone)
    date= frmtdTime.strftime("%d/%m/%Y")


    post = {"title": title, "text": text, "date": date}
    jsonData["posts"].append(post)

    with open('./posts.json', 'w') as outfile:
      json.dump(jsonData, outfile)

def getData():
    
  file = open("posts.json", "r")
  jsonData = json.load(file)
  jsonData = json.dumps(jsonData)
  file.close()

  return jsonData