import pandas as pd
from argparse import ArgumentParser
from src.GlobalProduct import getInformationProduct
from src.SpecificProduct import infoProduct




def parse():
    parser=ArgumentParser(description="Activa Pythonium")
    parser.add_argument("--item",dest="item",type=str,help="Escribe detalladamente el producto que quieres.")
    parser.add_argument("--index",dest="index",type=int,help="Selecciona el número del índice del 0 al 4.")
    parser.add_argument("--precio",dest="precio",type=float,help="Indica el precio máximo que estás dispuesto a pagar.")
    return parser.parse_args()

def main():
    args=parse()
    item=args.item
    index=args.index
    precio=args.precio
    print('¡Te he enviado un email!')
    # Step 1
    First_step=getInformationProduct(item)   
    # Step 2
    Second_Step=infoProduct(index,precio)


if __name__ == '__main__':
    main()