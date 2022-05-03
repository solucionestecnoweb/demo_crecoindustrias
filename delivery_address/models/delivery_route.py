# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliveryRoute(models.Model):
    _name = 'delivery.route'
    _description = 'Ruta destino'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    description = fields.Char(string='Descricción')