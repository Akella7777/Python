# |Задание на выбор или дополнительное про классы (тема 10ого семинара)|
#
# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.
#
# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
#
# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
#
# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;
#
# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;
#
# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;
#
# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
#
# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
#
# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)
#
# Пример
#
# dr = Dragon(69, 5, “brown™)
# dr1 = Dragon(69, 5, “gray")
# print (dr > dr1, dr != dr1, dr <= dr1)
# print(dr, dr1, sep="\n")
# print()
#
# dr.change_color("white")
# dr -= 23
# dr1 -= 2
# dr2 = dr+dr1
# print(dr, dr1, dr2, sep="\n")
#
# print(dr("Welcome")
#
# Вывод
#
# False True True
# Dragon with height 69, danger 5 and color brown.
# Dragon with height 69, danger 5 and color gray.
#
# Dragon with height 66, danger 10 and color white.
# Dragon with height 35, danger 6 and color gray.
# Dragon with height 50, danger 10 and color brown.
# WelcomeWelcomeWelcomeWelcomeWelcome

class Dragon:
    # созданиt экземпляра (инициализация объекта)
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    # Определяем поведение оператора меньше, <
    def __lt__(self, other):
        return self.height < other.height and self.danger < other.danger and self.color < other.color

    #  Определяем поведение оператора меньше или равно, <=
    def __le__(self, other):
        return self.height <= other.height and self.danger <= other.danger and self.color <= other.color

    # Определяем поведение оператора больше, >.
    def __gt__(self, other):
        return self.height > other.height and self.danger > other.danger and self.color > other.color

    # Определяем поведение оператора больше или равно, >=
    def __ge__(self, other):
        return self.height >= other.height and self.danger >= other.danger and self.color >= other.color

    # Определяем поведение оператора равенства, ==
    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color

    # Определяем поведение оператора неравенства, !=
    def __ne__(self, other):
        return self.height != other.height or self.danger != other.danger or self.color != other.color

    # Сложение
    def __add__(self, other):
        new_color = self.color if self.color < other.color else other.color
        new_height = (self.height + other.height) // 2
        new_danger = self.danger if self.danger > other.danger else other.danger
        return Dragon(height=new_height, danger=new_danger, color=new_color)

    # Вычитание с присваиванием
    def __isub__(self, value):
        self.height -= self.height // value
        self.danger += self.danger % value
        return self

    # Остаток от деления, оператор %
    def __mod__(self, value):
        new_height = self.height % value
        new_danger = self.danger // value
        new_color = self.color
        return [Dragon(new_height, new_danger, new_color) for i in range(value)]

    #
    def __call__(self, string):
        return string * self.danger

    #
    def change_color(self, color):
            self.color = color

    # Определяем поведение функции str(), вызванной для экземпляра класса
    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.danger} and color {self.color}'

    # Определяем поведение функции repr(), вызыванной для экземпляра класса
    def __repr__(self):
        return f'Dragon {self.height}, {self.danger}, {self.color}'

dr1 = Dragon(69, 5, 'green')
dr2 = Dragon(79, 6, 'red')
dr3 = Dragon(99, 7, 'black')

print(dr1 > dr2, dr1 != dr2, dr1 <= dr2)
print(dr2 > dr3, dr2 != dr3, dr2 <= dr3)
print(dr1, dr2, sep="\n")
print()

dr1.change_color("white")
dr1 -= 23
dr2 -= 2
dr6 = dr1+dr2
print(dr6)
print(dr1, dr2, dr3, sep="\n")
print(dr1("Welcome "))
print(dr2("Python "))
