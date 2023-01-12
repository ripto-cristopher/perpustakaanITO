from settings.queryFile import QueryStringDb


def getDate():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from anggotaperpustakaan ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)
