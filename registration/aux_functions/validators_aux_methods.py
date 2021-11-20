"""
This moodule only contains helper methods that can be used in other parts of this API
If you don't want to create a method, but just a simple function I sugesting you make a new module for it
TODO: Refectory this part to Strategy pattern
"""
from rest_framework import serializers, status
from rest_framework.response import Response
from random import randint
import re


class Sanatize:
    @staticmethod
    def sanitizes(value: str) -> str:
        # This method returns a string with no special or alphabetic characters
        value_sanitized = re.sub(r'[a-zA-Z^Çç./*@$%()+#!?\]\[_&\'\s"=~|,ªº-]', '', value)
        return value_sanitized

    @staticmethod
    def sanitizes_string(value: str) -> str:
        # This method returns a string with no special or numerics characters
        value_sanitized = re.sub(r'[0-9^.;:/*@$%()+#!?\]\[_&\'\s"=~|,ªº-]', '', value)
        return value_sanitized

    @staticmethod
    def sanitizes_integer(value: str) -> int:
        # This method removes all the special and alphabetic characters, convert to integer and return it
        value_sanitized = re.sub(r'[a-zA-Z^Çç.;:/*@$%()+#!?\]\[_&\'\s"=~|,ªº-]', '', value)
        return int(value_sanitized)


class CpfAuxMethods:
    @staticmethod
    def cpf_verificator(cpf: str) -> bool:
        # This method checks if the CPF is a valid one
        if type(cpf) is str:
            cpf_clear = Sanatize.sanitizes(cpf)
            cpf = [int(digit) for digit in list(cpf_clear)]
        try:
            assert len(cpf) == 11
            digits_list = [cpf[0:9], cpf[0:10]]
            mutip = 10
            total = 0
            for ls in digits_list:
                for digit in ls:
                    total += digit * mutip
                    mutip -= 1
                    if mutip < 2:
                        rest_div = (11 - (total % 11))
                        if len(ls) == 9 and rest_div == cpf[9]:
                            mutip = 11
                            total = 0
                        elif len(ls) == 10 and rest_div == cpf[10]:
                            return True
                        else:
                            return False, f'The CPF {cpf} is not valid!'
        except AssertionError:
            return False, f'CPF must contain 11 digits, the CPF you sended has {len(cpf)}'

    @staticmethod
    def cpf_generator() -> list:
        # This method just generate a random valid cpf
        cpf_digits = list()
        while True:
            random_ls = [randint(0, 9) for num in range(0, 11)]
            valid = CpfAuxMethods.cpf_verificator(random_ls)
            if valid:
                for digit in random_ls:
                    cpf_digits.append(str(digit))
                return ''.join(cpf_digits)

    @staticmethod
    def generate_list_of_cpf(quant_cpf: int) -> list:
        # This method just generate a random valid cpf
        cpf_list = list()
        while True:
            cpf_list.append(CpfAuxMethods.cpf_generator())
            if len(cpf_list) == quant_cpf:
                break
        return cpf_list


class CepAuxMethods:
    def __init__(self, cep: str):
        self.cep = cep

    # This method checks if the CEP is valid a valid one
    def cep_validation(self) -> bool:
        clear_cep = Sanatize.sanitizes(self.cep)
        try:
            assert len(clear_cep) == 8
            return True, clear_cep
        except AssertionError:
            return False, f'CEP with invalid length!'



class OtherValidators:
    @staticmethod
    def check_name(name: str) -> bool:
        special_char = re.findall(r'[0-9^.;:/*@$%()+#!?\]\[_&\'"¨¬=~|,ªº-]', name)
        if len(special_char) > 0:
            return False, f'No special character is allowed'
        else:
            return True

    @staticmethod
    def check_phone_numb(phone_numb: str) -> bool:
        # This method only check brazilian phone numbers
        clear_numb = Sanatize.sanitizes(phone_numb)
        if len(clear_numb) < 11 or len(clear_numb) > 13:
            return False, f'The phone {clear_numb}, are not valid.'
        else:
            return True

