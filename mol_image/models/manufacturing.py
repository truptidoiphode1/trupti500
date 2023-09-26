# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MrpProduction(models.Model):

    _inherit = 'mrp.production'

    product_mo_image = fields.Binary('Product Image', related='product_id.image_1920')

class StockMove(models.Model):

    _inherit = 'stock.move'

    product_mo_image = fields.Binary('Product Image', related='product_id.image_1920')