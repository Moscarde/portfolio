from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
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


@app.route("/")
def index():
    skills_file = os.path.join(app.root_path, 'content', 'skills.json')
    
    # Abrir e ler o arquivo skills.json
    with open(skills_file, 'r') as f:
        skills = json.load(f)

    print(skills)

    return render_template("index.html", data_skills=skills)


@app.route("/send", methods=["GET", "POST"])
def send():
    print('----------------', request.method)
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
