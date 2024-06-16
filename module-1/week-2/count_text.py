def count_text(path="P1_data.txt"):
    with open(path, "r") as file:
        text = file.read()
        text = text.lower()
        text = text.replace("\n", " ")

    return {word: text.count(word) for word in text.split()}

print(count_text())