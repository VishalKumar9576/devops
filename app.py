from flask import Flask
app=Flask(_name_)
@app.route('/home')
def home():
     return"hlo bhai"
if _name=='main_':
   app.run()