from settings.queryFile import QueryStringDb


def getAllpengarang():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from pengarang ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def insertpengarang(nama):
    customQuery = QueryStringDb()
    query = '''         
        insert into pengarang (nama)
        values (%(nama)s)
            '''
    kondisi = {
        'nama': nama
    }
    return customQuery.execute(query, kondisi)


def updatepengarang(id, nama):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE pengarang  SET nama = %(nama)s WHERE id = %(id)s
            '''
    kondisi = {
        'nama': nama,
        'id': id
    }
    return customQuery.execute(query, kondisi)
