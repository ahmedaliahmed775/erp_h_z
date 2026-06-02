from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Override default name display
    def _get_default_favicon(self):
        """Return custom favicon instead of Odoo default"""
        return False
