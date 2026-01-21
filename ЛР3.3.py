# TODO Напишите функцию count_letters

def count_letters(text):

    counts_dict = {}

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in counts_dict:
                counts_dict[char_lower] += 1
            else:
                counts_dict[char_lower] = 1

    return counts_dict



# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):

    total_count = sum(letters_dict.values())


    freq_dict = {}

    for letter_char, count in letters_dict.items():
        frequency = count / total_count
        freq_dict[letter_char] = frequency

    return freq_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

letter_counts = count_letters(main_str)

frequencies = calculate_frequency(letter_counts)

for letter in frequencies:
    print(f"{letter} {frequencies[letter]:.2f}")