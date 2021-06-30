from quart import Blueprint, session, render_template, request, redirect

auth = Blueprint("auth", __name__ , template_folder="templates")

@auth.route("/login", methods=["GET" , "POST"])
async def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        form = await request.form
        print(form)
        return(redirect("/"))

@auth.route("/signup", methods=["GET" , "POST"])
async def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        form = await request.form
        print(form)
        return(redirect("/login"))
