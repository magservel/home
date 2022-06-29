import requests
import datetime
from flask import Flask, render_template, request, redirect, url_for
from core.dico import get_entries, create_entry, set_entry

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/dico", methods=['GET'])
def dico():
    entries = get_entries()
    print("fd")
    return render_template("dico.html", entries=entries)


@app.route("/dico/newentry", methods=['POST'])
def dico_newentry():
    ang = request.form.get('ang')
    fra = request.form.get('fra')
    error, msg = create_entry(ang, fra)
    return redirect(url_for("dico"))


@app.route("/dico/setentry", methods=['POST'])
def dico_setentry():
    ang = request.form.get('ang')
    fra = request.form.get('fra')
    error, msg = set_entry(ang, fra)
    return redirect(url_for("dico"))


# @app.route("/crypto")
# def crypto():
#     today = int(datetime.datetime.now().timestamp())
#     start = str(today - 604800)  # 1 week
#     end = str(today)
#     period = str(900)  # 15 minutes
#     url_btc = "https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&" \
#               "start=" + start + "&end=" + end + "&period=" + period
#
#     api_data = requests.get(url_btc)
#     data = api_data.json()
#     print(type(data[0]['open']))
#     return render_template("crypto.html", data=data)



