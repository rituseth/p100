class computer:
    def __init__(self,cardnumber,pin):
        self.pin=pin
        self.cardnumber=cardnumber
        print('cardnumber,pin')
    
    
    
    def balancenquiry(self):
        print('kya hain balance?')
        
        
    def cashen(self):
        print('kitna paisa hain')

cash=computer('pin','cardnumber')
cash.balancenquiry()


cash2=computer('pin','cardnumber')
cash2.cashen()