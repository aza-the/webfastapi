import json
from fuzzywuzzy import process

DISTRICTS_PATH: str = 'app/utils/ml/files_for_ml/distrcit_dict.json'


def find_district(district: str) -> str:
    with open(DISTRICTS_PATH, 'r', encoding='utf-8') as json_file:
        districts = json.load(json_file)
        choices = set(list(districts.keys()))
        keys = ['микрорайон', 'район', 'деревня', 'поселок', 'поселение']
        for word in district.split(','):
            for key in keys:
                if key in word:
                    ans = process.extract(word, choices)[0][0]
                    return ans
        return 'мкр. 3-й'
