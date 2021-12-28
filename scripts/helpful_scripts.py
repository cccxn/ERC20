from brownie import accounts, network, config
from pathlib import Path
from solcx import compile_standard, install_solc
install_solc(version='0.8.0', show_progress=True)

PROJECT_PATH = Path(".").resolve().parent
PROJECT_ERC20 = Path(PROJECT_PATH, 'ERC20')

LOCAL_BLOCKCHAIN_ENVIRONMENT = [
    'development',
    'ganache',
    'hardhat',
    'local-ganache',
    'mainnet-fork'
]


def get_account(index = None, id: int = None):
    if index is not None:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print(accounts[0].balance())
        return accounts[0]
    if id is not None:
        return accounts.load(id)
    return accounts.add(config['wallets']['from_key'])
