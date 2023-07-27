# Copyright 2023 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseRequisition(models.Model):

    _inherit = "purchase.requisition"

    order_line_count = fields.Integer(
        compute="_compute_orders_lines_number", string="Number of Orders Lines"
    )

    @api.depends("purchase_ids")
    def _compute_orders_lines_number(self):
        for requisition in self:
            requisition.order_line_count = len(requisition.purchase_ids.order_line)
