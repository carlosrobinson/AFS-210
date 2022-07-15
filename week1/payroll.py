class Employee:
    def __init__(
                self, emplyeeID = input("Please enter the Employee's ID: "), 
                fName = input("Please enter the Employee's First Name: "), 
                lName = input("Please enter the Employee's Last Name: "),  
                hrlyPay = input("Please enter the Employee's Hourly Pay Rate: "
                )):
        """Describes an employee and their payscale"""
        self.emplyeeID = emplyeeID
        self.fName = fName
        self.lName = lName
        self.hrlyPay = hrlyPay


    def pay(self):
        weeklyPay = 0
        hoursWorked = input(f"How many hours did {self.fName} work this week? ")
        # Hours Greater than 40
        if float(hoursWorked) > 40:
            weeklyPay += (float(self.hrlyPay) * 1.5) * (float(hoursWorked) - 40 ) + (40 * float(self.hrlyPay))
            round_weeklyPay = round(weeklyPay, 2)
            pay_check = '{:,.2f}'.format(round_weeklyPay)
            return f"{self.fName} {self.lName}'s paycheck amount is ${pay_check}"
        # Hours Less than or Equal to 40
        elif float(hoursWorked) <= 40:
            weeklyPay += float(self.hrlyPay) * float(hoursWorked)
            round_weeklyPay = round(weeklyPay, 2)
            pay_check = '{:,.2f}'.format(round_weeklyPay)
            return f"{self.fName} {self.lName}'s paycheck amount is ${pay_check}"


emplyee1 = Employee()
print(emplyee1.pay())