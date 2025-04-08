class PaymentPlan:

    def __init__(self, country, code):
        self.country = country
        self.code = code

    def describe_payment_plan(self):
        return f'Payment plan: country: {self.country}, code: {self.code}'