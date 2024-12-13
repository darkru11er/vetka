import tkinter as tk
from tkinter import ttk, messagebox
import random
def slo(a, b):
    return a + b
def vich(a, b):
    return a - b
def umn(a, b):
    return a * b
def delen(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.")
        return
    result_slo.set(slo(a, b))
    result_vich.set(vich(a, b))
    result_umn.set(umn(a, b))
    res_delen = delen(a, b)
    if res_delen == "Ошибка: деление на ноль":
        result_delen.set(res_delen)
    else:
        result_delen.set(res_delen)
def make_list():
    nums = []
    for _ in range(10):
        num = random.randint(1, 100)
        nums.append(num)
    return nums
def print_min_max(nums):
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num
def print_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total
def generate_and_show():
    nums = make_list()
    result_list.set(nums)
    min_num, max_num = print_min_max(nums)
    result_min.set(min_num)
    result_max.set(max_num)
    result_sum.set(print_sum(nums))
def gen_nums(file, num):
    with open(file, 'w') as f:
        for _ in range(num):
            f.write(str(random.randint(1, 100)) + '\n')
def read_avg(file):
    nums = []
    with open(file, 'r') as f:
        for line in f:
            num = int(line.strip())
            nums.append(num)
    if nums:
        avg = sum(nums) / len(nums)
        return avg
    else:
        return "Файл пуст."
def generate_file():
    file = entry_file.get()
    num = entry_num.get()
    try:
        num = int(num)
        gen_nums(file, num)
        messagebox.showinfo("Успех", "Файл успешно сгенерирован.")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное количество чисел.")
def read_file():
    file = entry_file.get()
    avg = read_avg(file)
    result_avg.set(avg)
class Кот:
    def __init__(self, имя, цвет):
        self.имя = имя
        self.цвет = цвет
    def мяукать(self):
        print("Мяу!")
    def описание(self):
        return f"Это кот по имени {self.имя}, он {self.цвет} цвета."
class ДомашнийКот(Кот):
    def __init__(self, имя, цвет, любимая_игрушка):
        super().__init__(имя, цвет)
        self.любимая_игрушка = любимая_игрушка
    def играть(self):
        return f"{self.имя} играет с {self.любимая_игрушка}!"
def приветствие(имя):
    return f"Привет, {имя}!"
def создать_кота():
    имя = entry_кот_имя.get()
    цвет = entry_кот_цвет.get()
    мой_кот = Кот(имя, цвет)
    result_кот.set(мой_кот.описание())
def создать_домашнего_кота():
    имя = entry_дом_кот_имя.get()
    цвет = entry_дом_кот_цвет.get()
    игрушка = entry_дом_кот_игрушка.get()
    мой_домашний_кот = ДомашнийКот(имя, цвет, игрушка)
    result_дом_кот.set(мой_домашний_кот.описание() + " " + мой_домашний_кот.играть())
root = tk.Tk()
root.title("Приложение с вкладками")
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Приложение 1')
label_a = ttk.Label(tab1, text="Введите первое число:")
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = ttk.Entry(tab1)
entry_a.grid(row=0, column=1, padx=5, pady=5)
label_b = ttk.Label(tab1, text="Введите второе число:")
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = ttk.Entry(tab1)
entry_b.grid(row=1, column=1, padx=5, pady=5)
calc_button = ttk.Button(tab1, text="Выполнить", command=calculate)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)
result_slo = tk.StringVar()
label_slo = ttk.Label(tab1, text="Сложение:")
label_slo.grid(row=3, column=0, padx=5, pady=5)
result_label_slo = ttk.Label(tab1, textvariable=result_slo)
result_label_slo.grid(row=3, column=1, padx=5, pady=5)
result_vich = tk.StringVar()
label_vich = ttk.Label(tab1, text="Вычитание:")
label_vich.grid(row=4, column=0, padx=5, pady=5)
result_label_vich = ttk.Label(tab1, textvariable=result_vich)
result_label_vich.grid(row=4, column=1, padx=5, pady=5)
result_umn = tk.StringVar()
label_umn = ttk.Label(tab1, text="Умножение:")
label_umn.grid(row=5, column=0, padx=5, pady=5)
result_label_umn = ttk.Label(tab1, textvariable=result_umn)
result_label_umn.grid(row=5, column=1, padx=5, pady=5)
result_delen = tk.StringVar()
label_delen = ttk.Label(tab1, text="Деление:")
label_delen.grid(row=6, column=0, padx=5, pady=5)
result_label_delen = ttk.Label(tab1, textvariable=result_delen)
result_label_delen.grid(row=6, column=1, padx=5, pady=5)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Приложение 2')
generate_button = ttk.Button(tab2, text="Сгенерировать список", command=generate_and_show)
generate_button.grid(row=0, column=0, columnspan=2, pady=10)
result_list = tk.StringVar()
label_list = ttk.Label(tab2, text="Сгенерированный список:")
label_list.grid(row=1, column=0, padx=5, pady=5)
result_label_list = ttk.Label(tab2, textvariable=result_list)
result_label_list.grid(row=1, column=1, padx=5, pady=5)
result_min = tk.StringVar()
label_min = ttk.Label(tab2, text="Минимальное значение:")
label_min.grid(row=2, column=0, padx=5, pady=5)
result_label_min = ttk.Label(tab2, textvariable=result_min)
result_label_min.grid(row=2, column=1, padx=5, pady=5)
result_max = tk.StringVar()
label_max = ttk.Label(tab2, text="Максимальное значение:")
label_max.grid(row=3, column=0, padx=5, pady=5)
result_label_max = ttk.Label(tab2, textvariable=result_max)
result_label_max.grid(row=3, column=1, padx=5, pady=5)
result_sum = tk.StringVar()
label_sum = ttk.Label(tab2, text="Сумма всех чисел:")
label_sum.grid(row=4, column=0, padx=5, pady=5)
result_label_sum = ttk.Label(tab2, textvariable=result_sum)
result_label_sum.grid(row=4, column=1, padx=5, pady=5)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Приложение 3')
label_file = ttk.Label(tab3, text="Введите имя файла:")
label_file.grid(row=0, column=0, padx=5, pady=5)
entry_file = ttk.Entry(tab3)
entry_file.grid(row=0, column=1, padx=5, pady=5)
label_num = ttk.Label(tab3, text="Введите количество чисел:")
label_num.grid(row=1, column=0, padx=5, pady=5)
entry_num = ttk.Entry(tab3)
entry_num.grid(row=1, column=1, padx=5, pady=5)
generate_file_button = ttk.Button(tab3, text="Сгенерировать файл", command=generate_file)
generate_file_button.grid(row=2, column=0, columnspan=2, pady=10)
read_file_button = ttk.Button(tab3, text="Показать среднее значение", command=read_file)
read_file_button.grid(row=3, column=0, columnspan=2, pady=10)
result_avg = tk.StringVar()
label_avg = ttk.Label(tab3, text="Среднее значение:")
label_avg.grid(row=4, column=0, padx=5, pady=5)
result_label_avg = ttk.Label(tab3, textvariable=result_avg)
result_label_avg.grid(row=4, column=1, padx=5, pady=5)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Приложение 4')
label_привет = ttk.Label(tab4, text="Введите имя:")
label_привет.grid(row=0, column=0, padx=5, pady=5)
entry_привет = ttk.Entry(tab4)
entry_привет.grid(row=0, column=1, padx=5, pady=5)
greet_button = ttk.Button(tab4, text="Поприветствовать", command=lambda: result_привет.set(приветствие(entry_привет.get())))
greet_button.grid(row=1, column=0, columnspan=2, pady=10)
result_привет = tk.StringVar()
label_result_привет = ttk.Label(tab4, text="Приветствие:")
label_result_привет.grid(row=2, column=0, padx=5, pady=5)
result_label_привет = ttk.Label(tab4, textvariable=result_привет)
result_label_привет.grid(row=2, column=1, padx=5, pady=5)
label_кот_имя = ttk.Label(tab4, text="Имя кота:")
label_кот_имя.grid(row=3, column=0, padx=5, pady=5)
entry_кот_имя = ttk.Entry(tab4)
entry_кот_имя.grid(row=3, column=1, padx=5, pady=5)
label_кот_цвет = ttk.Label(tab4, text="Цвет кота:")
label_кот_цвет.grid(row=4, column=0, padx=5, pady=5)
entry_кот_цвет = ttk.Entry(tab4)
entry_кот_цвет.grid(row=4, column=1, padx=5, pady=5)
create_кот_button = ttk.Button(tab4, text="Создать кота", command=создать_кота)
create_кот_button.grid(row=5, column=0, columnspan=2, pady=10)
result_кот = tk.StringVar()
label_result_кот = ttk.Label(tab4, text="Описание кота:")
label_result_кот.grid(row=6, column=0, padx=5, pady=5)
result_label_кот = ttk.Label(tab4, textvariable=result_кот)
result_label_кот.grid(row=6, column=1, padx=5, pady=5)
label_дом_кот_имя = ttk.Label(tab4, text="Имя домашнего кота:")
label_дом_кот_имя.grid(row=7, column=0, padx=5, pady=5)
entry_дом_кот_имя = ttk.Entry(tab4)
entry_дом_кот_имя.grid(row=7, column=1, padx=5, pady=5)
label_дом_кот_цвет = ttk.Label(tab4, text="Цвет домашнего кота:")
label_дом_кот_цвет.grid(row=8, column=0, padx=5, pady=5)
entry_дом_кот_цвет = ttk.Entry(tab4)
entry_дом_кот_цвет.grid(row=8, column=1, padx=5, pady=5)
label_дом_кот_игрушка = ttk.Label(tab4, text="Любимая игрушка:")
label_дом_кот_игрушка.grid(row=9, column=0, padx=5, pady=5)
entry_дом_кот_игрушка = ttk.Entry(tab4)
entry_дом_кот_игрушка.grid(row=9, column=1, padx=5, pady=5)
create_дом_кот_button = ttk.Button(tab4, text="Создать домашнего кота", command=создать_домашнего_кота)
create_дом_кот_button.grid(row=10, column=0, columnspan=2, pady=10)
result_дом_кот = tk.StringVar()
label_result_дом_кот = ttk.Label(tab4, text="Описание домашнего кота:")
label_result_дом_кот.grid(row=11, column=0, padx=5, pady=5)
result_label_дом_кот = ttk.Label(tab4, textvariable=result_дом_кот)
result_label_дом_кот.grid(row=11, column=1, padx=5, pady=5)
tab_control.pack(expand=1, fill='both')
root.mainloop()
