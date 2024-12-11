from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Question

app = Flask(__name__)

engine = create_engine("sqlite:///questions.sqlite", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def index():
    questions = session.query(Question).all()
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    results = []
    for question in session.query(Question).all():
        question_id = question.id
        user_answer = request.form.get(f"{question_id}")
        if user_answer and question.correct_answer.lower() == user_answer.lower():
            results.append((question.question, "Correct!"))
        else:
            results.append((question.question, "Incorrect!"))
    return render_template("results.html", results=results) 

if __name__ == "__main__":
    app.run(debug=True)