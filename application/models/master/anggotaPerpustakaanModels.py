from settings.queryFile import QueryStringDb


def getAnggotaPerpustakaans():
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, nama, email, tanggallahir , kategori, to_char(totalDenda, 'FM999G999G999G999G999D99') as totalDenda
            from 
                anggotaperpustakaan a 
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def getAnggotaPerpustakaan(id):
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, nama, email, tanggallahir , kategori, to_char(totalDenda, 'FM999G999G999G999G999D99') as totalDenda
            from 
                anggotaperpustakaan a 
            where
                id = %(id)s
            '''
    kondisi = {
        "id" : id
    }
    return customQuery.select(query, kondisi)


