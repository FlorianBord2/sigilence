def myparse(word):
    for letter in word:
        if letter.isalpha() == False:
            return 'ko'
    if len(word) == 0:
        return 'ko'
    if len(word) <= 2:
        return(word)        
    first = word[0:1]
    second = str(len(word) - 2)
    last = word[len(word)-1:len(word)]
    return first + second + last

def main():
    user_response = input('Entrer un mot (exit pour quitter): ')
    while user_response.lower() != 'exit':
        print(myparse(user_response))
        user_response = input('Entrer un mot : ')
        
if __name__ == '__main__':
    main()
