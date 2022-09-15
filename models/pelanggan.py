from email.policy import default
from odoo import api, fields, models


class Pelanggan(models.Model):
    _name = 'farhanfutsal.pelanggan'
    _description = 'New Description'

    name = fields.Char(string='Nama Pelanggan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telepon')
    tgl_daftar = fields.Datetime(string='Tanggal Daftar', default = fields.Datetime.now())
    sewalapangan_id = fields.Many2many(comodel_name='farhanfutsal.sewalapangan', string='Sewa Lapangan')
    
    
    
    
    
