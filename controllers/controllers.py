from odoo import http, models, fields
from odoo.http import request
import json

class farhanmart(http.Controller):
    @http.route('/farhanfutsal/getpelanggan', auth='public', method=['GET'])
    def getPelanggan(self, **kw):
        pelanggan = request.env['farhanfutsal.pelanggan'].search([])
        pel = []
        for s in pelanggan:
            pel.append({
                'nama_pelanggan' : s.name,
                'alamat' : s.alamat,
                'no_telpon' : s.no_telp,
                'barang' : s.sewalapangan_id[0].name
            })
        return json.dumps(pel)