from aiogram import Bot, Dispatcher, types


def create_user(bot: Bot, students: list, user_id: int):
    pass


def get_student_by_id(students, user_id):
    for s in students:
        if s.user_id == user_id:
            return s
    return None


def get_student_info(student) -> str:
    result = ""
    result += f"<b>" + student.name + "</b>\n"
    result += f"<b>" + str(student.balance) + "$</b>"
    return result


def get_students_results(students):
    with open("results.csv", "w") as f:
        for student in students:
            f.write(
                str(student.name) + ';' + str(student.balance)
            )
