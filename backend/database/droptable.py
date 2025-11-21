def droptable( dbconn , tablname ):
   try: 
      cursor = dbconn.cursor() 
      sqlstr = "DROP TABLE IF EXISTS " + tablname + ";"
      cursor.execute(  sqlstr ) 
      dbconn.commit()
      cursor.close() 
      print( "No table existed" )

   except:
      print( "Error!" )
      curcor.close()

