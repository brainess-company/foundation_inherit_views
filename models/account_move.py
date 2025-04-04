# models/account_move.py
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    nome_obra = fields.Char(
        string='Nome da Obra',
        compute='_compute_nome_obra',
        store=False,
        readonly=True
    )

    @api.depends('invoice_origin', 'line_ids.sale_line_ids.order_id')
    def _compute_nome_obra(self):
        for move in self:
            sale_order = self.env['sale.order'].search([
                ('name', '=', move.invoice_origin)
            ], limit=1)
            move.nome_obra = sale_order.nome_obra if sale_order else False