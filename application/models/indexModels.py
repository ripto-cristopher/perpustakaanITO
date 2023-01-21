from settings.queryFile import QueryStringDb


def getDate():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from anggotaperpustakaan ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)

    
def getjumlahanggota():
    customQuery = QueryStringDb()
    query = '''         
            select count(*)  from anggotaperpustakaan a;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)

def getjumlahbuku():
    customQuery = QueryStringDb()
    query = '''         
            select count(*)  from buku b;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)