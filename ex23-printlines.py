import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    print(">>>> main", repr(language_file), encoding, errors)
    line = language_file.readline()

    if line:
        print(">> there's a line", repr(line))
        print_line(line, encoding, errors)
        print(">> calling main again")
        return main(language_file, encoding, errors)
    print("<<<< exit main")


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    print("<<<< exit print_line")

languages = open("languages.txt", encoding="UTF-8")

main(languages, input_encoding, error)
