def truncatetable( dbconn , tablname ):


   try:
      cursor = dbconn.cursor() 
      sqlstr = "TRUNCATE TABLE " + tablname + ";"
      cursor.execute(  sqlstr ) 
      dbconn.commit()
      cursor.close() 
      print( "Truncate success" )

   except:
      print( "Error!" )
      curcor.close()