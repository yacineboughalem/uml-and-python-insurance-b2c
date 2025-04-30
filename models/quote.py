class Quote:
    def __init__(self, client, plan, estimation):
        self.client = client
        self.plan = plan
        self.estimation = estimation

    def afficher(self):
        print(f"Devis genere pour {self.client.nom} - Plan: {self.plan.titre}, Estimation: {self.estimation} MAD")

