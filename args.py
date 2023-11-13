import argparse

# python args.py --file file_to_read.txt

def usage():
    parser = argparse.ArgumentParser(
       description="Parse file and demo information.",
       #epilog="Designed by developer Ivanna Ivannivna Juk",
       prog="args"
    )

    parser.add_argument(
       '-f', '--file',
       required=True,  # обовязковый параметр для вводу
       type=str,  # тип даних
       help='Повний або відносний шлях до файлу'  # пояснення для опцій
    )

    parser.add_argument(
       '-o', '--opacity',
       # required=True,  # обовязковый параметр для вводу
       type=str,  # тип даних
       help='ghghghghghghghghghghghghghghу'  # пояснення для опцій
    )

    args = parser.parse_args()

    return args

def main():
    arguments = usage()
    print("arguments.file: ", arguments.file)
    print("arguments.opacity: ", arguments.opacity)



if __name__ == "__main__":
    main()

