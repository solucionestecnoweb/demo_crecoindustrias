# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliverySicn(models.Model):
    _name = 'delivery.sicn'
    _description = 'Sicn'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    description = fields.Char(string='Descricción')