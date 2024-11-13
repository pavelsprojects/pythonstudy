import random
import time

# Генерация массива
arr = [random.randint(0, 100) for _ in range(100000)]

def selection_sort(arr): #сортировка выбором
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

def bubble_sort(arr): #сортировка пузырьком
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

# Сортировка пузырьком
start_time = time.time()
bubble_sort(arr.copy())
end_time = time.time()
print(f"Время сортировки пузырьком: {end_time - start_time:.4f} секунд")

# Сортировка выбором
start_time = time.time()
selection_sort(arr.copy())
end_time = time.time()
print(f"Время сортировки выбором: {end_time - start_time:.4f} секунд")
#Время сортировки пузырьком: 247.5415 секунд
#Время сортировки выбором: 96.2692 секунд
#Вывод: выбранный мною алгоритм работает быстрее сортировки пузырьком