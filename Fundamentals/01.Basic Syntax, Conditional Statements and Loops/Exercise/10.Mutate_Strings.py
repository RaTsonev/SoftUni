first_string = input()
second_string = input()
changed_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    current_string = left_part + right_part
    if current_string == changed_string:
        continue
    print(current_string)
    changed_string = current_string