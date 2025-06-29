from flask import request, jsonify, render_template
from app import app, db
from app.models import Candle
import pandas as pd
import plotly.graph_objs as go

@app.route('/')
def index():
    candles = Candle.query.filter_by(symbol='GBPUSD').limit(100).all()
    df = pd.DataFrame([(c.open, c.high, c.low, c.close) for c in candles], 
                      columns=['open', 'high', 'low', 'close'])
    
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'])])
    
    return render_template('index.html', plot=fig.to_html())

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    candle = Candle(
        symbol=data.get('symbol'),
        timeframe=data.get('timeframe'),
        open=data.get('open'),
        high=data.get('high'),
        low=data.get('low'),
        close=data.get('close')
    )
    db.session.add(candle)
    db.session.commit()
    return jsonify({'status': 'success'})