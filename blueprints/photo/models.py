# blueprints/blog/models.py
# Example SQLAlchemy model
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import pandas as pd

db = SQLAlchemy()


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(200))
    filename = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def import_csv_with_pandas():
    # Read CSV
    df = pd.read_csv('test/photos.csv', encoding='gb18030')

    # If table exists, append to it
    df.to_sql('photo', db.engine, if_exists='append', index=False)

    # Or if you want to replace the table
    # df.to_sql('users', db.engine, if_exists='replace', index=False)

    print(f"Imported {len(df)} records")
