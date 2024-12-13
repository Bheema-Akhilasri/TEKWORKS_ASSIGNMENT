class Bank():

    accbal=10000
    num = 0
    def deposit(self):
        deposit_amount=int(input('Enter the deposit amount'))
        if (50000>=deposit_amount>=100) and (deposit_amount%100==0):
            obj.accbal = obj.accbal+deposit_amount
        else:
            print('Deposit amount should be between 100 and 50k')
    def withdraw(self):

        if(self.num<3):
            withdraw_amount = int(input('Enter the withdraw amount'))
            if (20000 >= withdraw_amount >= 100) and (withdraw_amount % 100 == 0) and (withdraw_amount < obj.accbal):
                if obj.accbal - withdraw_amount > 500:
                    obj.accbal = obj.accbal - withdraw_amount
                    self.num=self.num+1
                    if withdraw_amount>=500:
                        amount = withdraw_amount // 500
                        print('500 notes are ', amount)
                        withdraw_amount = withdraw_amount % 500
                    if withdraw_amount>=200:
                        amount = withdraw_amount // 200
                        print('200 notes are ', amount)
                        withdraw_amount = withdraw_amount % 200
                    if withdraw_amount>=100:
                        amount = withdraw_amount // 100
                        print('100 notes are ', amount)
                else:
                    print('Minimum balance will be less than 500')
            else:
                print('Withdraw amount should be min of 100 and max of 20k and should be less than account balance')
        else:
            print('Number of Transactions per day is only 3')

    def validation(self):
        n=0
        while n<3:
            pin = int(input('Enter the pin '))
            if pin == 1234:
                obj.view_option()
                return
            else:
                print('Invalid pin')
                n=n+1
        print('Try after sometime')
    def view_option(self):
        n=0
        while(n<4):
            print('1.Deposit\n2.Withdraw\n3.Bal Enquiry\n0.Exit\n')
            option=int(input('Choose your option '))
            match option:
                case 1:
                    obj.deposit()
                case 2:
                    obj.withdraw()
                case 3:
                    print(obj.accbal)
                case 0:
                    exit(0)



obj=Bank()
obj.validation()
