from flask import Blueprint
from flask import render_template, session

from ATMflask import db
from ATMflask.sql import User

IS = Blueprint('IS',__name__)


@IS.route('/InquiryService',methods = ['GET','POST'])
def InquiryService():
    id = session.get('id')
    client = db.session.query(User).filter(User.id == id).first()
    return  render_template('InquiryService.html',username=client.username,balance=client.balance)
