class PricingStrategy:
    def calculer(self, montant: float) -> float:
        return montant

class DefaultPricing(PricingStrategy):
    def calculer(self, montant: float) -> float:
        return montant



class DiscountPricing(PricingStrategy):
    def __init__(self, remise: float):
        self.remise = remise

    def calculer(self, montant: float) -> float:
        return montant * (1 - self.remise)