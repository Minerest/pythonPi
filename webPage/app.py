from flask import Flask, render_template, json
import os
app = Flask(__name__)

@app.route("/")
def main():
    path = "./static"
    images = [x for x in os.listdir(path) if (not x.endswith(".js") and not x.endswith(".ini"))]
    
    return render_template("index.html", images = json.dumps(images))

if __name__ == "__main__":
    app.run()
    
