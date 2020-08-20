def presentation():
    print("Payment Calculator")


def payment_calculator(worked_hours, value_hour):
    if worked_hours <= 0 or value_hour <= 0:
        print("Invalid values, please type again.")
        return 0
    else:
        return worked_hours * value_hour


presentation()
payment_value = 0

while payment_value == 0:
    worked_hours = int(input("How many hours did you work?: "))
    value_hour = int(input("Hourly rate: "))
    payment_value = payment_calculator(worked_hours, value_hour)

print("Your payment will be: ${}".format(payment_value))
