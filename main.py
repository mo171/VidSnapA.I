from flask import Flask, render_template, request,redirect,url_for,flash
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "your_secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():

    myid = uuid.uuid1() # Generate a unique identifier
    recieved_id = request.form.get("myid") 
    descr = request.form.get("text") 

    if request.method == "POST":
        # Handle form submission logic here
        
        for key,value in request.files.items(): # key is the name attribute in the form, value is the file
          
          file =request.files[key] # contains the file metadata in `<FileStorage: 'human.jpeg' ('image/jpeg')>` format
          if file:
            filename = secure_filename(file.filename) # secure the filename before storing it directly `'human.jpeg'`
            if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], recieved_id)):
                os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], recieved_id)) 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], recieved_id, filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], recieved_id, "descr.txt"), 'w') as f:
                f.write(descr)
            flash('File successfully uploaded') 


    return render_template("create.html", myid=myid)


@app.route("/gallery")
def gallery():
    
    return render_template("gallery.html")

app.run(debug=True)