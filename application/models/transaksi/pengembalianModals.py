from settings.queryFile import QueryStringDb


def insertKembalikan(idBuku, denda, idadmin, idpeminjaman):
    customQuery = QueryStringDb()
    query = '''         
        insert into pengembalian  (idbuku,idpeminjaman, idadmin, denda )
        values (%(idBuku)s, %(idpeminjaman)s,%(idadmin)s, %(denda)s )
            '''
    kondisi = {
        'idBuku': idBuku,
        'denda': denda,
        'idadmin': idadmin,
        'idpeminjaman': idpeminjaman

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


def getIdpengembalian(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        select 
            id 
        from 
            peminjaman 
        where 
            flag = 1 
            and idbuku = %(idBuku)s
            '''
    kondisi = {
        'idBuku': idBuku

    }
    return customQuery.select(query, kondisi)
