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
    sheet_id = "1A2C7oX5pcR_M1b375sCQVJZ0eschowzVBOMkf6sIr-8"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")

    carousel_tbl = dbs["carousel_db"]
    carousel_img = carousel_tbl.find()
    
    return render_template("home.html",myList = records, carousel_img = carousel_img)

@views.route('/aboutpgcc')
def aboutpgcc():
    return render_template("aboutpgcc.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/gallery')
def gallery():
    gallery_table = dbs["gallery_db"]
    gallery_img = gallery_table.find()
    return render_template("gallery.html" , gallery_img = gallery_img)



@views.route('/notice')
def notice():
    notice = dbs["notice_db"]
    notice_list = notice.find()
    return render_template("notice.html", noticeList = notice_list)


@views.route('/member')
def member():
    # sheet_id = "1mXpaO4rbj34uFdUpwVjltaIEYzaQ2rxgVg75d7qG3mE"
    # df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    # records = df.to_dict(orient="records")
    return render_template("member.html", memberList = {})

@views.route('/exec_committee')
def exec_committee():
    sheet_id = "1A2C7oX5pcR_M1b375sCQVJZ0eschowzVBOMkf6sIr-8"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    return render_template("executive_committee.html", myList = records)



@views.route('/tournament-summary')
def tournament_summary():
    sheet_id = "1PqVRcyl5Pp7RGXL-YbYOGwupG5jQEQACRokSjIl8dyw"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    records = df.to_dict(orient="records")
    
    return render_template("tournament_summary.html", myList = records)