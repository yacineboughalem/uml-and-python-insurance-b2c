from models.client import Client
from models.broker import Broker
from models.admin import Admin
from models.subscription import Subscription
from models.quote import Quote
from patterns.factory import InsurancePlanFactory
from patterns.strategy import DiscountPricing
from services.notifierService import Notifier
from services.subscriptionService import SubscriptionService

# Client
client = Client("Client-000001", "Yacine", "yacin.boughalem@mail.com")

# Select plan
plan = InsurancePlanFactory.create("premium")

# Remise 20% 
strategie = DiscountPricing(0.2)
prix_estime = strategie.calculer(plan.prix)

# devis
quote = Quote(client,plan, prix_estime)
quote.afficher()

# Notification et de souscription
notifier = Notifier()
subscription_service = SubscriptionService(notifier)

# paiement de la souscription a partir devis
souscription = subscription_service.creer_souscription_depuis_devis(quote)
subscription_service.payer_souscription(souscription)

# Admin : validation
admin = Admin("A01", "frontYnova")
admin.valider_souscription(souscription)

broker = Broker("Broker-00001", "Oussama Bg")
broker.affecter_client(client)
broker.suivre(souscription)

# Notification Recap
notifier.envoyer(
    f"✔ {client.nom} a souscrit au plan {plan.titre} pour {prix_estime} MAD. "
    f"Statut actuel : {souscription.statut}"
)

# Affichage
print("\n----- Recapitulatif de la souscription -----")
print(f"Client              : {client.nom}")
print(f"Plan                : {plan.titre}")
print(f"Montant paye        : {prix_estime} MAD")
print(f"Statut              : {souscription.statut}")
print(f"Statut              :{ souscription.statut}")
