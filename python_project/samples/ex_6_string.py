__author__ = 'Vlad'
def main():
    text = raw_input("Please type yor text: ")

    # example of count of big letters
    big_letters_amount = []
    for char in text:
        if char >= "A" and char <= "Z":
            big_letters_amount.append(char)

    print "amount of big letters in text is %s" % len(big_letters_amount), big_letters_amount
    sentences = 0 # write code here
    numbers = 0 # write code here
    words = 0 # write code here

    m = []
    for numbers in text:
       if numbers.isdigit() == True:
         m.append(numbers)

    s = 0
    for sentences in text:
       if (sentences == '.'):
           s+=1

    count = 0
    for words in text:
        words = text.split(' ')
    for q in words:
        if q.isdigit() == True:
            count+=1

    print "numbers: %s, words: %s, sentences: %s" % (len(m),len(words)-count, s)

if __name__ == '__main__':
    main()

"""
 numbers_amount = []
    for num in text:
        if num >= "0" and num <= "9":
            numbers_amount.append(num)

    sentences = len(text.split("."))
    words = len(text.split(" "))
    numbers = len(numbers_amount)

    print "numbers: %s, words: %s, sentences: %s" % (numbers, words, sentences)
"""