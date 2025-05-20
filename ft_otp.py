#!/usr/bin/env python3
import argparse
from colorama import Fore, Style
# import rsa


def banner():
   print(Fore.GREEN + Style.BRIGHT + r"""
  __ _            _         
 / _| |_     ___ | |_ _ __  
| |_| __|   / _ \| __| '_ \ 
|  _| |_   | (_) | |_| |_) |
|_|  \__|___\___/ \__| .__/ 
       |_____|       |_|    
""" + Style.RESET_ALL)
   
def generate_key(hex_string):
        try:
            if len(hex_string) != 64:
                print(Fore.RED + "Invalid hex string length" + Style.RESET_ALL)
            key = bytes.fromhex(hex_string)
            with open("ft_otp.key", "wb") as key_file:
                key_file.write(key)
            print(Fore.GREEN + "Key generated successfully" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid hex string" + Style.RESET_ALL)

def parse_args():
    parser = argparse.ArgumentParser(prog="./ft_otp", description="TOTP (Time-based One-Time Password) generator")
    parser.add_argument("-g", "--generate", type=str, help="Generate KEY from hex string")
    parser.add_argument("-k", "--key", type=str, help="Generate TOTP from KEY")
    return parser.parse_args()

if __name__ == "__main__":
    banner()
    args = parse_args()
    if args.generate:
        generate_key(args.generate)
