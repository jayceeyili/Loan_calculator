from tkinter import *

class LoanCalculator:
    def __init__(self):
        window =Tk()
        window.title("Loan Calculator")

        Label(window, text = "Annual Interest Rate").grid(row = 1,
                column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2,
                column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3,
                column = 1, sticky = W)
        Label(window, text = "Credit Point").grid(row = 4,
                column = 1, sticky = W)
        Label(window, text = "Estimated Cost").grid(row = 5,
                column = 1, sticky = W)
        Label(window, text = "Final Cost").grid(row = 6,
                column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 7,
                column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 8,
                column = 1, sticky = W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar,
                justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearVar = StringVar()
        Entry(window, textvariable = self.numberOfYearVar,
                justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar,
                justify = RIGHT).grid(row = 3, column = 2)
        self.creditPointVar= StringVar()
        Entry(window, textvariable = self.creditPointVar,
              justify = RIGHT).grid(row = 4, column = 2)
        self.estimatedCostVar= StringVar()
        Entry(window, textvariable = self.estimatedCostVar,
              justify = RIGHT).grid(row = 5, column = 2)

        self.finalCostVar= StringVar()
        lblFinalCost= Label(window, textvariable =
        self.finalCostVar).grid(row = 6, column = 2,
                        sticky = E)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable =
                self.monthlyPaymentVar).grid(row = 7, column = 2,
                        sticky = E)
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable =
                self.totalPaymentVar).grid(row = 8,
                        column = 2, sticky =E)
        btComputePayment = Button(window, text = "Compute Payment",
                command = self.computePayment).grid(
                        row = 9, column = 2, sticky = E)

        window.mainloop()

    def computePayment(self):
        finalCost = self.getFinalCost(float(self.loanAmountVar.get()),
                float(self.creditPointVar.get()) / 100, float(self.estimatedCostVar.get()))
        self.finalCostVar.set(format(finalCost, "10.2f"))
        monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmountVar.get()),
                float(self.annualInterestRateVar.get()) / 1200,
                int(self.numberOfYearVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                       * int(self.numberOfYearVar.get()) + finalCost
        self.totalPaymentVar.set(format(totalPayment, "10.2f"))

    def getMonthlyPayment(self,
        loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1
            - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

    def getFinalCost(self, loanAmount, cerditPoint, estimatedCost):
        finalCost = loanAmount * cerditPoint + estimatedCost
        return finalCost

LoanCalculator()

