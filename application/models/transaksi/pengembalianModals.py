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
    print (query, kondisi)
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


def getpeminjaman(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        select 
            p.id, lamapengembalian, bataspengembalian, besardenda, idanggotaperpustakaan
        from 
            peminjaman p
        left join denda d 
        on p.iddenda= d.id
        where 
        flag = 1 
        and idbuku = %(idBuku)s
            '''
    kondisi = {
        'idBuku': idBuku

    }
    return customQuery.select(query, kondisi)


def getTotalDendaAnggotaPerpustakaan(idAnggotaPerpustakaan):
    customQuery = QueryStringDb()
    query = '''         
        select 
            totaldenda from anggotaperpustakaan a 
        where 
            id =  %(idAnggotaPerpustakaan)s
                    '''
    kondisi = {
        'idAnggotaPerpustakaan': idAnggotaPerpustakaan
    }
    return customQuery.select(query, kondisi)


def updateDendaAnggotaPerpustakaan(idAnggotaPerpustakaan, totalDenda):
    customQuery = QueryStringDb()
    query = '''         
        UPDATE anggotaperpustakaan
        SET totalDenda = %(totalDenda)s
        where 
            id =  %(idAnggotaPerpustakaan)s
                    '''
    kondisi = {
        'idAnggotaPerpustakaan': idAnggotaPerpustakaan,
        'totalDenda': totalDenda
    }
    return customQuery.execute(query, kondisi)


def getDataPeminjaman(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        select 
            a.nama as namaanggota, j.nama as namabuku
        from 
            peminjaman p
        left join denda d 
        on p.iddenda= d.id
        left join anggotaperpustakaan a 
        on p.idanggotaperpustakaan  = a.id 
        left join buku b   
        on p.idbuku  = b.id 
        left join judulbuku j    
        on b.idjudulbuku  = j.id 
        where 
        flag = 1 
        and idbuku =  %(idBuku)s
            '''
    kondisi = {
        'idBuku': idBuku

    }
    return customQuery.select(query, kondisi)
