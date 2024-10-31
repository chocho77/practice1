class CalcNumbers:

    @staticmethod
    def sum_two_num() -> None:
        print("Sum two float numbers:")
        num1 = float(input("Enter a float number:"))
        num2 = float(input("Enter a float number: "))
        sum:float = num1 + num2
        print(f"Sum = {sum}")

    @staticmethod
    def raz_two_num() -> None:
        print("Razlika two float numbers:")
        num1 = float(input("Enter a float number:"))
        num2 = float(input("Enter a float number:"))
        raz:float = num1 - num2
        print(f"Raz = {raz}")

CalcNumbers.sum_two_num()
CalcNumbers.raz_two_num()

