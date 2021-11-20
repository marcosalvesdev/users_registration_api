from registration.aux_functions import CpfAuxMethods, OtherValidators, CepAuxMethods


# ######################## CPF TEST FUNCTIONS ###############################
def test_valid_cpf_function():
    valid_cpf = CpfAuxMethods.cpf_verificator("03677718376")
    assert valid_cpf is True


def test_invalid_cpf_function():
    valid_cpf = CpfAuxMethods.cpf_verificator("03677 7 18 % 678343476")
    assert valid_cpf[0] is False


def test_cpf_generator():
    cpf = CpfAuxMethods.cpf_generator()
    print(cpf)
    assert len(cpf) == 11


def test_cpf_list_generator():
    quant_cpf = 1
    cpf_list = CpfAuxMethods.generate_list_of_cpf(quant_cpf)
    assert len(cpf_list) == quant_cpf

############################################################################


# ######################## CEP TEST FUNCTIONS ###############################
def test_valid_cep():
    cep_instance = CepAuxMethods('29005-050')
    valid = cep_instance.cep_validation()
    assert valid[0] is True


def test_invalid_cep():
    cep_instance = CepAuxMethods('290as4323-050')
    valid = cep_instance.cep_validation()
    assert valid[0] is False


############################################################################


# ######################## OTHER TEST FUNCTIONS ###############################
def test_valid_name():
    valid = OtherValidators.check_name('Marcos Vinícius Alves da Silva')
    assert valid is True


def test_invalid_name():
    valid = OtherValidators.check_name('@Mar#cos Viní%cius da Silva¬¨')
    assert valid[0] is False


def test_valid_phone_numb():
    valid = OtherValidators.check_phone_numb('+5544991837743')
    assert valid is True


def test_invalid_phone_numb():
    valid = OtherValidators.check_phone_numb('33334444')
    assert valid[0] is False


############################################################################

