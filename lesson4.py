import re

def process_array_command(command, array):

    if re.match(r"Получить элемент по \d+ индексу", command):
        match = re.match(r"Получить элемент по (\d+) индексу", command)
        index = int(match.group(1))
        if 0 <= index < len(array):
            return array[index]
        else:
            return "Ошибка: Индекс вне диапазона"

    elif re.match(r"Получить элементы с \d+ по \d+ с шагом \d+", command):
        match = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
        start = int(match.group(1))
        end = int(match.group(2))
        step = int(match.group(3))

        if 0 <= start <= end < len(array) and step > 0:
            return array[start:end+1:step]  # +1, чтобы включить конечный элемент
        else:
            return "Ошибка: Некорректные параметры среза"

    elif re.match(r"Получить \d+ элемент с конца массива", command):
        match = re.match(r"Получить (\d+) элемент с конца массива", command)
        index_from_end = int(match.group(1))
        if 0 < index_from_end <= len(array):
            return array[-index_from_end]
        else:
            return "Ошибка: Индекс вне диапазона"
    else:
        return "Ошибка: Неизвестная команда, проверьте правильность ввода и корректность индексов (>=0)"

#массив
some_array = [10, 20, 30, 40, 50, 60]
#здесь писать команды
print(process_array_command("Получить элемент по 2 индексу", some_array))
print(process_array_command("Получить элементы с 1 по 5 с шагом 2", some_array))
print(process_array_command("Получить 3 элемент с конца массива", some_array))
print(process_array_command("Получить элемент по 10 индексу", some_array))  # Вывод: Ошибка: Индекс вне диапазона
print(process_array_command("Получить элементы с 5 по 1 с шагом 2", some_array))  # Вывод: Ошибка: Некорректные параметры среза
print(process_array_command("Получить 100 элемент с конца массива", some_array)) # Вывод: Ошибка: Индекс вне диапазона
print(process_array_command("Неправильная команда", some_array)) # Вывод: Ошибка: Неизвестная команда, проверьте правильность ввода и корректность индексов (>=0)