#Wenhuang Lin

def encoder(pw):
    temp = []
    result = ""
    for x in pw:
        if (int(x) < 7):
            temp.append(int(x)+3)
        else:
            temp.append(int(x)+3-10)
    for x in range(len(temp)):
        result = result + str(temp[x])
    return result
# Ryan Tram Segment
def decoder(en_pw):
    temp = []
    result = ""
    for x in en_pw:
        if (int(x) < 3):
            temp.append(10 + int(x) - 3)
        else:
            temp.append(int(x) - 3)
    for x in range(len(temp)):
        result += str(temp[x])
    return result

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        
        user_menu_option = int(input("Please enter an option: "))
        if user_menu_option == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_pw = encoder(user_password)
            print("Your password has been encoded and stored!")
        elif user_menu_option == 2:
            decoded_pw = decoder(encoded_pw)
            print(f'The encoded password is {encoded_pw}, and the original password is {decoded_pw}.')
        elif user_menu_option == 3:
            break
        print()



if __name__ == '__main__':
    main()
