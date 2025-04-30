# > YACINE BOU-GHALEM <

# Projet B2C

Ce projet simule un système de souscription en ligne pour une assurance B2C, avec gestion des plans, devis, souscriptions, utilisateurs, et courtiers.

---

## Objectif du projet

- Permettre à un **client** de choisir un plan d'assurance, obtenir un **devis** et **souscrire**.
- Gérer les étapes métiers : **paiement**, **validation admin**, **suivi par un courtier**.
- Structurer un projet Python utilisant des **Design Patterns** avec des diagrammes UML détaillés.

---

## Explication rapide des patterns utilises

### `Factory Pattern`
- Classe : `InsurancePlanFactory`
- Objectif : creer des plans d'assurance dynamiquement (`basic`, `premium`, ....)

### `Strategy Pattern`
- Classe abstraite : `PricingStrategy`
- Implémentations : `DefaultPricing`, `DiscountPricing`
- Objectif : appliquer une strategie de calcul de prix..

### `Services`
- Classe : `SubscriptionService`
- Objectif : centraliser la logique metier (creation, paiement, validation de souscription..)

---

## Diagrammes UML

- `Use Case Diagram` : montre les reles (Client, Admin, Broker)
- `Class Diagram` : structure des entites avec relations et patterns
- `Activity Diagram` : parcours etape par étape du client
- `Sequence Diagram` : detail de l’interaction entre objets


