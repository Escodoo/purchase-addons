# Copyright 2023 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    requisition_id = fields.Many2one(
        "purchase.requisition",
        related="order_id.requisition_id",
        readonly=True,
        store=True,
    )
