TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

tariff = input("Which tariff? 11 or 31: ")
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))

if tariff == 11:
    estimated_bill = TARIFF_11 * daily_use_in_kWh * number_of_billing_days
    print("Estimated bill: ${}".format(estimated_bill))
elif tariff == 31:
    estimated_bill = TARIFF_31 * daily_use_in_kWh * number_of_billing_days
    print("Estimated bill: ${}".format(estimated_bill))
