import argparse
from random import randint, sample
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def get_char(chars: str) -> str:
    return chars[randint(0, len(chars) - 1)]

def make_password(password_len: int) -> str:
    ascii_list = [
            ascii_lowercase,
            ascii_uppercase,
            punctuation,
            digits
    ]
    password = []
    count = 0
    for i in range(password_len):
        if count > 3:
            count = 0
            ascii_list = sample(ascii_list, k=len(ascii_list))
        password.append(get_char(ascii_list[count]))
        count += 1
    return ''.join(sample(password, k=len(password)))

def main() -> None:
    parser = argparse.ArgumentParser(
            prog='genpass',
            description='Password generator',
            epilog='Developed by Erlon'
    )
    parser.add_argument('len', help='password length', type=int, default=16)
    args = parser.parse_args()
    print(make_password(args.len))


if __name__ == '__main__':
    main()
