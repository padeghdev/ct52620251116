
def inserttable ( connstr , tablename , fieldnames , datainsert  ):

   try:

      cursor = connstr.cursor()

      qty =  len (   fieldnames ) 
      #print ( qty )

      result = " %s" 
      for i in range ( qty -1):
         #print ( i )
         result += ", %s" 

      #print ( qty )    


      mixfn = fieldnames[0]  
      for i in range ( qty-1 ):
         mixfn +=  " , "  + fieldnames[i+1]  
      #print (mixfn)    



      sql = ""
      sql += "INSERT INTO " 
      sql +=  tablename  + " ( " 
      sql +=  mixfn
      sql +=  " ) " 
      sql += "VALUES (" 
      sql +=  result 
      sql +=  " ) " 
      sql +=  "" 

      print (sql)

      print (datainsert )
    
 
      
      '''
      sql = "INSERT INTO test ( column1, column2 , column3 ) VALUES (%s , %s, %s ) ;" 
      val = ( datainsert[0], datainsert[1] , datainsert[2] )

      '''

      
      cursor.execute( sql ,  datainsert  ) 
      connstr.commit()

      #cursor.close()

      print( "Data are inserted successfully" )
   
   except:
      print( "Insert Operation Error 2")
      # dbconn.rollback


