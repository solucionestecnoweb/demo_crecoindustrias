# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'

    route_id = fields.Many2one('delivery.route',string='RUTA')