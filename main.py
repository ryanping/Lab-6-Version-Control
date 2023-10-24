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


def main():
    print(encoder("00009962"))




if __name__ == '__main__':
    main()
