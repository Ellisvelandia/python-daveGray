from bank_accounts import *

Ellis = BankAccount(1000, "Ellis")
Sara = BankAccount(2000, "Sara")

Ellis.getBalance()
Sara.getBalance()

Sara.deposit(500)

Ellis.withdraw(10000)

Ellis.transfer(100000000, Sara)
Ellis.transfer(100, Sara)

Jim = InteresRewardsAcct(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Ellis)

Blaze = SavingAcct(1000 , "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(100, Sara)