from flask import Flask
from flask import redirect, request, render_template
from pymongo import Connection

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def main():

    db = Connection()["python"]
    table = db["mesaj"]
    kayitlar = list(table.find())

    
    if request.method == 'POST':
        name    = request.form.get("name")
        mesaj   = request.form.get("mesaj")

        table.insert({"name": name, "mesaj": mesaj})
        return redirect("/")

    else:
        return render_template("form.html", kayitlar = kayitlar)



if __name__ == "__main__":
    app.run(debug=True)
