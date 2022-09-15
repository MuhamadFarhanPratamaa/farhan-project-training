from odoo import api, fields, models

class addlapangan(models.TransientModel):
    _name = 'farhanfutsal.addlapangan'

    
    lapangan_id = fields.Many2one(
        string='Nama Lapangan',
        comodel_name='farhanfutsal.lapangan',
        required='False')
    
    
    kode_lap = fields.Char(
        string='Kode Lapangan',
        required='True')
    
    biaya_sewa = fields.Char(
        string='Biaya Sewa',
        required='True')
    
    def button_lapangan(self):
        pass