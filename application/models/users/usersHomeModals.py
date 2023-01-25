from settings.queryFile import QueryStringDb


def getPeminjamanUser(id):
    customQuery = QueryStringDb()
    query = '''         
			select 
                idbuku as idbuku, j.nama as namabuku, a.id as nisanggota, a.nama as namaanggota, p.tanggalpeminjaman, p.bataspengembalian, p.bataspengembalian <= p.tanggalpeminjaman as statusDenda, p.bataspengembalian - p.tanggalpeminjaman as massapeminjamansebelumbataspengembalian
            from 
                peminjaman p 
            left join buku b 
                on p.idbuku = b.id 
            left join judulbuku j 
                on b.idjudulbuku  = j.id 	
            left join anggotaperpustakaan a 
                on p.idanggotaperpustakaan = a.id
            where 
                idanggotaperpustakaan =  %(id)s
                and flag = 1
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)
