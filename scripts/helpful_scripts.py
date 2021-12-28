from brownie import accounts, network, config

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
