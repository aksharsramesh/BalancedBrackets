def balance(brackets):
    try:
        list = []
        if (brackets[0] == "("):
            for i in range(0, len(brackets)):
                print brackets[i]
                if (brackets[i] == "("):
                    list.append("(")
                else:
                    if (len(list) != 0):
                        list.pop()
                    else:
                        print("Imbalanced")
                        return
            if (len(list) == 0):
                print("Balanced")
                return
        else:
            print("Imbalanced")
            return
    except:
        print("error")

a = raw_input("Enter brackets: ")
balance(a)
