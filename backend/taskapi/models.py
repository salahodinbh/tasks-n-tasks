"""
models.py
- Clases de modelo de datos para las tasks de la aplicación
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    completed=self.completed,
                    completion_date = self.completion_date
                    )

'''
class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    choices = db.relationship('Choice', backref='question', lazy=False)

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    survey_id=self.survey_id,
                    choices=[choice.to_dict() for choice in self.choices])

class Choice(db.Model):
    __tablename__ = 'choices'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    selected = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def to_dict(self):
        return dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    question_id=self.question_id)
'''