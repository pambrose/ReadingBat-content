# @desc Converting string cases

def case(name):
    if "A" in name:
        return name.upper()
    elif "e" in name:
        return name.lower()
    else:
        return name.title()


def main():
    print(name('Anna'))
    print(name('MIGUEL'))
    print(name('FRed'))
    print(name('Mr. Rodgers'))
    print(name('oliVia'))

if __name__ == '__main__':
    main()
