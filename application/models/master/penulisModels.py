from settings.queryFile import QueryStringDb


def getAllpenulis():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from pengarang ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def insertpenulis(nama):
    customQuery = QueryStringDb()
    query = '''         
        insert into pengarang (nama)
        values (%(nama)s)
            '''
    kondisi = {
        'nama': nama
    }
    return customQuery.execute(query, kondisi)


def updatepenulis(id, nama):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE pengarang  SET nama = %(nama)s WHERE id = %(id)s
            '''
    kondisi = {
        'nama': nama,
        'id': id
    }
    return customQuery.execute(query, kondisi)
