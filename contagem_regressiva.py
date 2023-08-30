def contagem_regressiva_recursiva(comeca_em:int = 10, termina_em: int = 0) -> int:

    contagem regressiva iniciado em 'comeca_em' e terminando em 'termina_em'
    print(comeca_em)

    #caso-base
    if comeca_em <= termina_em:
        #perceba que aqui um valor real é retornado e não há mais recursão
    return comeca_em

    #caso recursivo
    #Esse código será executado sempre, até
    #'comeca_em' se tornar menor ou igual a 'termina_em'
    return contagem_regressiva_recursiva(comeca_em - 1)

if __name__ =="__main__":
    contagem_regressiva_recursiva()