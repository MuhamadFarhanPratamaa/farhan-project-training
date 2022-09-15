from email.policy import default
from odoo import api, fields, models


class Pembayaran(models.Model):
    _name = 'farhanfutsal.pembayaran'
    _description = 'New Description'

    id_pembayaran = fields.Char(string='Id Pembayaran')
    name = fields.Char(string='Nama Pelanggan')
    tgl_bayar = fields.Datetime(string='Tanggal Bayar', default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar',string='Total Bayar')
    detailpembayaran_ids = fields.One2many(
                    comodel_name='farhanfutsal.detailpembayaran', 
                    inverse_name='pembayaran_id', 
                    string='Detail Pembayaran')
    
    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default='draft')

    @api.depends('nama_pelanggan')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.nama_pelanggan.id_member

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})
        
    
    @api.depends('detailpembayaran_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['farhanfutsal.detailpembayaran'].search([('pembayaran_id', '=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a


class DetailPembayaran(models.Model):
    _name = 'farhanfutsal.detailpembayaran'
    _description = 'New Description'

    name = fields.Char(string='Name')
    pembayaran_id = fields.Many2one(comodel_name='farhanfutsal.pembayaran', string='Detail Pembayaran')
    lapangan_id = fields.Many2one(comodel_name='farhanfutsal.lapangan', string='List Sewa')
    harga_sewa = fields.Integer(string='Harga Sewa')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_sewa')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.harga_sewa
    
    @api.onchange('lapangan_id')
    def _onchange_lapangan_id(self):
        if (self.lapangan_id.biaya_sewa):
            self.harga_sewa = self.lapangan_id.biaya_sewa
    
    
    

    
    
    
