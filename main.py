def encryption(p, k):
    result = ''
    for i in range(len(p)):
        char = p[i]
        if ord('a') <= ord(char) <= ord('z'):
            result += chr((ord(char) + k - 97) % 26 + 97)
        elif ord('A') <= ord(char) <= ord('Z'):
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += char

    return result


def decryption(p, k):
    result = ''
    for i in range(len(p)):
        char = p[i]
        if ord('a') <= ord(char) <= ord('z'):
            result += chr((ord(char) - k - 97) % 26 + 97)
        elif ord('A') <= ord(char) <= ord('Z'):
            result += chr((ord(char) - k - 65) % 26 + 65)
        else:
            result += char

    return result


if __name__ == '__main__':
    selected_input = True
    while selected_input:
        selected_input = input('please enter one of the following \n' 
                               'Enter 1 to encrypt \n'
                               'Enter 2 to decrypt \n'
                               'enter 3 to exit \n')
        if selected_input == '3':
            selected_input = False
        elif selected_input == '1':
            selected_text = input('Enter your message:  ')
            selected_code = input('Enter your encryption key:  ')
            print(encryption(selected_text, int(selected_code)))
        elif selected_input == '2':
            selected_text = input('Enter your message:  ')
            selected_code = input('Enter your decryption key:  ')
            print(decryption(selected_text, int(selected_code)))
