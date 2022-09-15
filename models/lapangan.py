from odoo import api, fields, models


class Lapangan(models.Model):
    _name = 'farhanfutsal.lapangan'
    _description = 'New Description'

    name = fields.Char(string='Nama Lapangan')
    kode_lap = fields.Char(string='Kode Lapangan')
    biaya_sewa = fields.Char(string='Biaya Sewa Lapangan', required=True)

    name = fields.Selection ( [
        ('lapangan a', 'Lapangan A'),
        ('lapangan b', 'Lapangan B'),
        ('lapangan c', 'Lapangan C')
    ], string= 'Nama Lapangan')

    @api.onchange('name')
    def _onchange_kode_lapangan(self) :
        if self.name == 'lapangan a' :
            self.kode_lap = 'LAP01'
        elif self.name == 'lapangan b':
            self.kode_lap = 'LAP02'
        elif self.name == 'lapangan c' :
            self.kode_lap = 'LAP03'

    sewalapangan_ids = fields.Many2one(comodel_name='farhanfutsal.sewalapangan', 
                                            string='sewa lapangan')