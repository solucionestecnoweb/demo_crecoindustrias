# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    
    _inherit = 'res.partner'

    sicn_id = fields.Many2one('delivery.sicn',string='SICN')