# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def default_get(self, default_fields):
        res = super(StockPicking, self).default_get(default_fields)
        if self.env.user.branch_id and self.env.user.branch_id.company_id.id == self.env.company.id:
            res['branch_id'] = self.env.user.branch_id.id
        elif self.env.user.branch_ids.ids:
            for i in self.env.user.branch_ids:
                if self.env.company.id == i.company_id.id:
                    res['branch_id'] = i.id
                    break
        return res

    branch_id = fields.Many2one('res.branch', string='Branch', domain="[('company_id', '=', company_id)]")
