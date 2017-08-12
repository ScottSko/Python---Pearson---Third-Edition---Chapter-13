import sys

def main():

    print("You are running scratch paper for anagram finder")

    first_string = input("Please enter a string: ").lower()
    second_string = input("Please enter another string: ").lower()

    list = [] * len(first_string)
    list_2 = [] * len(second_string)

    if first_string == second_string:

        print("The strings are not anagrams, they are the same string.")
        sys.exit()

    if len(first_string) != len(second_string):

        print("The strings are not anagrams, they are different lengths.")
        sys.exit()

    for x in first_string:
        list.append(x)

    for y in second_string:
        list_2.append(y)

    print(list)
    print(list_2)

    list.sort()
    list_2.sort()

    print(list)
    print(list_2)

    new_string = ''

    for o in list:
        new_string += o

    print(new_string)

    if list == list_2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

main()