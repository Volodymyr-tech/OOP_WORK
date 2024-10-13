from src.user_interaction import UserInteraction


def main():
    ui = UserInteraction()

    while True:
        print("\nМеню:")
        print("1. Поиск вакансий")
        print("2. Показать вакансии")
        print("3. Удалить вакансию")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            ui.search_vacancies()
        elif choice == "2":
            ui.show_vacancies()
        elif choice == "3":
            ui.delete_vacancy()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
