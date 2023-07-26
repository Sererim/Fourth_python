# Возьмите задачу о банкомате из семинара
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

class ATM:
    def __init__(self):
        money: int = 0
        counter: int = 0
        operations: list[str] = []

        self.money = money
        self.counter = counter
        self.operations = operations

    def withdraw(self, amount: int) -> None:
        self.counter += 1
        if amount < self.money + self.percentage(amount, -1):
            if amount > 5_000_000:
                self.money -= self.percentage(amount, -1)
            if self.check_if_valid_sum(amount):
                if self.counter < 3:
                    self.money -= amount + self.percentage(amount, self.counter)
                    self.operations.append(f"{len(self.operations) + 1}: Operation Withdraw: {amount + self.percentage(amount, self.counter)}")
                else:
                    self.operations.append(f"{len(self.operations) + 1}: Operation Withdraw: {amount + self.percentage(amount, self.counter)}")
                    self.money -= amount + self.percentage(amount, self.counter)
            else:
                print("Error! Amount must be a multiplicity of 50.")
        else:
            print("Error! You can not withdraw more money than you have on your account.")

    def deposit(self, amount: int) -> None:
        self.counter += 1
        if amount > 5_000_000:
            self.money -= self.percentage(amount, -1)
        if self.check_if_valid_sum(amount):
            if self.counter < 3:
                self.operations.append(f"{len(self.operations) + 1}: Operation Deposit: {amount - self.percentage(amount, self.counter)}")
                self.money += amount - self.percentage(amount, self.counter)
            else:
                self.operations.append(f"{len(self.operations) + 1}: Operation Deposit: {amount - self.percentage(amount, self.counter)}")
                self.money += amount - self.percentage(amount, self.counter)
        else:
            print("Error! Amount must be a multiplicity of 50.")

    def account(self) -> None:
        print(f"Your account has: {self.money}")

    def show_operations(self) -> None:
        for j in self.operations:
            print(j)

    @staticmethod
    def percentage(amount: int, check: int = 0) -> float:
        per: float = 1.0
        if check < 3:
            per = 1.5
            if (per * amount) / 100 < 30:
                per = 30
            elif (per * amount) / 100 > 600:
                per = 600
        elif check == -1:
            per = 10.0
            per = (per * amount) / 100
        else:
            per = 3.0
            if (per * amount) / 100 < 30:
                per = 30
            elif (per * amount) / 100 > 600:
                per = 600
        return per

    @staticmethod
    def check_if_valid_sum(amount: int) -> bool:
        return True if amount % 50 == 0 else False


def main():
    amount: int = 0
    atm = ATM()
    while True:
        atm.account()
        match str(input("To deposit money enter 1.\n"
                        "To withdraw money enter 2.\n"
                        "To stop working with the ATM enter 3.\n")):
            case "1":
                try:
                    amount = int(input("Please insert money into the ATM.\n"))
                except ValueError:
                    print("Error!\nPlease insert the money correctly.")
                atm.deposit(amount)
            case "2":
                try:
                    amount = int(input("Please enter amount of money to withdraw.\n"))
                except ValueError:
                    print("Error!\nPlease enter correct data the money correctly.")
                atm.withdraw(amount)
            case "3":
                atm.show_operations()
                break
            case _:
                print("No such operation found!\nPlease try again.")
    return 0


if __name__ == "__main__":
    main()
