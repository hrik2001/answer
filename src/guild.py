from quart import Blueprint, session, render_template, request, redirect , current_app
from . import models
import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import secrets
import string
engine = create_engine("sqlite:///data.db")
models.create(engine)

sess = Session(engine)

def gen(N):
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))

guild = Blueprint("guild", __name__ , template_folder="templates")

@guild.route("/create", methods=["GET"])
async def create():
    if request.method == "GET":
        # return "hi"
        try:
            prev_entry = sess.query(models.Verify).filter_by(username = session["user"]).first()
            if prev_entry:
                return(prev_entry.otp)
            else:
                otp = gen(10)
                verification = models.Verify(username = session["user"] , otp = otp)
                sess.add(verification)
                sess.commit()
                # return(session["user"])
                return(otp)
        except:
            return(redirect("/login"))
