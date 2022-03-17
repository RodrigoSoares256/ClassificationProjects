



def SeparaFaixaIdade(registro, idades = [15,25,35,45,55,65,75], faixas = ["15..25","25..35","35..45","45..55","55..65","65..75"]):
    
    #Self.idades
    #Self.faixas

    if registro < idades[0]:
        return 'Faixa 0..15'
    elif registro >= idades[len(idades)-1]:
        return "faixa >= 75"
    else:
        for i in range(len(idades)-1):
            if registro >= idades[i] and registro < idades[i+1]:
                return faixas[i]