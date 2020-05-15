import pandas as pd
from argparse import ArgumentParser
from src.GlobalProduct import getInformationProduct
from src.SpecificProduct import infoProduct




def parse():
    parser=ArgumentParser(description="Activa Pythonium")
    parser.add_argument("--item",dest="item",type=str,help="Escribe detalladamente el producto que quieres.")

    return parser.parse_args()

def main():
    args=parse()
    item=args.item

    First_step=getInformationProduct(item)   



if __name__ == '__main__':
    main()