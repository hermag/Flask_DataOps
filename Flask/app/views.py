from app import app

@app.route("/")
def index():
    return "<h1 style='color:red'>Alohaaaa</h1>"

@app.route("/about")
def about():
    return "This is about page"