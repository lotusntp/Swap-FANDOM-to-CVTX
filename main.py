import json
import logging
import math
import threading
import time
from datetime import datetime, timedelta, timezone
from multiprocessing import Process
from pickle import FALSE, TRUE
import os
import inquirer
import requests
from inquirer.themes import GreenPassion
from web3 import Web3

from legacy import Legacy
from line import LINE
from log import Log
import configparser


config = configparser.ConfigParser()

        
config.read('config.ini')

        # อ่านค่า exit_time จากเซคชัน DEFAULT
TOKEN_LINE = config.get('DEFAULT', 'token_line')
WALLET = config.get('DEFAULT', 'wallet')
PRIVATE_KEY = config.get('DEFAULT', 'private_key')
RATE = config.get('DEFAULT', 'rate')
NOTIFY = config.get('DEFAULT', 'notify')



provider = 'https://polygon-rpc.com'
web3 = Web3(Web3.HTTPProvider(provider))
log = Log()
line = LINE('test')
a = open('abi.json')
abi_swap = open('abi_swap.json')
ABI_LOAD = json.load(a)
ABI = ABI_LOAD["abi"]
ABI_LOAD_SWAP = json.load(abi_swap)
ABI_SWAP_MAIN = ABI_LOAD_SWAP["abi"]

contract_address_fandom = '0x683A77DFa820ADd8cd85cC723d6c0b4A5C8F5015'
contract_fandom = web3.eth.contract(address=contract_address_fandom, abi=ABI)
contract_address_swap = '0x8f76BF40f8CC3b8A7Fc4473154b4F6A06447C1aE'
contract_swap = web3.eth.contract(address=contract_address_swap, abi=ABI_SWAP_MAIN)
def balanceOf(account,name):
    try:
        address2 = Web3.to_checksum_address(account)
        balanceOf = contract_fandom.functions.balanceOf(address2).call()
        log.console(f"Check {name} have fdx:: {int(balanceOf / 1e18)}", color="green")
        return int(balanceOf / 1e18)
    except:
        log.console(f"{name} can not get FANDOM")
        return None
    
def check_matic(account, name):
    address2 = Web3.to_checksum_address(account)
    matic = web3.eth.get_balance(address2) / 10 ** 18
    log.console(f"Check {name} have matic:: {matic} wallet: {account}", color="green")
    return matic

def gas_fast():
    client = Legacy('test','test')
    response = client.gas_fast()
    if response != None:
        return int(float(response['result']['FastGasPrice']))

def rate_fee():
    try:
        result = contract_swap.functions.getSwapAmountsOut(web3.to_wei(1000, 'ether'),['0x683A77DFa820ADd8cd85cC723d6c0b4A5C8F5015','0x40F97Ec376aC1c503E755433BF57f21e3a49f440']).call()
        value = result[1] / 1e18
        rounded_value = math.floor(value * 100) / 100
        formatted_value = "{:.2f}".format(rounded_value)
        return float(value)
    except:
        # log.console(f"{name} Fail get price getSwapAmountsOut")
        return None
def getSwapAmountsOut(name,pandom_amount):
    
    try:
        log.console(f"{name} amount swap: {pandom_amount}",color='blue')
        result = contract_swap.functions.getSwapAmountsOut(web3.to_wei(pandom_amount, 'ether'),['0x683A77DFa820ADd8cd85cC723d6c0b4A5C8F5015','0x40F97Ec376aC1c503E755433BF57f21e3a49f440']).call()
        value = result[1] / 1e18
        percentage = 0.5 / 100
        result = value - (value * percentage)
        result_rounded = round(result, 2)
        log.console(f"Fee: {result_rounded}",color='blue')
        return web3.to_wei(result_rounded,'ether')
    except:
        log.console(f"{name} Fail get price getSwapAmountsOut")
        return None
    
def pandom_swap_to_cvtx(account,name,private_key):
    try:
        fandom = balanceOf(account,name)
        matic = check_matic(account,name)
        gas = gas_fast()
        
        if fandom != None and fandom >= 10000 and matic > 0.1:
            fee = getSwapAmountsOut(name,int(fandom))
            log.console(f'Start {name} swap FANDOM to CVTX',color='yellow')
            nonce = web3.eth.get_transaction_count(account)
            transaction = {
                'to': contract_address_swap,
                'chainId': 137,
                'gas': 300000,
                'gasPrice': web3.to_wei(gas + 50, 'gwei'),
                'nonce': nonce,
                'data': contract_swap.encodeABI(fn_name='swapExactTokensForTokens', args=[web3.to_wei(int(fandom),'ether'),fee,['0x683A77DFa820ADd8cd85cC723d6c0b4A5C8F5015','0x40F97Ec376aC1c503E755433BF57f21e3a49f440'],account,115792089237316195423570985008687907853269984665640564039457584007913129639935])
            }
            signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
            log.console(f'{name} Start send transaction',color='yellow')
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_hash_tohex = web3.to_hex(tx_hash)
            tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash_tohex)
            if tx_receipt['status'] == 1:
                log.console(
                    f'{name} transfer FDX to main wallet suscess transaction trx :: {tx_hash_tohex}',color="green")
                return True
            elif tx_receipt['status'] == 0:
                log.console(
                    f'{name} transfer FDX to main wallet false transaction trx :: {tx_hash_tohex}',color="red")
                return False
        else:
            log.console(f'{name} not have fandom',color='yellow')
            return False
    except Exception as inst:
        log.console('Process false send transaction',color="red")
        log.console(f"{inst}",color="red")
        return False

def main(wallet,name,rate,private_key):
    min = 0.00
    count = 0
    while True:
        result = rate_fee()
        if result and result != min:
            min = result
            # line.sendtext(f"Rate FANDOM to CVTX: {min}")
           
            log.console(f"Rate FANDOM to CVTX: {min} Rate swap : {rate}", color='yellow')
            if min >= float(rate):
               response = pandom_swap_to_cvtx(wallet,name,private_key)
               if response:
                   count = 0
               else:
                   print('Transaction Failed')
                #    line.sendtext(f"Transaction Failed")
                   count = count + 1
            
            if count == 2:
                break

        time.sleep(2)  

if __name__ == '__main__':
    if not WALLET :
        print('Please key wallet in file config.ini')
        os._exit(1)
    
    if not PRIVATE_KEY:
        print('Please key private key in file config.ini')
        os._exit(1)
    
    if not RATE:
        print('Please key rate in file config.ini')
        os._exit(1)
    
    print(f"Check wallet: {WALLET}  check rate: {RATE}")

    fandom = balanceOf(WALLET,'MAIN WALLET')

    t1 = threading.Thread(target=main, args=(WALLET,'MAIN WALLET',RATE,PRIVATE_KEY))

                    
    t1.start()
