# QAP 5, Jacob Jesso

# Imports

import datetime

def add_month(date, add):
    CurrentMonth = date.month
    NextMonth = CurrentMonth + add
    if NextMonth > 12:
        NextMonth = NextMonth - 12
    return NextMonth

f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline())
BASE_RATE = float(f.readline())
ADD_DISC_RATE = float(f.readline())
ADD_LIB_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOAN_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

while True:
    try:
        CustFName = input("Enter the Customers First Name: ")
        CustLName = input("Enter the Customers Last Name: ")
        CustAddress = input("Enter the Customers Address: ")
        City = input("Enter the City: ").title()
        Prov = input("Enter the Province: ").upper()
        Postal = input("Enter Postal Code (X1X 1X1): ")
        CustPhoneNum = input("Enter Phone Number (xxx-xxx-xxxx): ")
        while True:
            try:
                CarAmount = int(input("Enter Number of insured cars"))
            except:
                print('Invalid input!')
            else:
                if CarAmount >= 1:
                    break
                else:
                    print('Invalid input!')

        while True:
            OptGlassCov = input("Would you Like Optional Glass Coverage? (Y or N): ")
            OptGlassCov = OptGlassCov.upper()
            if OptGlassCov == 'Y' or OptGlassCov == 'N':
                break
            else:
                print("Please Enter Y or N")
        while True:
            ExtraLiability = input("Would you like extra Liability up to $1,000,000? (Y or N): ")
            ExtraLiability = ExtraLiability.upper()
            if ExtraLiability == 'Y' or ExtraLiability == 'N':
                break
            else:
                print("Please Enter Y or N")
        while True:
            OptLoanerCar = input("Would you like Optinal Loaner Car? (Y or N): ")
            OptLoanerCar = OptLoanerCar.upper()
            if OptLoanerCar == 'Y' or OptLoanerCar == 'N':
                break
            else:
                print("please Enter Y or N")

# Calculations

    if CarAmount == 1:
        InsPrem = BasicPrem
    if CarAmount > 1:
        InsPrem = BasicPrem + (((BasicPrem) * (CarAmount - 1)) * ADD_DISC_RATE)
    if ExtraLiability.upper() == 'Y':
        ExtraCharge1 = (CarAmount * ADD_LIB_RATE)
    if OptGlassCov.upper() == 'Y':
        ExtraCharge2 = (CarAmount * GLASS_COV_RATE)
    if OptLoanerCar.upper() == 'Y':
        ExtraCharge3 = (CarAmount * LOAN_CAR_RATE)
    print(ExtraCharge1)
    print(InsPrem)
    print(ExtraCharge3)
    print(ExtraCharge2)
    TotExchangeCharge = ExtraCharge1 + ExtraCharge2 + ExtraCharge3
    TotPremium = InsPrem + TotExchangeCharge
    TAX = TotPremium * HST_RATE
    FinalTotCost = TotPremium + TAX
    MonthlyPayment = (FinalTotCost + 39.99) // 12

# Print Statement

    print("CUSTOMER DETAILS")
    print("LISTING")
    print()
    print("CUSTOMER       ADDRESS       CITY        PROVINCE        POSTAL        PHONE")
    print("  NAME")
    print("{:<11} {:<15} {:<9} {:<10} {:<7} {:<7}".format(CustFName, CustAddress, City, Prov, Postal, CustPhoneNum))

    print("ONE STOP INSURANCE COMPANY")
    print()
    print("TOTAL EXTRA      INSURANCE      TOTAL PREMIUM      TAX      TOTAL")
    print("   CHARGE         PREMIUM                                        ")
    print("="*15)
    print("{:<20} {:<10} {:<10} {:<10} {:<10}".format(TotExchangeCharge, InsPrem, TotPremium, TAX, FinalTotCost))

    f = open("Policies.dat", "a")
    f.write(
        f"{POLICY_NUM}, {CustFName}, {CustAddress}, {City}, {Prov}, {Postal}, {CustPhoneNum}, "
        f"{ExtraLiability}, {OptGlassCov}, {OptLoanerCar}, {InsPrem}\n")
    f.close()
    print(" Policy was saved! ")
    print("="*50)
    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF dd-mon-yy")
    print()
    print("POLICY CUSTOMER                     INSURANCE      EXTRA        TOTAL PREMIUM")
    print("NUMBER NAME                          PREMIUM        COST                     ")
    print("="*50)
    print("{:<2} {:30} {:<2} {:<2} {:<2}".format(POLICY_NUM, CustFName, InsPrem, FinalTotCost, TotPremium))
    print("="*50)
    print("ONE STOP INSURANCE COMPANY")
    print("MONTHLY PAYMENT LISTING AS OF dd-mon-yy")
    print()
    print("POLICY CUSTOMER                    TOTAL      HST    TOTAL     MONTHLY")
    print("NUMBER NAME                          PREMIUM           COST      PAYMENT")
    print("=" * 50)
    print("{:<2} {:30} {:<2} {:<2} {:<2}".format(POLICY_NUM, CustFName, TotPremium, HST_RATE, FinalTotCost, MonthlyPayment))
    print("=" * 50)
    print("TOTAL POLICIES: ")

    while True:
        ProgramContinue = input("Would you like to continue the program? (Y or N): ")
        ProgramContinue = ProgramContinue.upper()
        if ProgramContinue != "Y" and ProgramContinue != "N":
            print("Please press Y or N")
            continue
        elif ProgramContinue == "N":
            POLICY_NUM += 1
            break
        elif ProgramContinue == "Y":
            POLICY_NUM += 1
            break
    if ProgramContinue == "Y":
        continue

    f = open("OSICDef.dat", "w")
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASE_RATE:,.2f}\n")
    f.write(f"{ADD_DISC_RATE:,.2f}\n")
    f.write(f"{ADD_LIB_RATE:,.2f}\n")
    f.write(f"{OptGlassCov:,.2f}\n")
    f.write(f"{OptLoanerCar:,.2f}\n")
    f.write(f"{HST_RATE:,.2f}\n")
    f.write(f"{PROCESS_FEE:,.2f}\n")
    f.close()