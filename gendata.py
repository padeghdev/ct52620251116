#from flask import Flask , render_template 

from backend.database.dbconnection import dbconn
from backend.database.selectmovies import selectmovies
from backend.database.insertmovie import insertmovies
 
from backend.database.createmovie import createmovies
from backend.database.droptable import droptable
from backend.database.truncatetable import truncatetable


## function สำหรับทำการ สร้าง table ใหม่   

''' 
conn = dbconn()
createstr = "CREATE TABLE IF NOT EXISTS movies ( "  
createstr += " mid int primary key, m_name varchar(255), release_date varchar(10),"
createstr += " genre varchar(100), country varchar(100) , imagename varchar (255)"
createstr += " ) ; "  
createmovies( conn , createstr ) 
 '''

 
## function สำหรับทำการ ลบ ทั้ง ข้อมูล และ โครงสร้าง ของ table  

''' 
conn = dbconn()
droptable( conn , "movies" ) 
'''



## function สำหรับทำการ Truncate ข้อมูล โดยจะ ลบ เฉพาะข้อมูลในตาราง เท่านั้น โดยที่ โครงสรา้งของตารางจะยังคงเดิม

''' 
 
conn = dbconn()
truncatetable( conn , "movies") 
 
 '''
 

 
## function สำหรับทำการ insert ข้อมูล เข้าสู่ฐานชข้อมูล 

''' 

conn = dbconn()
tablename = "movies"
movdata = []
movdata.append([ 1 , 'GHOST' , '1990' , 'Romantic' , 'USA'  , 'ghost.jpg'  ] )
movdata.append([ 2 , 'Frankenstein' , '2025' , 'Gothic science fiction drama' , 'USA' , 'frankenstein.png'   ] )
movdata.append([ 3 , 'Predator: Badlands' , '2025' , 'Science fiction action film' , 'USA' , 'predator.jpg' ] )
movdata.append([ 4 , 'Avatar: Fire and Ash' , '2025' , 'epic science fiction film' , 'USA' , 'avartar.jpg' ] )
movdata.append([ 5 , 'บุญชูผู้น่ารัก' , '1988' , 'comedy' , 'THAILAND'  , 'boonchou1.jpg'] )


for md in movdata :
    insertmovies(conn, tablename , md  )  
 
 '''
 ## function สำหรับทำการ query ข้อมูล 

''' 
conn = dbconn()

tablename = "movies"
movies = selectmovies( conn , tablename )
for movie in movies:
   print( movie )

 '''

 


