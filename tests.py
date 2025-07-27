from functions.get_file_content import get_file_content


def test():
    print("Results for 'main.py':")
    print(get_file_content("calculator", "main.py"))
    print()

    print("Results for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print("Results for '/bin/cat':")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print("Results for '../pokedexcli/main.go':")
    print(get_file_content("calculator", "../pokedexcli/main.go"))


if __name__ == "__main__":
    test()