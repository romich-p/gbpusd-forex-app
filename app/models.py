from app import db

class Candle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    timeframe = db.Column(db.String(10), nullable=False)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())