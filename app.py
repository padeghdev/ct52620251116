from flask import Flask , render_template 
from backend.database.dbconnection import dbconn
from backend.database.selectmovies import selectmovies
 

app = Flask(__name__)

conn = dbconn()


@app.route("/")
def indexpage():

   sinfo = { 
      "topic" : "Assignment : Python Web show data from PostgreSQL" ,
      "name" : "นายเผด็จ แสงบุษราคัม" ,
      "code" : "รหัส : 68130039" ,
      "moviespage" : "แสดงรายชื่อภาพยนตร์" ,
      "urlmovie" : "/movies" 
 
   }
 

   return render_template("indexhome.html" ,  sinfo= sinfo )


@app.route("/movies")
def indexmovies():
    

   minfo = { 
   "topic" :  "รายชื่อภาพยนตร์",
   "moviespage" : "กลับไปหน้าแรก" ,
   "urlmovie" : "/" ,
   "headcolumns" :  [ "เลขที่", "ชื่อภาพยนตร์", "ปีที่ฉาย", "แนวภาพยนตร์", "ประเทศผู้สร้าง" , "ภาพ" ] 
      }
 
  
   movies = selectmovies( conn , "movies" )


   return render_template("indexmovies.html" ,  minfo=minfo , rows=movies )


 
if __name__ == "__main__":
   app.run(host='0.0.0.0' ,  port=80 ,debug=True)