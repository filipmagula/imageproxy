from flask import Flask, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/seismo_today.png')
def todays_image():
    today = datetime.now().strftime('%Y_%m_%d')
    url = f'http://czechgeo.ig.cas.cz/plotfiles/gfu/OKC/{today}.png'
    return redirect(url, code=302)

@app.route('/seismo_yesterday.png')
def yesterdays_image():
    yesterday = (datetime.now() - timedelta(1)).strftime('%Y_%m_%d')
    url = f'http://czechgeo.ig.cas.cz/plotfiles/gfu/OKC/{yesterday}.png'
    return redirect(url, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
