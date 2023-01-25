			# select
            #     b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit, (select count(*)  from buku s where  idJudulbuku = b.id and s.status = 'tersedia' ) as jumlahbukutersedia, (select count(*)  from buku s where  idJudulbuku = b.id) as jumlahBuku
            # from 
            #     judulbuku  b
            # left join penerbit p
            #     on b.idpenerbit  = p.id
            # left join pengarang p2  
            #     on b.idpengarang = p2.id
            # left join kategori k    
            #     on b.idkategori = k.id ;

from settings.queryFile import QueryStringDb


# def getAllJudulBukuAvaliable():
#     customQuery = QueryStringDb()
#     query = '''         
# 			select
#                 b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit, (select count(*)  from buku s where  idJudulbuku = b.id and s.status = 'tersedia' ) as jumlahbukutersedia, (select count(*)  from buku s where  idJudulbuku = b.id) as jumlahBuku
#             from 
#                 judulbuku  b
#             left join penerbit p
#                 on b.idpenerbit  = p.id
#             left join pengarang p2  
#                 on b.idpengarang = p2.id
#             left join kategori k    
#                 on b.idkategori = k.id ;
#             '''
#     kondisi = {}
#     return customQuery.select(query, kondisi)
