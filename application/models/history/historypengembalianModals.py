from settings.queryFile import QueryStringDb


def getHistoryPengembalian():
    customQuery = QueryStringDb()
    query = '''         
        select 
            p.id as idpengembalian, b.id as idbuku , tanggalpengembalian, a.nama as namaanggota, j.nama as namabuku , denda, a.id as idanggota
        from 
            pengembalian p
        left join peminjaman p2
            on p.idpeminjaman = p2.id
        left join anggotaperpustakaan a
            on p2.idanggotaperpustakaan = a.id
        left join buku b
            on p.idbuku = b.id
        left join judulbuku j
            on b.idjudulbuku = j.id
        order by p.id
            '''
    kondisi = {

    }
    return customQuery.select(query, kondisi)
