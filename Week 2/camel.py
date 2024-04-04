def main():
    # prompt user to input camelcase
    camel = input("CamelCase: ")

    # check and replace
    for i in camel:
        if i.isupper():
            camel = camel.replace(i, "_" + i.lower())
    print("snake name:", camel)

main()
