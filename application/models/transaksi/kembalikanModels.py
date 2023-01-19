from settings.queryFile import QueryStringDb


def insertKembalikan(idSubBuku, denda, idadmin):
    customQuery = QueryStringDb()
    query = '''         
        insert into pengembalian  (idsubbuku, idadmin, denda )
        values (%(idsubBuku)s, %(idadmin)s, %(denda)s )
            '''
    kondisi = {
        'idsubBuku': idSubBuku,
        'denda': denda,
        'idadmin': idadmin

    }
    return customQuery.execute(query, kondisi)


def updateSubBukuStatus(idSubBuku):
    customQuery = QueryStringDb()
    query = '''         
        update subbuku set 
 	        status = 'tersedia'
        where id = %(idSubBuku)s
            '''
    kondisi = {
        'idSubBuku': idSubBuku
    }
    return customQuery.execute(query, kondisi)


def updatePinjam(idSubBuku):
    customQuery = QueryStringDb()
    query = '''         
    update peminjaman set flag = 0
    where idsubbuku = %(idSubBuku)s and flag = 1 
            '''
    kondisi = {
        'idSubBuku': idSubBuku
    }
    return customQuery.execute(query, kondisi)

