def main():
    try:
        file_location = "./Frankenstein.txt"
        file_content = get_file_contents(file_location)
        word_count = get_word_count(file_content)
        character_count = get_character_count(file_content)
        return print_report(character_count, file_location, word_count)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occured {e}")


def get_file_contents(file_location):
    with open(file_location) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(content):
    content_list = content.split()
    return len(content_list)

def get_character_count(text):
    count = {}
    for char in text:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1
    return count


def print_report(character_count, file_location, word_count):
    print(f"--- Begin report of {file_location} ---")
    print(f"{word_count} words found in the document\n")

    character_count_items = sorted(list(character_count.items()), key=lambda x: x[1], reverse=True)

    for k,v in character_count_items:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")


    print("--- End report ---")

main()