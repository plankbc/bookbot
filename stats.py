import string
import sys

def get_num_words(): 
    with open(sys.argv[1]) as file:
        content = str(file.read()).lower()
        file_words = content.split()
        word_count = len(file_words)
    #print(f"{word_count} words found in the document")
    return content, word_count

    
def get_num_chars(content):
    num = 0
    all_chars = string.printable
    all_chars = all_chars.lower()
    letter_count = {}
    while len(letter_count) < 50:
        letter_to_count = content[num]
        count = content.count(letter_to_count)
        if content[num] in letter_count:
            num += 1
        else:
            letter_count[content[num]] = count
            num += 1    
    #print(letter_count)
    return letter_count


def gen_report(data):
    ordered_list = sorted(data.items(), key=lambda x:x[1], reverse=True)
    converted = dict(ordered_list)
    for key, value in converted.items():
        if key.isalpha():
            print(f"{key}: {value}")





if __name__ == "__stats__":
    gen_report(get_num_chars(get_num_words()))
    #gen_report()