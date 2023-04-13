import subprocess

TASK_TEXT = 'Необходимо реализовать функцию, которая будет вычислять вероятности класса для энтропии Шеннона'
cur_dir = "task_3_py_files"
results = {}


def get_task_text() -> str:
    return TASK_TEXT


def get_student_result(student_id: int,) -> (str, int):
    msg = ""
    bal = 0
    if results[student_id][0] == 'ok':
        if results[student_id][1] == 1:
            bal = 1000
            msg = "Поздравляю! Все супер"
        else:
            msg = "К сожалению, твой код прошел только часть тестов"
    else:
        msg = "К сожалению, файл не запустился. Скорее всего, это что-то синтаксическое"
    return msg, bal


async def task_test(student_id: int, file_path: str):
    wrapper_code = ""
    with open("task_3_py_files/wrapper.py", "r") as f:
        wrapper_code = f.read()

    temp_wrapper = "task_3_py_files/temp_wrapper_" + str(student_id) + ".py"
    with open(temp_wrapper, "w") as f:
        file_path = file_path.replace('/', '.')
        f.write("from " + file_path[:-3] + " import data_entropy\n")
        f.write(wrapper_code)

    result = "task_3_py_files/result_" + str(student_id) + ".txt"
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
        if len(a) == 1:
            results[student_id] = ('ok', int(a[0]))
        else:
            results[student_id] = ('bad', 0)