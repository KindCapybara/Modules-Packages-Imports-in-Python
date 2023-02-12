from web3 import Web3
import requests
import json
import pathlib
from pathlib import Path

path_check = Path(pathlib.Path.cwd(), 'application', 'db', 'checkBalance.txt')
path_checked = Path(pathlib.Path.cwd(), 'application', 'db', 'checkedBalance.txt')

bsc = 'https://bsc-dataseed1.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))
connecting = web3.isConnected()
print('\nConnecting...', connecting)


def get_abi(contract_address):
    abi_get = requests.get(f'https://api.bscscan.com/api?module=contract&action=getabi&address={contract_address}')
    response = abi_get.json()
    ABI = json.loads(response['result'])
    return ABI


def contract_initialization(contract_address):
    token_contract = web3.eth.contract(address=contract_address, abi=get_abi(contract_address))
    counter = 0
    with open(path_check, 'r') as eth:
        count_line = (sum(1 for _ in eth))

    for i in range(count_line):
        with open(path_check, 'r') as eth:  # wallet address with a new line
            lines = eth.readlines()
            wallet_out = lines[0]
            wallet_out = Web3.toChecksumAddress(wallet_out.rstrip('\n'))
            balance = web3.fromWei(token_contract.functions.balanceOf(wallet_out).call(), 'ether')
            counter += 1
            print(f'{counter}. {wallet_out} Balance: {round((balance), 2)}')

            if balance > 0:
                with open(path_checked, 'a') as checked:
                    checked.write(f'\n{wallet_out} - {round((balance), 2)}')
        del lines[0]
        with open(path_check, 'w') as eth:
            eth.writelines(lines)
