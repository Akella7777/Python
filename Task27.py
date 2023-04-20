# Задача No27. 
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13


# s_1 = "Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# st = input("Введите строку: ")
# st = st.lower()
# st2 = set(st.split())
# print(len(st2))

s_1 = input("Введите текст: ")
s_1 = s_1.lower().split()
print(len(s_1))

s_1 = input("Введите текст: ")
s_1 = set(s_1.lower().split())
print(len(s_1))