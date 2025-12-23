from odoo import models, fields, api

class CostConfirmationWizard(models.TransientModel):
    _name = 'cost.confirmation.wizard'
    _description = 'Confirmação de Custo Suspeito'

    message = fields.Html(readonly=True)
    purchase_id = fields.Many2one('purchase.order')

    def action_confirm(self):
        return self.purchase_id.with_context(skip_cost_check=True).button_confirm()