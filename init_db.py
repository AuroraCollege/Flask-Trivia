from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Question

engine = create_engine("sqlite:///questions.sqlite", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add some questions
questions = [
    Question(
        question="What is the capital of France?",
        choice_a="Berlin",
        choice_b="Madrid",
        choice_c="Paris",
        choice_d="Rome",
        correct_answer="c"
    ),
    Question(
        question="What is 2 + 2?",
        choice_a="3",
        choice_b="4",
        choice_c="5",
        choice_d="6",
        correct_answer="b"
    ),
    Question(
        question="Who wrote 'To Kill a Mockingbird'?",
        choice_a="Mark Twain",
        choice_b="Harper Lee",
        choice_c="Ernest Hemingway",
        choice_d="F. Scott Fitzgerald",
        correct_answer="b"
    )
]

session.add_all(questions)
session.commit()