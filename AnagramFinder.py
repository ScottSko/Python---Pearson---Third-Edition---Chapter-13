import sys

def main():

    print("You are running anagram finder")

    first_string = input("Please enter a string: ").lower()
    second_string = input("Please enter another string: ").lower()

    list = []
    list_2 = []

    index = 0

    truth = False

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


    #for k in second_string:
    #    try:
    #        value_2 = list.index(k)
    #    except:
    #        print("The strings are not anagrams")
    #        sys.exit()

    #for b in first_string:
    #    try:
    #        value = list_2.index(b)
    #    except:
    #        print("The strings are not anagrams")
    #        sys.exit()


    for z in list:
        for a in list_2:
            #print("z is", z)
            #print("a is", a)
            if z == a:
                truth = True

                #first = list.index(z)
                #second = list_2.index(a)
                #print("loop went through.")
            #else:
                #print("loop did not go through.")


        if truth == False:
            print("The strings are not anagrams.")
            sys.exit()
        truth = False

        for u in list_2:
            for l in list:
                #print("u is", u)
                #print("l is", l)
                if u == l:
                    truth = True

                    #first = list.index(z)
                    #second = list_2.index(a)
                    #print("loop went through.")
                #else:
                    #print("loop did not go through.")

            if truth == False:
                print("The strings are not anagrams.")
                sys.exit()
            truth = False

        #print(z)
        #print(a)

        #print(list)
        #print(list_2)

    print("The strings are anagrams")

main()






