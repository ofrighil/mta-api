from enum import Enum

class Service(Enum):
    A = 'A Eighth Avenue Express'
    C = 'C Eighth Avenue Local'
    E = 'E Eighth Avenue Local'

    B = 'B Sixth Avenue Express'
    D = 'D Sixth Avenue Express'
    F = 'F Queens Boulevard Express/Sixth Avenue Local'
    M = 'M Sixth Avenue Local'

    # G = 'g'

    # J = 'j'
    # Z = 'z'

    # N = 'n'
    # Q = 'q'
    # R = 'r'
    # W = 'w'

    # L = 'l'

    # ONE = '1'
    # TWO = '2'
    # THREE = 3'

    # FOUR = '4'
    # FIVE = '5'
    # SIX = '6'

    # SEVEN = '7'

    # SIR = 'si'


def convert_to_parameter(service: Service) -> str:
    match service:
        case Service.A | Service.C | Service.E:
            return '%2Fgtfs-ace'
        case Service.B | Service.D | Service.F | Service.M:
            return '%2Fgtfs-bdfm'
