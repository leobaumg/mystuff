from expenses import ExpenseManager
import sys

def main():
    manager = ExpenseManager()
    manager.load_from_csv()
    if sys.argv[1] == "filter" and sys.argv[2] == "":
        manager.filter_by_date(sys.argv[2])
    elif sys.argv[1] == "filter" and sys.argv[2] in ["chipotle", "food", "venmo", "gas"]:
        manager.filter_by_category(sys.argv[2])
    elif sys.argv[1] == "manage":
        manager.date = input("Date: ")
        while True:
            try:
                manager.add_expense()
            except EOFError:
                break
    elif sys.argv[1] == "amount" and sys.argv[2] in ["chipotle", "food", "venmo", "gas", "groceries"]:
        manager.sum_amount(sys.argv[2])

if __name__ == "__main__":
    main()
