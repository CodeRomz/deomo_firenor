from odoo import models, fields, api


class sales_order_inh(models.Model):
    _inherit = 'sale.order'

    inh_project_reference = fields.Many2one('project.project', string='Project Reference')
    inh_project_status = fields.Selection(related='inh_project_reference.inh_project_status')


