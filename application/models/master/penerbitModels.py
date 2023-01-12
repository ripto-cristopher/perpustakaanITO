from settings.queryFile import QueryStringDb


def getAllpenerbit():
    customQuery = QueryStringDb()
    query = '''         
            SELECT * from penerbit ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def insertpenerbit(nama):
    customQuery = QueryStringDb()
    query = '''         
        insert into penerbit (nama)
        values (%(nama)s)
            '''
    kondisi = {
        'nama': nama
    }
    return customQuery.execute(query, kondisi)


def updatepenerbit(id, nama):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE penerbit  SET nama = %(nama)s WHERE id = %(id)s
            '''
    kondisi = {
        'nama': nama,
        'id': id
    }
    return customQuery.execute(query, kondisi)
