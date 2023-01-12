from settings.queryFile import QueryStringDb


def getAllKategori():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from kategori ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def insertKategori(nama):
    customQuery = QueryStringDb()
    query = '''         
        insert into kategori (nama)
        values (%(nama)s)
            '''
    kondisi = {
        'nama': nama
    }
    return customQuery.execute(query, kondisi)


def updateKategori(id, nama):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE kategori  SET nama = %(nama)s WHERE id = %(id)s
            '''
    kondisi = {
        'nama': nama,
        'id': id
    }
    return customQuery.execute(query, kondisi)
