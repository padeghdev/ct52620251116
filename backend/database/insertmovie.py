from backend.database.inserttable import inserttable

def insertmovies( connstr  , tablename ,  datainsert  ):

   try:

 


      tablename  = "movies" 

      fieldnames =  ( "mid" , "m_name" , "release_date" , "genre" , "country" , "imagename"  )

      inserttable ( connstr , tablename , fieldnames , datainsert  )
             
 
   
      print( "Data are inserted successfully" )
   
   except:
      print( "Insert Operation Error")
 

 






 