import csv

class Infor:
    def __init__(self, date, cat, amount):
        self.date = date
        self.cat = cat
        self.amount = amount

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.date = None

    def load_from_csv(self):
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = row["Date"]
                cat = row["Category"]
                amount = float(row["Amount"])
                self.expenses.append(Infor(date, cat, amount))


    def add_expense(self):
        amount = float(input("Expenses: "))
        cat = input("Category: ")
        self.expenses.append(Infor(self.date, cat, amount))
        with open("expenses.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"Date": self.date, "Category": cat, "Amount": amount})

    def sum_amount(self, category):
        total = sum(e.amount for e in self.expenses if e.cat == category)
        print(total)


    def filter_by_category(self, cat):
        filtered_category = [e for e in self.expenses if e.cat == cat]
        for e in filtered_category:
            print(f"Date: {e.date}, Category: {e.cat}, Amount: {e.amount}")
        category_total = sum(e.amount for e in filtered_category)
        print(f"\n{category_total}")


    def filter_by_date(self, date):
        filtered_date = [e for e in self.expenses if e.date == date]
        for e in filtered_date:
            print(f"Date: {e.date}, Category: {e.cat}, Amount: ${e.amount}")
        date_total = sum(e.amount for e in filtered_date)
        print(f"\n{round(date_total, 2)}")
