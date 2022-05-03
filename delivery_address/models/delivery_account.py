# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _ 
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger('__name__')


class AccountMove(models.Model):
    
    _inherit = 'account.move'

    route_id = fields.Many2one('delivery.route',string='RUTA')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    prueba = fields.Selection([('a', 'A'),('b', 'B')])