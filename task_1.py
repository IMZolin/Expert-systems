import subprocess

TASK_TEXT = 'Необходимо реализовать функцию select.\n' \
            'Так как база фактов небольшая, то задание будет засчитано в случае прохождения всех тестов. ' \
            'Также предусмотрен бонус за оптимальное решение по числу заданных вопросов'
cur_dir = "task_1_py_files"
results = {}


def get_task_text() -> str:
    return TASK_TEXT


def get_student_result(student_id: int) -> (str, int):
    msg = ""
    bal = 0
    if results[student_id][0] == 'ok':
        if results[student_id][1] == 20:
            bal = 1000
            msg = "Поздравляю! Твой код прошел 20/20 тестов"
            if results[student_id][2] > 20:
                bal += (results[student_id][2] - 20) * 10
                msg += "\nХочу отдельно похвалить его, он задал не очень много вопросов, поэтому начисляю премию: " + str(bal)
        else:
            msg = "К сожалению, твой код прошел только часть тестов: " + str(results[student_id][1]) + "/20"
    elif results[student_id][0] == 'err':
        msg = "К сожалению, файл не запустился, возникли некоторые ошибки: " + str(results[student_id][1])
        bal = 0
    else:
        msg = "К сожалению, файл не запустился. Скорее всего, это что-то синтаксическое"
        bal = 0
    return msg, bal


async def task_test(student_id: int, file_path: str):
    wrapper_code = ""
    with open("task_1_py_files/wrapper.py", "r") as f:
        wrapper_code = f.read()

    temp_wrapper = "task_1_py_files/temp_wrapper_" + str(student_id) + ".py"
    with open(temp_wrapper, "w") as f:
        file_path = file_path.replace('/', '.')
        f.write("from " + file_path[:-3] + " import select\n")
        f.write(wrapper_code)

    result = "task_1_py_files/result_" + str(student_id) + ".txt"
    f = open(result, "w")
    try:
        c = subprocess.call(['python', temp_wrapper], timeout=10, stdout=f)
    except subprocess.TimeoutExpired:
        f.write('Превышено время ожидания, возможно вечный цикл')
    except subprocess.CalledProcessError as err:
        f.write('Другие ошибки:\n' + str(err))
    except subprocess.SubprocessError:
        print('Супер другие ошибки у юзера' + str(student_id))
    f.close()

    with open(result, "r") as f:
        a = f.readlines()
        if len(a) == 2:
            results[student_id] = ('ok', int(a[0]), int(a[1]))
        elif len(a) == 1:
            results[student_id] = ('err', a[0])
        else:
            results[student_id] = ('bad', 0)
