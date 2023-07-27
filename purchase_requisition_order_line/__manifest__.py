# Copyright 2023 - TODAY, Escodoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Requisition Order Line",
    "summary": """
        Adds the requisition_id field to the purchase order lines and adds an access
        link to these lines.""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Escodoo",
    "website": "https://github.com/Escodoo/purchase-addons",
    "depends": [
        "purchase_requisition",
    ],
    "data": [
        "views/purchase_requisition.xml",
        "views/purchase_order_line.xml",
    ],
    "demo": [],
}
