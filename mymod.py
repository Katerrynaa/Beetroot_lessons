#1 part
def count_lines():
    with open("my_file.txt", "r") as file:
        lines = len(file.readlines())
        print("Number of lines: ", lines)

count_lines()

#2 part
def count_chars():
    with open("my_file.txt", "r") as file:
        data = file.read()
        number_of_characters = len(data)
        print("Number of characters: ", number_of_characters)
        
count_chars()

#3 part
def test():
    lines = count_lines()
    chars = count_chars()
    print(f"Number of lines: {lines}")
    print(f"Number of chars: {chars}")

    






   
