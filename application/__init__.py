
from flask import Flask


app = Flask(__name__)
app.secret_key = '5up3r 53cr3t'

# controller
from application.controllers.transaksi.Pengembalian import *
from application.controllers.transaksi.peminjaman import *
from application.controllers.master.buku import *
from application.controllers.master.judulBuku import *
from application.controllers.master.anggotaPerpustakaan import *
from application.controllers.master.pengarang import *
from application.controllers.master.penerbit import *
from application.controllers.master.kategori import *
from application.controllers.master.denda import *
from application.controllers.history.historyPeminjaman import *
from application.controllers.history.historyPengembalian import *
from application.controllers.users.users import *
from application.controllers.auth import *
from application.controllers.index import *