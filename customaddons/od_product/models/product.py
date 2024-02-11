from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    processor = fields.Char(string='computer processor')
