from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

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
    return render_template("index.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.methods == "POST":
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
    app.run(debug=True)
