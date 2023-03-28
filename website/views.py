from flask import Blueprint, render_template
import pymongo
from pymongo import MongoClient
import pandas as pd


views = Blueprint('views', __name__)

 #Setup Mongo
client = MongoClient("mongodb+srv://shahin_shuvo:Shuvo919671@cluster0.wr8gao3.mongodb.net/?retryWrites=true&w=majority")
dbs = client["pgc_db"]


@views.route('/')
def home():
    # For committe data
    sheet_id = "1A2C7oX5pcR_M1b375sCQVJZ0eschowzVBOMkf6sIr-8"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")

    # For image link
    sheet_id = "1BrbDXdeZTQqZOJ9NdiR_FFoyIxN2VbpxOGImm-N-tW8"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    carousel_img = df.to_dict(orient="records")
    # print(carousel_img)
    return render_template("home.html",myList = records, carousel_img = carousel_img)

@views.route('/aboutpgcc')
def aboutpgcc():
    return render_template("aboutpgcc.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/gallery')
def gallery():
    sheet_id="1lNBpItZy8wBb7eJvPg1uGTVaTayFfnx7QSTn5fYkCjI"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    return render_template("gallery.html" , gallery_img = records)



@views.route('/notice')
def notice():
    sheet_id = "1AQY2AjiYRo6R3LOkEj5Imp1CEeyDAMZT5Kovv_OQKKM"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    return render_template("notice.html", noticeList = records)


@views.route('/membership')
def membership():
    sheet_id = "1mXpaO4rbj34uFdUpwVjltaIEYzaQ2rxgVg75d7qG3mE"
    gid = "1654696814"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    records = df.to_dict(orient="records")
    return render_template("member.html", memberList = records)

@views.route('/subscription')
def subscription():
    sheet_id = "1mXpaO4rbj34uFdUpwVjltaIEYzaQ2rxgVg75d7qG3mE"
    gid = "0"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    records = df.to_dict(orient="records")

    gid = "1058097752"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    TempMemFee = df.to_dict(orient="records")

    gid = "562291024"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    CorpMemFee = df.to_dict(orient="records")
    return render_template("subscription.html", FullMemFee = records, TmpFee = TempMemFee, CorpFee = CorpMemFee)

@views.route('/exec_committee')
def exec_committee():
    sheet_id = "1A2C7oX5pcR_M1b375sCQVJZ0eschowzVBOMkf6sIr-8"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    return render_template("executive_committee.html", myList = records)



@views.route('/tournament-summary')
def tournament_summary():
    sheet_id = "1PqVRcyl5Pp7RGXL-YbYOGwupG5jQEQACRokSjIl8dyw"
    sheet_name = "Sheet1"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    
    return render_template("tournament_summary.html", myList = records)


@views.route('/result')
def result():

    sheet_id = "1PqVRcyl5Pp7RGXL-YbYOGwupG5jQEQACRokSjIl8dyw"
    sheet_name = "Sheet1"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    last_item = ""
    for x in records:
        last_item = x["Name of Tournament"]
    print(last_item)
    sheet_id = "1PqVRcyl5Pp7RGXL-YbYOGwupG5jQEQACRokSjIl8dyw"
    gid = "20053265"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    records = df.to_dict(orient="records")
   
    return render_template("result.html", myList = records, t_name = last_item)


@views.route('/guest-room')
def guest_room():
    sheet_id = "1BrbDXdeZTQqZOJ9NdiR_FFoyIxN2VbpxOGImm-N-tW8"
    gid = "1668208811"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    records = df.to_dict(orient="records")
   
    return render_template("guestroom.html", room_img = records)
   
  
@views.route('/upcoming-event')
def upcoming_event():
    sheet_id = "1AQY2AjiYRo6R3LOkEj5Imp1CEeyDAMZT5Kovv_OQKKM"
    gid = "1115812265"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}")
    records = df.to_dict(orient="records")
    
    return render_template("/upcoming-event.html", records= records)

@views.route('/golf-driving')
def golf_driving():
    return render_template("/golf-driving.html")

@views.route('/caddies')
def caddies():
    return render_template("/caddies.html")
