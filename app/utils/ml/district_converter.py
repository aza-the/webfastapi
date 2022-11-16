import json

def convert_word(word: str) -> str:
    """Из строки достает слова, которые начинаются с большой буквы"""
    districts_words = word.split()
    words = []
    for word in districts_words:
        if word and (word[0].isupper() or word[0].isdigit()):
            words.append(word)
    return ''.join(words)


def get_disctricts(dict_file: dict, districts={}) -> list:
    """
    Преобразует словарь в словарь с:
    Ключ - Слова, начинающиеся с большой буквы(районы)
    Значение - Районы из json файла
    """
    if districts:
        return districts

    for district in dict_file.keys():
        words = convert_word(district)
        if words:
            districts[words] = district

    return districts


def find_district(disctrict: list):
    """
    Главная функция, получает список слов, из которых нужно найти район.
    Прогоняет их циклом до тех пор, пока либо не найдется нужный район,
    либо не закончится
    """
    with open("app/utils/ml/files_for_ml/distrcit_dict.json") as json_file:
        districts = get_disctricts(json.load(json_file))
        for word in disctrict.split():
            disctrict = districts.get(convert_word(word), False)
            if disctrict:
                return disctrict
    return None


def test():
    assert find_district('микрорайон Высотный') == "мкр. Высотный"
    assert find_district('Загорянский') == "Загорянский дп"
    assert find_district('Марушкинское поселение') == "Марушкинское поселение"
    assert find_district('Никольско-Архангельский') == "мкр. Никольско-Архангельский"
    assert find_district('Заря') == "мкр. Заря"
    assert find_district('Косино-Ухтомский') == "р-н Косино-Ухтомский"
    assert find_district('Электроугли') == "Электроугли"
    assert find_district('Федурново') == "Федурново деревня"
    assert find_district('Щелково-3') == "мкр. Щелково-3"


test() 