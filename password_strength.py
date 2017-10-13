import argparse


def get_password_strength(password):
    max_strength = 10
    normal_value = 1

    minimal_length = 10
    digits = '1234567890'
    special_chars = '[]\;,"./~!@#$%^&*()_+{|}:\'<>?'

    upcase_counter = max(
        sum(1 for single_char in password if single_char.isupper()), 0.1)
    locase_counter = max(
        sum(1 for single_char in password if single_char.islower()), 0.1)
    digits_counter = sum(
        1 for single_char in password if single_char in digits)
    spec_counter = sum(
        1 for single_char in password if single_char in special_chars)

    digits_strength = min(digits_counter / len(password), normal_value)

    len_strength = min (normal_value, len(password) / minimal_length)

    lowup_case_strength = min(min((upcase_counter / locase_counter),
                                  (locase_counter / upcase_counter)),
                              normal_value)

    spec_strength = spec_counter / len(password)

    strength_list = [len_strength, lowup_case_strength,
                     digits_strength, spec_strength]

    return round(sum(strength_list) / len(strength_list) *
                 max_strength * max_strength / len(strength_list))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='The script calculates password strenth.')
    parser.add_argument('password', type=str,
                        help='password to check strength.')

    args = parser.parse_args()
    password_string = args.password

    print("The password strength is {} in points from 1 to 10".format(get_password_strength(password_string)))
