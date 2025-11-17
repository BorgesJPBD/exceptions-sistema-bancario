from datetime import datetime
from typing import List
from abc import ABC, abstractmethod

# importa as exceções do outro arquivo
from errors import (
    ErroBanco,
    SaldoInsuficienteError,
    ValorInvalidoError,
    ValorNegativoError,
    TipoInvalidoError,
    ContaNaoEncontradaError,
    AgenciaNaoEncontradaError,
    ClienteNaoEncontradoError,
    SenhaIncorretaError,
    LimiteExcedidoError,
    ContaJaExistenteError,
    AgenciaJaExistenteError,
)

# --------------------------------------
# Função auxiliar opcional (somente exceções!)
# --------------------------------------

def validar_valor(value: float) -> float:
    """Valida valores numéricos para operações bancárias."""
    try:
        value = float(value)
    except (TypeError, ValueError) as e:
        raise ValorInvalidoError("Valor inválido: não é um número.") from e

    if value == 0:
        raise ValorInvalidoError("O valor não pode ser zero.")
    if value < 0:
        raise ValorNegativoError("O valor não pode ser negativo.")

    return value


# --------------------------------------
# CLASSES
# --------------------------------------

class Bank:
    def __init__(self, name: str, cnpj: str, location: str, phone: str):
        self._name = name
        self._cnpj = cnpj
        self._location = location
        self._phone = phone
        self._branch: List['Branch'] = []

        # validações básicas de CNPJ bem simples, só exemplo
        if not isinstance(cnpj, str) or len(cnpj.replace(".", "").replace("-", "").replace("/", "")) < 8:
            raise ValorInvalidoError("CNPJ em formato inválido.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValorInvalidoError("Nome do banco não pode ser vazio.")
        self._name = value

    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, value):
        if not isinstance(value, str):
            raise ValorInvalidoError("CNPJ deve ser uma string.")
        self._cnpj = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value:
            raise ValorInvalidoError("Endereço do banco não pode ser vazio.")
        self._location = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValorInvalidoError("Telefone do banco não pode ser vazio.")
        self._phone = value

    def add_branch(self, branch: 'Branch'):
        # valida tipo
        if not isinstance(branch, Branch):
            raise TipoInvalidoError("O objeto informado não é uma branch válida.")

        # valida se já existe agência com o mesmo número
        for b in self._branch:
            if b.number == branch.number:
                raise AgenciaJaExistenteError(f"Já existe uma agência com o número {branch.number}.")

        self._branch.append(branch)
        print("Branch added successfully")

    def show_branches(self):
        for branch in self._branch:
            print(f"Branch: {branch.name}")

    def get_branch_by_number(self, number: str) -> 'Branch':
        for b in self._branch:
            if b.number == number:
                return b
        raise AgenciaNaoEncontradaError(f"Agência com número {number} não encontrada.")


class Branch:
    def __init__(self, number: str, name: str, location: str, phone: str):
        if not number:
            raise ValorInvalidoError("Número da agência não pode ser vazio.")
        self._number = number
        self._name = name
        self._location = location
        self._phone = phone
        self._accounts: List['Account'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not value:
            raise ValorInvalidoError("Número da agência não pode ser vazio.")
        self._number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValorInvalidoError("Nome da agência não pode ser vazio.")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value:
            raise ValorInvalidoError("Endereço da agência não pode ser vazio.")
        self._location = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value:
            raise ValorInvalidoError("Telefone da agência não pode ser vazio.")
        self._phone = value

    def add_account(self, account: 'Account'):
        if not isinstance(account, Account):
            raise TipoInvalidoError("O objeto informado não é uma conta válida.")

        for c in self._accounts:
            if c.number == account.number:
                raise ContaJaExistenteError(f"Já existe uma conta com o número {account.number} nessa agência.")

        self._accounts.append(account)

    def get_account_by_number(self, number: str) -> 'Account':
        for c in self._accounts:
            if c.number == number:
                return c
        raise ContaNaoEncontradaError(f"Conta número {number} não encontrada nesta agência.")


class Client:
    def __init__(self, name, age):
        if not name:
            raise ValorInvalidoError("Nome do cliente não pode ser vazio.")
        if age < 0:
            raise ValorNegativoError("Idade do cliente não pode ser negativa.")
        self._name = name
        self._age = age
        self._accounts: List['Account'] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValorInvalidoError("Nome do cliente não pode ser vazio.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValorNegativoError("Idade do cliente não pode ser negativa.")
        self._age = value


class Transaction:
    def __init__(self, type: str, value: float, account: 'Account'):
        self._type = type
        self._value = value
        self._account = account
        self._date = datetime.now()

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def date(self):
        return self._date

    def get_receipt(self):
        print(f"Date: {self.date}")


class Authenticate(ABC):

    @abstractmethod
    def auntheticate(self, password: str) -> bool:
        pass


class Tax(ABC):
    @abstractmethod
    def get_tax_value(self) -> float:
        pass


class Earning(ABC):
    @abstractmethod
    def get_Earning(self) -> float:
        pass


class Account(Authenticate, ABC):
    def __init__(self, number: str, client: str, balance: float, password: str):
        if not number:
            raise ValorInvalidoError("Número da conta não pode ser vazio.")
        if balance < 0:
            raise ValorNegativoError("Saldo inicial não pode ser negativo.")
        if not password:
            raise ValorInvalidoError("Senha da conta não pode ser vazia.")

        self._number = number
        self._client = client
        self._balance = balance
        self._password = password
        self._transactions: List['Transaction'] = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not value:
            raise ValorInvalidoError("Número da conta não pode ser vazio.")
        self._number = value

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        if not value:
            raise ValorInvalidoError("Nome do cliente na conta não pode ser vazio.")
        self._client = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not value:
            raise ValorInvalidoError("Senha da conta não pode ser vazia.")
        self._password = value

    def authentication(self, password: str):
        # aqui podemos levantar uma exception se a senha estiver errada
        if not self.auntheticate(password):
            raise SenhaIncorretaError("Senha incorreta para a conta.")
        return True

    @abstractmethod
    def withdraw(self, value: float):
        pass

    @abstractmethod
    def deposit(self, value: float):
        pass

    def auntheticate(self, password: str) -> bool:
        return self._password == password

    def total(Self):
        pass

    def print_total(self):
        pass


class Current_account(Account, Tax):
    def __init__(self, number: str, client: str, balance: float,
                 password: str, limit: float):
        if limit < 0:
            raise ValorNegativoError("O limite da conta não pode ser negativo.")
        super().__init__(number, client, balance, password)
        self._limit = limit
        self._tax = 10.0
        self._transactions: List['Transaction'] = []

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValorNegativoError("O limite não pode ser negativo.")
        self._limit = value

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        value = validar_valor(value)
        self._tax = value

    def withdraw(self, value):
        value = validar_valor(value)

        withdraw_value = value + self._tax
        available = self._balance + self._limit

        # Exemplo de uso de LimiteExcedidoError:
        if value > self._limit:
            raise LimiteExcedidoError("Valor do saque ultrapassa o limite da conta.")

        if withdraw_value <= available:
            self.balance -= withdraw_value
            print(f"the remaining value on the account is: {self._balance}")
            transaction = Transaction("current", value, self)
            self._transactions.append(transaction)
        else:
            raise SaldoInsuficienteError(
                "Não é possível sacar: saldo + limite insuficientes."
            )

    def deposit(self, value):
        value = validar_valor(value)
        self._balance += value
        print(f"Depósito realizado. Novo saldo: {self._balance}")

    def get_tax_value(self):
        return self._balance * 0.07


class Savings_account(Account, Earning):
    def __init__(self, number: str, titular: str, balance: float,
                 password: str, earnings: float):
        if earnings < 0:
            raise ValorNegativoError("Taxa de rendimento não pode ser negativa.")
        super().__init__(number, titular, balance, password)
        self._earnings = earnings
        self._date = datetime.now().day

    def get_Earning(self):
        # Ex: poderia aplicar rendimento, só esquemático por enquanto
        return self._balance * self._earnings


# ===========================
#   BLOCO DE TESTES / EXEMPLOS
# ===========================

if __name__ == "__main__":

    try:
        bank1 = Bank("bank1", "123.456/0001-00", "123", "123")
        agency1 = Branch("1", "agency on izidoro", "Izidoro2", "123321")
        agency2 = Branch("3", "branch on vioção", "143", "1111111")

        bank1.add_branch(agency1)
        bank1.add_branch(agency2)
        bank1.show_branches()

        # forçar erro de agência duplicada:
        bank1.add_branch(Branch("1", "Agência repetida", "X", "Y"))

    except AgenciaJaExistenteError as e:
        print("Erro de agência duplicada:", e)
    except ErroBanco as e:
        print("Erro do sistema bancário ao criar banco ou agências:", e)

    # branch inválida (tipo errado)
    try:
        bank1.add_branch("isso não é uma branch")
    except TipoInvalidoError as e:
        print("Tratando erro de branch inválida:", e)

    # conta corrente
    try:
        account1 = Current_account("123", "Cliente 1", 100.0, "123", 50.0)
        agency1.add_account(account1)
        account1.withdraw(20.0)
    except ErroBanco as e:
        print("Erro ao sacar:", e)

    # saque maior que limite de saque
    try:
        account1.withdraw(1000.0)
    except LimiteExcedidoError as e:
        print("Erro de limite de saque:", e)
    except SaldoInsuficienteError as e:
        print("Tratando saque maior que o permitido:", e)

    # saque com valor inválido
    try:
        account1.withdraw("abc")
    except ValorInvalidoError as e:
        print("Erro ao tentar sacar com valor inválido:", e)

    # depósito com valor inválido
    try:
        account1.deposit("xyz")
    except ValorInvalidoError as e:
        print("Erro ao tentar depositar com valor inválido:", e)

    # autenticação com senha errada
    try:
        account1.authentication("senha_errada")
    except SenhaIncorretaError as e:
        print("Falha de autenticação:", e)
