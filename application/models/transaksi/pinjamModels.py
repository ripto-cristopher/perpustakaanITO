from settings.queryFile import QueryStringDb


def insertPeminjaman(idSubBuku, idAnggota, idadmin):
    customQuery = QueryStringDb()
    query = '''         
        insert into peminjaman (idsubbuku, idanggotaperpustakaan , idadmin, flag )
        values (%(idsubBuku)s, %(idAnggota)s, %(idadmin)s, %(flag)s)
            '''
    kondisi = {
        'idsubBuku': idSubBuku,
        'idAnggota': idAnggota,
        'idadmin': idadmin,
        'flag': 1   

    }
    print (query, kondisi)
    return customQuery.execute(query, kondisi)


def updateSubBukuStatus(id):
    customQuery = QueryStringDb()
    query = '''         
        update subbuku set 
 	        status = 'dipinjam'
        where id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.execute(query, kondisi)

