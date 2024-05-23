from odoo import models, fields, api


class project_project_inh(models.Model):
    _inherit = 'project.project'

    project_status = fields.Selection([
        ('active', 'Active'),
        ('closed', 'Closed'),
    ], string='Project Status',
        tracking=True,
        index=True,
        default="active",
    )

