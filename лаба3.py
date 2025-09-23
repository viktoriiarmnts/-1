def main():
    students = {}  

    print("Введіть ім'я студента та його оцінку (1-12). Для завершення введіть 'stop'.\n")

    while True:
        name = input("Ім'я студента: ")
        if name.lower() == "stop":
            break

        try:
            grade = int(input("Оцінка: "))
            if grade < 1 or grade > 12:
                print("Оцінка має бути від 1 до 12!")
                continue
            students[name] = grade
        except ValueError:
            print(" Введіть число від 1 до 12!")

    if not students:
        print("Немає даних для аналізу.")
        return

    print("\n Список студентів та їх оцінок:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    average = sum(students.values()) / len(students)

    excellent = [n for n, g in students.items() if 10 <= g <= 12]
    good = [n for n, g in students.items() if 7 <= g <= 9]
    weak = [n for n, g in students.items() if 4 <= g <= 6]
    failed = [n for n, g in students.items() if 1 <= g <= 3]

    print("\n Статистика:")
    print(f"Середній бал по групі: {average:.2f}")
    print(f"Кількість відмінників (10-12): {len(excellent)} → {', '.join(excellent) if excellent else 'немає'}")
    print(f"Кількість хорошистів (7-9): {len(good)}")
    print(f"Кількість відстаючих (4-6): {len(weak)}")
    print(f"Кількість тих, хто не здав (1-3): {len(failed)}")


if __name__ == "__main__":
    main()