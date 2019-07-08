import json

def ten_popular_words():
    from collections import Counter
    with open('newsafr.json', encoding='utf-8') as f:
        data = json.load(f)
        words = data['rss']['channel']['items']

        descriptions = []

        for i in words:
            descriptions.append(i['description'].split())

        format_description = []

        for word in sum(descriptions, []):
            if len(word) > 6:
                format_description.append(word)

        Counter = Counter(format_description)
        words = Counter.most_common(10)
        for word in words:
            print(f'Слово: "{word[0]}" встречается: {word[1]} раз')

ten_popular_words()