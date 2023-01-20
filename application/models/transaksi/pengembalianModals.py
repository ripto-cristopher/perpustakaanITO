from settings.queryFile import QueryStringDb


def insertKembalikan(idBuku, denda, idadmin):
    customQuery = QueryStringDb()
    query = '''         
        insert into pengembalian  (idbuku, idadmin, denda )
        values (%(idBuku)s, %(idadmin)s, %(denda)s )
            '''
    kondisi = {
        'idBuku': idBuku,
        'denda': denda,
        'idadmin': idadmin

    }
    return customQuery.execute(query, kondisi)


def updateSubBukuStatus(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        update buku set 
 	        status = 'tersedia'
        where id = %(idBuku)s
            '''
    kondisi = {
        'idBuku': idBuku
    }
    return customQuery.execute(query, kondisi)


def updatePinjam(idBuku):
    customQuery = QueryStringDb()
    query = '''         
    update peminjaman set flag = 0
    where idbuku = %(idBuku)s and flag = 1 
            '''
    kondisi = {
        'idBuku': idBuku
    }
    return customQuery.execute(query, kondisi)

