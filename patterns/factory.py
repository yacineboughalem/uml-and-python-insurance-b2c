from models.plan import InsurancePlan

class InsurancePlanFactory:
    @staticmethod

    def create(plan_type: str) -> InsurancePlan:
       
        plans = {
            "basic": InsurancePlan("P01", "Plan Basic", 350),
            "standard": InsurancePlan("P02", "Plan Standard", 750),
            "premium": InsurancePlan("P03", "Plan Premium", 1200),
        }

        return plans.get(plan_type, plans["basic"])