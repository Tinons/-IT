# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, delimiter=','):

    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)


    common = []
    for participant in list1:
        if participant in list2 and participant not in common:
            common.append(participant)

    return common



common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter='|'
)


common_participants_sorted = sorted(common_participants)

print("Общие участники обеих групп:")
for participant in common_participants_sorted:
    print(participant)