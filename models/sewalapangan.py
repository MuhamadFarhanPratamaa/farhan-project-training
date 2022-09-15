from dataclasses import field
# from email.policy import default
# from addonsfutsal.farhanfutsal.models import lapangan
from odoo import api, fields, models

class SewaLapangan(models.Model):
    _name = 'farhanfutsal.sewalapangan'
    _description = 'New Description'

    name = fields.Char(string='Nama Lapangan')
    kode_lap = fields.Char(string='Kode Lapangan')
    tgl_booking = fields.Datetime(string='Tanggal Booking', default = fields.Datetime.now())
    dp = fields.Char(string='DP', required=True)

    lapangan_id = fields.Many2one(comodel_name='farhanfutsal.lapangan', 
                                    string='Nama Lapangan')
    pelanggan_id = fields.Many2many(comodel_name='farhanfutsal.pelanggan', 
                                    string='Pelanggan')