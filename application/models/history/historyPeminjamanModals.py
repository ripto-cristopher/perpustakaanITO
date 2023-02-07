from settings.queryFile import QueryStringDb


def getHistoryPengembalian():
    customQuery = QueryStringDb()
    query = '''         
        select idbuku as idbuku, j.nama as namabuku, a.id as nisanggota, a.nama as namaanggota, p.tanggalpeminjaman, p.bataspengembalian, p.flag from peminjaman p 
        left join buku b 
        on p.idbuku = b.id 
        left join judulbuku j 
        on b.idjudulbuku  = j.id 	
        left join anggotaperpustakaan a 
        on p.idanggotaperpustakaan = a.id 
        order by p.id desc
        
            '''
    kondisi = {
    }
    return customQuery.select(query, kondisi)


# where flag = 1
