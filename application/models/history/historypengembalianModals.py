from settings.queryFile import QueryStringDb


def getHistoryPengembalian():
    customQuery = QueryStringDb()
    query = '''         
        select 
            p.id as idpengembalian, b.id as idbuku , tanggalpengembalian, a.nama as namaanggota, j.nama as namabuku ,  to_char(denda, 'FM999G999G999G999G999D99') as denda, a.id as idanggota
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
        order by p.id desc
            '''
    kondisi = {

    }
    return customQuery.select(query, kondisi)
