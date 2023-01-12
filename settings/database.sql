-- id diambil dari nisn jika siswa, NUPTK (Nomor Unik Pendidik dan Tenaga Kependidikan) jika staf atau tenaga pengajar, idanggotaperpustakaan berguna juga untuk login
-- email untuk pengiriman pemberintahuan (dibuat jika memungkinkan)
-- status = { 'aktif', 'tidak aktif'}, aktif jika anggota perpustakaan masih dalam organisasi, tidak aktif jika telah keluar dari organisasi (lulus, pindah, atau dikeluarkan)
-- kategori = { 'guru', 'siswa'}
-- password dalam bentuk hash 256 

create table anggotaperpustakaan (
id int primary key not NULL,
nama VARCHAR ( 50 ) NOT NULL,
email VARCHAR ( 50 ) UNIQUE NOT NULL,
status Varchar (20) not null,
kategori varchar (20) not null,
password varchar (100) NOT NULL 
)

create table penerbit (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table pengarang (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table kategori (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table buku (
id BIGSERIAL  primary key not NULL,
idpenerbit BIGINT REFERENCES penerbit (id),
idpengarang BIGINT REFERENCES pengarang (id),
idkategori BIGINT REFERENCES kategori (id),
nama varchar (100) not null,
tahunTerbit int not null
)

-- status = {'hilang', 'rusak', 'perbaikan','tersedia', 'dipinjma'}

create table subBuku (
id BIGSERIAL  primary key not NULL,
idbuku BIGINT REFERENCES buku (id),
status Varchar (20) not null,
tanggalMasuk date not null
)

create table admin (
id BIGSERIAL  primary key not NULL,
username Varchar (50) unique not null,
nama Varchar (50) not null,
password varchar (100) NOT NULL 

)


create table peminjaman (
id BIGSERIAL  primary key not NULL,
idsubbuku BIGINT REFERENCES subbuku (id),
idadmin BIGINT REFERENCES admin (id),
idanggotaperpustakaan bigint REFERENCES anggotaperpustakaan (id),
tanggalpeminjaman date not null,
bataspengembalian date not null
)

create table pengembalian (
id BIGSERIAL primary key not NULL,
idsubbuku BIGINT REFERENCES peminjaman (id),
tanggalpengembalian date not null,
denda int
)
