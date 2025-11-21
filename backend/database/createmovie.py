def createmovies( dbconn , createstr  ):
        try:
                cursor = dbconn.cursor() 
                cursor.execute( createstr ) 
                dbconn.commit()
                cursor.close() 
                print ( "Table created" )

        except:
                print ( "Error !" )
                cursor.close() 