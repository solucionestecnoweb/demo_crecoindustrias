# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    
    _inherit = 'account.move'

    route_id = fields.Many2one('delivery.route',string='RUTA')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    prueba = fields.Char(string='Prueba', store=True)