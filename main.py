import pandas as pd
from argparse import ArgumentParser
from src.GlobalProduct import getInformationProduct



# ex: python3 main.py --item 'MacBook Air 13' --user  --email 


def parse():
    parser=ArgumentParser(description="Activa Pythonium")
    parser.add_argument("--item",dest="item",type=str,help="Escribe detalladamente el producto que quieres.")
    parser.add_argument("--user",dest="user",type=str,help="Escribe tu nombre")
    parser.add_argument("--email",dest="email",type=str,help="Escribe tu email")
    return parser.parse_args()

def main():
    args=parse()
    item=args.item
    user=args.user
    email=args.email
    First_step=getInformationProduct(item,user,email)   



if __name__ == '__main__':
    main()