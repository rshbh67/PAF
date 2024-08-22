# http://164.90.152.44:6556
from flask import Flask, url_for ,request , jsonify ,send_file , render_template , redirect ,session , flash

from datetime import date , datetime , timedelta

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pytz




utc_now = datetime.utcnow()

# Convert UTC time to Indian Standard Time (IST)
ist = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.astimezone(ist)

# Add 5 hours and 30 minutes
ist_later = ist_now + timedelta(hours=5, minutes=30)


date_in_indian_format = ist_now.strftime('%d-%m-%Y')
time_in_indian_format = ist_now.strftime('%H:%M:%S')



cred = credentials.Certificate(r'C:/Users/risha/OneDrive/Desktop/linux_downloads/downloads/firebase/rishabh34-9a7b1-firebase-adminsdk-ljeri-642e197008.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

today = date.today()
today_string = today.strftime('%Y-%m-%d')

app = Flask(__name__)
app.secret_key="hello"


# @app.route('/ll' , methods=['GET' , 'POST'])
# def sign():
#     if request.method == 'POST':
#          if 'name' in session:
#              session.pop('name',None)
#              session.pop('pass',None)

#          name = request.form['name']
#          pasd = request.form['pass']
#          query = db.collection('user_logins').where('name', '==',name)
#          res={}
#          print(name, pasd)
#          for doc in query.stream():
#            res = doc.to_dict()
#            print(res)

#          if 'name' in res:
         
#           if res['pass'] == pasd:
             
#              flash('successfully sign in !! ')
#              session['name'] = name
#              session['pass'] = pasd
#              return redirect(url_for('net_form'))
#           else:
#              flash('No UserName found !!! ')
#              return redirect(url_for('sign'))

             
#          else:
#             flash('Wrong password !!!')
#             return redirect(url_for('sign'))


#     return render_template('sign.html')


@app.route('/' ,methods=['GET' , 'POST'])
def login():
   return render_template("home.html")




@app.route('/getpdf/<pdf>' , methods=['GET'])
def getpdf(pdf):
    new_pdf = send_file(pdf, as_attachment=True)
    return new_pdf





# @app.route('/find', methods=['GET' , 'POST'])
# def find():
#    if request.method == "POST":
#       data = request.json
#       phone = data["number"]
#       print(phone)
#       query = db.collection('pdfs-data').where('cust_phone', '==',phone)
#       res={}
#       for doc in query.stream():
#         res = doc.to_dict()

#       session['customer'] = res  
#       print(res)
#       if 'maindata' in res:
#          print('not found')
#          return "true"
#       else:
#          flash('Number not found !!!')
#          return "not"

      
     
#    return render_template("find.html")





# @app.route('/click')
# def click():
#     models = []
#     docs = db.collection('pdfs-data').stream()
#     for doc in docs:
#         res = {}
#         res["name"] = doc.get('name')
#         res['date'] = doc.get('date')
#         res['time'] = doc.get('time')
#         res['Generated_by'] = doc.get('Generated_by')
#         res['Generated_mail'] = doc.get('Generated_mail')


#         models.append(res)
    
#     return render_template("click.html", data=models)






# @app.route('/send', methods=['GET', 'POST'])
# def send():
#    if request.method == "POST":
#       data = request.json
#       lis = []
#       phone  = "+91"+str(data['number'])
#       lis.append(phone)
#       lis.append(data['awb'])
#       print(lis)
#       whats_res = sending.send_msg(lis)
#       print(whats_res)
#       return "sent"


#     #   whats_res = sending.send_msg()
      
#    return render_template("send.html")




if __name__ == "__main__":
    app.run(port=6556 , host="0.0.0.0" , debug=True)




# query = db.collection('taskCollection').where('age', '>=',40)

# print(type(query))



# Iterate over the results and print them
# for doc in query.stream():
#     print(f'{doc.id} => {doc.to_dict()}')
