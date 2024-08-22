import requests
from datetime import date

today = date.today()
today_string = today.strftime('%Y-%m-%d')

url ="https://api.ycloud.com/v2/whatsapp/messages/sendDirectly"


order_number = 155501
track_id = "this_is_id"


headers={"X-API-Key": "386754f816783e4886c8bc7a99d14a0c" ,
"accept": "application/json" ,
"content-type": "application/json" 
}


def send_msg(lis):
    aa=lis[1]
    tracking_link=f"https://www.delhivery.com/track/package/{aa}"
    j = {
    "from": "+919821908015",
    "to": lis[0],
    "type": "template",
    "template": {

    "name": "moonord2",
    "language": {
      "code": "en"
    },
    "components": [
      {
        "type": "body",
       "parameters": [
          {
            "type": "text",
            "text": "45"
          },{
            "type": "text",
            "text": today_string
          },{
            "type": "text",
            "text": tracking_link
          }
        ]
      }
    ]
    }
   }
    res=requests.post(url,headers=headers,json=j)
    # print(res.content,res.status_code)
    print(res.status_code)

for i in range(1,100):
  ll=[]
  ll.append("+919899416045")
  ll.append(17979013576311)
  send_msg(ll)
    



