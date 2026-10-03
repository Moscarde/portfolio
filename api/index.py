import json
import os
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request
from flask_mail import Mail, Message

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')
app.secret_key = "secret"


mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get("MAIL"),
    "MAIL_PASSWORD": os.environ.get("PASSWORD"),
}

app.config.update(mail_settings)

mail = Mail(app)


class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


def load_content(name):
    with open(os.path.join(root_dir, "content", f"{name}.json"), encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=load_content("profile"),
        data_skills=load_content("skills"),
        data_articles=load_content("articles"),
        data_educations=load_content("education"),
        data_experiences=load_content("experiences"),
        data_projects=load_content("projects"),
    )


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        formContato = Contato(
            request.form["nome"], request.form["email"], request.form["mensagem"]
        )

        msg = Message(
            subject=f"{formContato.nome} te enviou uma mensagem",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f"""De: {formContato.nome}
E-mail: {formContato.email}
Mensagem: {formContato.mensagem}
        """,
        )

        mail.send(msg)
        flash("Mensagem enviada com sucesso!", "success")

    return redirect("/")


if __name__ == "__main__":
    app.run(port=5001, debug=True)
