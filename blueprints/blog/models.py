# blueprints/blog/models.py
# Example SQLAlchemy model
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

db = SQLAlchemy()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))


def import_csv_with_pandas() :
    # Read CSV
    df = pd.read_csv('test/users.csv')

    # If table exists, append to it
    df.to_sql('user', db.engine, if_exists='append', index=False)

    # Or if you want to replace the table
    # df.to_sql('users', db.engine, if_exists='replace', index=False)

    print(f"Imported {len(df)} records")
