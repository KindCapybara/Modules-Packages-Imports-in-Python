from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from web3 import Web3
from application.check_token_balance import contract_initialization


if __name__ == '__main__':
    print(datetime.date(datetime.today()))
    calculate_salary()
    get_employees()
    print('Проверка баланса кошельков')
    contract_initialization(Web3.toChecksumAddress('0xe9e7cea3dedca5984780bafc599bd69add087d56'))
