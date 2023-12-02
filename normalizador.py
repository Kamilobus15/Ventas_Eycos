from Class.Comerciales import *

comercialesFinal = {
    'Mostrador Gabriel Paez ': Comerciales.GABRIEL,
    'Mostrador Judith Mateus ': Comerciales.JUDITH,
    'Mostrador Omaida Cuesta ': Comerciales.OMAYRA,
    'Mostrador David Sanchez ': Comerciales.DAVID,
    'Mostrador Jader Martinez ': Comerciales.JADER,
    'Mostrador Medellín ': Comerciales.MEDELLIN,
    'Mostrador Mariana Bustos ': Comerciales.MARIANA,
    'YEBELIS PAOLA CHARRIS MEZA ': Comerciales.BARRAQUILLA,
    'Mostrador STEFANY ': Comerciales.OTROS,
    'Mostrador Jorge Espitia ': Comerciales.OTROS,
    'Mostrador Alejandra Ibague ': Comerciales.OTROS,
    'Mostrador Juan Carlos ': Comerciales.BARRAQUILLA
}

def estandarVendedor(vendedor):
    for key, value in comercialesFinal.items():
        if key in vendedor:
            vendedor = value
            break
    return vendedor 