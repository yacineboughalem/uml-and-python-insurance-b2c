import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.subscription import Subscription
from models.quote import Quote
from services.notifierService import Notifier



class SubscriptionService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def creer_souscription_depuis_devis(self, quote: Quote):
        
        print("Creation de la souscription...")
        souscription = Subscription(quote.client, quote.plan, quote.estimation)

        return souscription

    def payer_souscription(self, souscription: Subscription):
        souscription.payer()

        self.notifier.envoyer(
            f"{souscription.client.nom} a paye le plan {souscription.plan.titre} pour {souscription.montant} MAD."
        )

    def confirmer_souscription(self, souscription: Subscription):
        print("Souscription confirmer pour " + {souscription.client.nom} + "(souscription.plan.titre)")
        print("Statut :"  + souscription.statut)
