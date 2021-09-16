from flask import Flask
import json
app=Flask(__name__)
user='''{
   "users":[
      {
         "id":"0",
         "isActive":true,
         "age":36,
         "name":"Dunlap Hubbard",
         "gender":"male",
         "company":"CEDWARD",
         "email":"dunlaphubbard@cedward.com",
         "phone":"+1 (890) 543-2508",
         "address":"169 Rutledge Street, Konterra, Northern Mariana Islands, 8551"
      },
      {
         "id":"1",
         "isActive":true,
         "age":24,
         "name":"Kirsten Sellers",
         "gender":"female",
         "company":"EMERGENT",
         "email":"kirstensellers@emergent.com",
         "phone":"+1 (831) 564-2190",
         "address":"886 Gallatin Place, Fannett, Arkansas, 4656"
      },
      {
         "id":"2",
         "isActive":true,
         "age":30,
         "name":"Acosta Robbins",
         "gender":"male",
         "company":"ORGANICA",
         "email":"acostarobbins@organica.com ",
         "phone":"+1 (882) 441-3367",
         "address":"697 Linden Boulevard, Sattley, Idaho, 1035"
      }
   ]
}
'''
info=json.loads(user)
@app.route("/")
def home():
    return "Hello!! Are ypu there????????"
@app.route("/users")
def get():
    return info['users']
@app.route("/users/<id>")
def get_id(id):
    for item in info['users']:
        if(item['id']==id):
            return item
def get():
    return info



if __name__=="__main__":
    app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)