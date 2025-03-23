class BankApi:
    def verify_account(self,user):
        print(f"{user} is varified")

class PaymentGateway:
    def process_payment(self,amount):
        print(f"{amount} is processed")

class FraudCheck:
    def check_risk(self, user):
        print(f"Checking fraud risk for {user}")

class PaymentFacade:
    
    def __init__(self):
        self.BankApi = BankApi();
        self.PaymentGateway = PaymentGateway();
        self.FraudCheck = FraudCheck();

    def make_payment(self,user,amount):
        print("\n🔹 Initiating Payment Process...\n")
        self.BankApi.verify_account(user)
        self.FraudCheck.check_risk(user)
        self.PaymentGateway.process_payment(amount)
        print("\n✅ Payment Successful!\n")

if __name__=="__main__":
    payment = PaymentFacade()
    payment.make_payment("rahul",200000000)

