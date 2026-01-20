import json
import os
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request
from flask_mail import Mail, Message

load_dotenv()

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


@app.route("/")
def index():
    base_path = os.path.dirname(os.path.dirname(__file__))

    skills_file = os.path.join(base_path, "content", "skills.json")
    articles_file = os.path.join(base_path, "content", "articles.json")
    education_file = os.path.join(base_path, "content", "education.json")
    experiences_file = os.path.join(base_path, "content", "experiences.json")
    projects_file = os.path.join(base_path, "content", "projects.json")

    # Abrir e ler o arquivo skills.json
    with open(skills_file, "r") as f:
        skills = json.load(f)

    with open(articles_file, "r") as f:
        articles = json.load(f)

    with open(education_file, "r") as f:
        educations = json.load(f)

    with open(experiences_file, "r") as f:
        experiences = json.load(f)

    with open(projects_file, "r") as f:
        projects = json.load(f)

    return render_template(
        "index.html",
        data_skills=skills,
        data_articles=articles,
        data_educations=educations,
        data_experiences=experiences,
        data_projects=projects,
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
