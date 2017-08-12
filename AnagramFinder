import sys

def main():

    print("You are running scratch paper for anagram finder")

    first_string = input("Please enter a string: ").lower()
    second_string = input("Please enter another string: ").lower()

    truth = False

    if first_string == second_string:

        print("The strings are not anagrams, they are the same string.")
        sys.exit()

    if len(first_string) != len(second_string):

        print("The strings are not anagrams, they are different lengths.")
        sys.exit()

    for z in first_string:
        for a in second_string:

            if z == a:
                truth = True

        if truth == False:
            print("The strings are not anagrams.")
            sys.exit()
        truth = False

    for u in second_string:
        for l in first_string:

            if u == l:
                truth = True

        if truth == False:
            print("The strings are not anagrams.")
            sys.exit()
        truth = False

    print("The strings are anagrams")

main()








