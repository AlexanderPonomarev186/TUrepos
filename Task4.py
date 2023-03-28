class Person:
    def __init__(self):
        self.name = input()
        self.gender = input()
        self.height = int(input()) / 100
        self.weight = int(input())

    def calculate_BMI(self):
        return int(self.weight / (self.height * self.height))

    def exact_BMI_type(self):
        values_of_BMI = {20: "Недовес. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                         25: "Нормальный вес.",
                         30: "Избыточный вес. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                         40: "Ожирение. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                         100: "Тяжелое ожирение. Рекомендуем вам обратиться к врачу или специалисту диетологу."}
        values_of_BMI_F = {19: "Недовес. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                           24: "Нормальный вес.",
                           30: "Избыточный вес. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                           40: "Ожирение. Рекомендуем вам обратиться к врачу или специалисту диетологу.",
                           100: "Тяжелое ожирение. Рекомендуем вам обратиться к врачу или специалисту диетологу."}
        if self.gender == "М":
            for key in values_of_BMI.keys():
                if self.calculate_BMI() < key:
                    return values_of_BMI[key]
        if self.gender == "Ж":
            for key in values_of_BMI_F.keys():
                if self.calculate_BMI() < key:
                    return values_of_BMI_F[key]

    def print_BMI(self):
        if self.gender == "Ж":
            print(f"Уважаемая {self.name}. \n"
                  f"Ваш ИМТ равен - {self.calculate_BMI()}. \n"
                  f"Данный ИМТ говорит о том, что у вас {self.exact_BMI_type()}")
        if self.gender == "М":
            print(f"Уважаемый {self.name}. \n"
                  f"Ваш ИМТ равен - {self.calculate_BMI()}. \n"
                  f"Данный ИМТ говорит о том, что у вас {self.exact_BMI_type()}")


tom = Person()
tom.print_BMI()
