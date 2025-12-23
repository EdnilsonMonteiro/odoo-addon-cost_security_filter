from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        if self.env.context.get('skip_cost_check'):
            return super(PurchaseOrder, self).button_confirm()

        lines_with_high_cost = []
        
        for line in self.order_line:
            current_cost = float(line.product_id.standard_price or 0.0)
            
            if current_cost > 0 and line.price_unit > (current_cost * 10):
                lines_with_high_cost.append(line)

        if lines_with_high_cost:
            msg = "<p>Os seguintes produtos excederam <b>10x</b> o custo configurado:</p><ul>"
            
            for line in lines_with_high_cost:
                current_cost = float(line.product_id.standard_price)
                msg += f"<li><b>{line.product_id.name}</b>:<br/>"
                msg += f"&nbsp;&nbsp;<b>Novo:</b> R$ {line.price_unit:.2f}<br/>"
                msg += f"&nbsp;&nbsp;vs<br/>"
                msg += f"&nbsp;&nbsp;<b>Antigo:</b> R$ {current_cost:.2f}</li><br/>"
            
            msg += "</ul><p>Deseja continuar com a confirmação?</p>"

            return {
                'name': 'Aviso de Preço Excessivo',
                'type': 'ir.actions.act_window',
                'res_model': 'cost.confirmation.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_message': msg,
                    'default_purchase_id': self.id,
                }
            }

        return super(PurchaseOrder, self).button_confirm()