def open_book(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    lowered_text = text.lower()

    for c in lowered_text:
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1 
            
    return char_dict

def reportify_dict(dictionary, path, word_count):
    report =[]
    print(f"--- Begin report of {path}")
    print(f"{word_count} words found in the document")

    for entry in dictionary:
        if entry.isalpha():
            report.append({"letter" : entry, "num" : dictionary[entry]})
            
    report.sort(reverse=True, key=sort_on)

    for dict in report:
        print(f"The '{dict["letter"]}' character was found {dict["num"]} times")

    print("--- End report ---")
    return report

def sort_on(dict):
    return dict["num"]


if __name__ == '__main__':
    path = "books/frankenstein.txt"
    story = open_book(path)
    #print(story)
    #print(count_words(story))
    #print(count_chars(story))
    reportify_dict(count_chars(story), path, count_words(story))