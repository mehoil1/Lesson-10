import xml.etree.ElementTree as ET

def ten_popular_words():
    from collections import Counter
    tree = ET.parse("newsafr.xml")
    descriptions = []
    root = tree.getroot()
    words = root.findall("channel/item")

    for item in words:
        description = item.find("description")
        descriptions += description.text.split()

    format_description = []
    for word in descriptions:
        if len(word) > 6:
            format_description.append(word)

    def sortByLength(inputStr):
        return len(inputStr)

    format_description.sort(key=sortByLength, reverse=True)

    Counter = Counter(format_description)
    words = Counter.most_common(10)
    for word in words:
        print(f"Слово: '{word[0]}' встречается: {word[1]} раз")


ten_popular_words()