from flask import Blueprint, render_template
import pymongo
from pymongo import MongoClient

views = Blueprint('views', __name__)

 #Setup Mongo
client = MongoClient("mongodb+srv://shahin_shuvo:Shuvo919671@cluster0.wr8gao3.mongodb.net/?retryWrites=true&w=majority")
dbs = client["pgc_db"]


@views.route('/')
def home():
    table = dbs["executive_committee"]
    exec_comte = table.find()

    carousel_tbl = dbs["carousel_db"]
    carousel_img = carousel_tbl.find()
    
    return render_template("home.html",myList = exec_comte, carousel_img = carousel_img)

@views.route('/aboutpgc')
def aboutpgc():
    return render_template("aboutpgc.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/gallery')
def gallery():
    gallery_table = dbs["gallery_db"]
    gallery_img = gallery_table.find()
    return render_template("gallery.html" , gallery_img = gallery_img)

@views.route('/exec_committee')
def exec_committee():
   
    table = dbs["executive_committee"]
    exec_comte = table.find()
    return render_template("executive_committee.html", myList = exec_comte)

@views.route('/notice')
def notice():
    notice = dbs["notice_db"]
    notice_list = notice.find()
    return render_template("notice.html", noticeList = notice_list)