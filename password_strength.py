from string import digits
from string import punctuation
import getpass
import logging


def get_upcase(string_to_process):
    return sum(1 for single_char in string_to_process if single_char.isupper())


def get_locase(string_to_process):
    return sum(1 for single_char in string_to_process if single_char.islower())


def get_digits(string_to_process):
    return sum(
        1 for single_char in string_to_process if single_char in digits)


def get_spec(string_to_process):
    return sum(
        1 for single_char in string_to_process if single_char in punctuation)


def get_strength_list(string_to_process, upcase_counter,
                      locase_counter, digits_counter, spec_counter):
    normal_value = 1

    minimal_length = 10

    digits_strength = min(digits_counter / len(string_to_process),
                          normal_value)

    len_strength = min(normal_value, len(string_to_process) / minimal_length)

    lowup_case_strength = min(upcase_counter / len(string_to_process),
                              locase_counter / len(string_to_process),
                              normal_value)

    spec_strength = spec_counter / len(string_to_process)

    logging.error([len_strength, lowup_case_strength,
                   digits_strength, spec_strength])

    return [len_strength, lowup_case_strength, digits_strength, spec_strength]


def get_password_strength(password):
    max_strength = 10

    upcase_counter = get_upcase(password)

    locase_counter = get_locase(password)

    digits_counter = get_digits(password)

    spec_counter = get_spec(password)

    strength_list = get_strength_list(
        password, upcase_counter, locase_counter, digits_counter, spec_counter)

    return round(sum(strength_list) / len(strength_list) *
                 max_strength * max_strength / len(strength_list))


if __name__ == '__main__':
    try:
        password_string = getpass.getpass()
    except EOFError:
        exit("Invalid password")

    print("The password strength is {} in points from 1 to 10".format(
        get_password_strength(password_string)))
    logging.error(password_string)
