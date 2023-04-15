# Задача №21.
# Напишите программу для печати всех уникальных значений в словаре.
#
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# lst = []
# for i in a:
#    for k, v in i.items():
#        # print(v, end = ",")
#         lst.append((v.strip()))
# print(set(lst))
lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set_uniq = set()
for dct in lst:
    for key, value in dct.values():
        set_uniq.add(value.strip())
print(set_uniq)

# def unique(ф):
#     list_unique = []
#     unique_numbers = set(a)
#
#     for number in unique_numbers:
#         list_unique.append(number)
#
#     return list_unique
#
# print(unique(a))