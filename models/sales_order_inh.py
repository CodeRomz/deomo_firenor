from odoo import models, fields, api


class sales_order_inh(models.Model):
    _inherit = 'sales.order'

    project_reference = fields.Many2one('project.project', string='Project Reference')
    project_status = fields.Selection(related='project_reference.project_status')

