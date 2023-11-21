import re
# Определение функции emails, которая принимает путь к файлу в качестве аргумента.
def emails(file_path):
# Открытие файла в режиме чтения и сохранение его в переменную file.
    with open(file_path, 'r') as file:
        content = file.read()
#соответствует одному или более символам из набора a-z, A-Z, 0-9, '.', '_', '%', '+', и '-'.
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
        return emails
      
# Задание пути к файлу, который будет обработан.
file_path = 'file.html'
out = emails(file_path)
print("Extracted Emails:", out)