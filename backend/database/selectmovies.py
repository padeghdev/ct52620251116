
def selectmovies( dbconn ,   tablename  ):
    try:
        cursor = dbconn.cursor()
        cursor.execute("SELECT * FROM " +   tablename  + " order by mid asc ;")
        movies = cursor.fetchall()
        cursor.close()
        #dbconn.close()
        return movies

    except:
        print( "Query Operation Error")
 








