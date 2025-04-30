class Subscription:
    def __init__(self, client, plan, montant):
        self.client = client
        self.plan = plan
        self.montant = montant
        self.statut = "en attente"

    def payer(self):
        self.statut = "payee"