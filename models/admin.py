class Admin:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.plans_crees = []

    def valider_souscription(self, souscription):
        souscription.statut = "validee"
        print(f"{self.nom} a validé la souscription de {souscription.client.nom}")

    def ajouter_plan(self, plan):
        self.plans_crees.append(plan)
        print(f"{self.nom} a ajoute le plan {plan.titre}")
