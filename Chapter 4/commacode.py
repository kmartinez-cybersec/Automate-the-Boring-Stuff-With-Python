def commas(list):
    try:
        for item in range(len(list) - 1):  # For all but the last item in the list:
            print(list[item] + ', ', end='')  # Print the item and a comma
        print('and ' + list[-1])  # Print "and, " before the last item in the list
    except IndexError:
        print('Sorry, that list is empty')

empty = []
spam = ['apples', 'bananas', 'tofu', 'cats']
commas(spam)
commas(empty)
