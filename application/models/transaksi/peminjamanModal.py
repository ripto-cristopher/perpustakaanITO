from settings.queryFile import QueryStringDb




def insertPeminjaman(idSubBuku, idAnggota, idadmin, idDenda, bataspengembalian):
    customQuery = QueryStringDb()
    query = '''  
        INSERT INTO peminjaman (idbuku, idadmin, iddenda, idanggotaperpustakaan, bataspengembalian, flag)
        values (%(idsubBuku)s, %(idadmin)s, %(idDenda)s,%(idAnggota)s, %(bataspengembalian)s, %(flag)s)
            '''
    kondisi = {
        'idsubBuku': idSubBuku,
        'idAnggota': idAnggota,
        'idadmin': idadmin,
        'idDenda': idDenda,
        'bataspengembalian': bataspengembalian,
        'flag': 1

    }
    print(query, kondisi)
    return customQuery.execute(query, kondisi)


def updateBukuStatus(id):
    customQuery = QueryStringDb()
    query = '''         
        update buku set 
 	        status = 'dipinjam'
        where id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.execute(query, kondisi)


def getDendaActivate():
    customQuery = QueryStringDb()
    query = '''         
        select 
            count(*) from denda d
        where
            activate = true 
            '''
    kondisi = {
    }
    return customQuery.select(query, kondisi)


def getDenda():
    customQuery = QueryStringDb()
    query = '''         
        select 
            id, lamapengembalian, activate, besardenda from denda d
        where
            activate = true 
            '''
    kondisi = {
    }
    return customQuery.select(query, kondisi)

