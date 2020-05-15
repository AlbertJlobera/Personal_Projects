import pandas as pd
from argparse import ArgumentParser
from src.GlobalProduct import getInformationProduct
from src.SpecificProduct import infoProduct




def parse():
    parser=ArgumentParser(description="Activa Pythonium")
    parser.add_argument("--index",dest="index",type=int,help="Selecciona el número del índice del 0 al 4.")
    parser.add_argument("--precio",dest="precio",type=float,help="Indica el precio máximo que estás dispuesto a pagar.")
    return parser.parse_args()

def main():
    args=parse()
    index=args.index
    precio=args.precio
    Second_Step=infoProduct(index,precio)


if __name__ == '__main__':
    main()