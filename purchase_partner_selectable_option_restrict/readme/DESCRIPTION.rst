This module restricts the visibility of the *Selectable in orders*
(``purchase_selectable``) field on the partner form, so that only users
belonging to the *Purchase / Manager* group can see and edit it.

It extends ``purchase_partner_selectable_option`` and keeps the field
loaded (invisible) for other users so that the purchase-related button
visibility rules on the partner form continue to work correctly.
