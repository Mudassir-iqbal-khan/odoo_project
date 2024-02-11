from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor', default=False)
    session_ids = fields.Many2many('od_openacademy.session', string='Attended Sessions')
