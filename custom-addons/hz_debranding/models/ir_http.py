from odoo import models, api


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @api.model
    def _get_content_common(self, xmlid=None, model='ir.attachment',
                            res_id=None, field='datas', unique=False,
                            filename=None, filename_field='name',
                            download=None, mimetype=None,
                            access_token=None, token=None):
        """Override to replace Odoo references in served content"""
        return super()._get_content_common(
            xmlid=xmlid, model=model, res_id=res_id, field=field,
            unique=unique, filename=filename,
            filename_field=filename_field, download=download,
            mimetype=mimetype, access_token=access_token, token=token
        )
