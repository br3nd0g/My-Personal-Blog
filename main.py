from flask import Flask, render_template, request
import interactWithJSON as si

baseURL = 'https://personal-blog.repl.co/'

app = Flask("Brendog's Blog")
app.static_folder = 'static'

passw = "myPassword"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':

      jsonData = si.getData()
      
      return render_template('index.html', url=baseURL, passwordCorrect=False, jsonn=jsonData)

    if request.method == 'POST':

      jsonData = si.getData()

      try:
        
        inpPassw = request.form['password']
        if inpPassw == passw:
          return render_template('index.html', url=baseURL, passwordCorrect=True, jsonn=jsonData)
        else:
          return render_template('index.html', url=baseURL, passwordCorrect=False, jsonn=jsonData)
      except:

        
        
        postTitle = request.form['title']
        postText = request.form['text']
        si.updateData(postTitle, postText)
        jsonData = si.getData()
        
        return render_template('index.html', url=baseURL, passwordCorrect=False, jsonn=jsonData)


      
app.run(host='0.0.0.0', port=8080, debug=True)
