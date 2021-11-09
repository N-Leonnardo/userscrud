from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route("/users")
def showusers():
    users = User.get_all()
    print(users)
    return render_template("newuser.html", users=users)


@app.route("/")
def index():
    return render_template("index.html")
            





            
if __name__ == "__main__":
    app.run(debug=True)
