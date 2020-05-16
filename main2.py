import pandas as pd
from argparse import ArgumentParser
from src.SpecificProduct import infoProduct

#python3 main2.py --index <index> --precio <precio> --user <user> --email <email>

def parse():
    parser=ArgumentParser(description="Activa Pythonium")
    parser.add_argument("--index",dest="index",type=int,help="Selecciona el número del índice del 0 al 4.")
    parser.add_argument("--precio",dest="precio",type=float,help="Indica el precio máximo que estás dispuesto a pagar.")
    parser.add_argument("--user",dest="user",type=str,help="Escribe tu nombre")
    parser.add_argument("--email",dest="email",type=str,help="Escribe tu email")
    return parser.parse_args()

def main():
    args=parse()
    index=args.index
    precio=args.precio
    user=args.user
    email=args.email
    Second_Step=infoProduct(index,precio,user,email)


if __name__ == '__main__':
    main()