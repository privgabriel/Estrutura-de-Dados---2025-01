def precedencia(operador):
    prioridades = {'not': 3, 'and': 2, 'or': 1}
    return prioridades.get(operador, 0) 

def eh_operador(token):
    return token in ('and', 'or', 'not')

def eh_booleano(token):
    return token in ('True', 'False')

def aplicar_operador(operador, operandos):
    if operador == 'not':
        if len(operandos) < 1:
            raise ValueError("Faltando operando para 'not'")
        val = operandos.pop()
        operandos.append(not val)
    elif operador in ('and', 'or'):
        if len(operandos) < 2:
            raise ValueError(f"Faltando operandos para '{operador}'")
        b = operandos.pop()
        a = operandos.pop()
        if operador == 'and':
            operandos.append(a and b)
        else:
            operandos.append(a or b)

def processar_operadores_ate_parenteses(operadores, operandos):
    while operadores and operadores[-1] != '(':
        aplicar_operador(operadores.pop(), operandos)
    if not operadores or operadores[-1] != '(':
        raise ValueError("Parênteses desbalanceados")
    operadores.pop()  # remove o '('

def processar_operadores_de_maior_precedencia(token, operadores, operandos):
    while (operadores and operadores[-1] != '(' and
           precedencia(operadores[-1]) >= precedencia(token)):
        aplicar_operador(operadores.pop(), operandos)
    operadores.append(token)

def avaliar_expressao(tokens):
    operadores = []
    operandos = []

    for token in tokens:
        if token == '(':
            operadores.append(token)
        elif token == ')':
            processar_operadores_ate_parenteses(operadores, operandos)
        elif eh_booleano(token):
            operandos.append(token == 'True')
        elif eh_operador(token):
            processar_operadores_de_maior_precedencia(token, operadores, operandos)
        else:
            raise ValueError(f"Token inválido: {token}")

    while operadores:
        if operadores[-1] == '(':
            raise ValueError("Parênteses desbalanceados")
        aplicar_operador(operadores.pop(), operandos)

    if len(operandos) != 1:
        raise ValueError("Expressão inválida")

    return operandos[0]

def quebrar_expressao(texto):
    return texto.replace('(', ' ( ').replace(')', ' ) ').split()

def main():
    expressao = "True or ( False and False )"
    tokens = quebrar_expressao(expressao)

    try:
        resultado = avaliar_expressao(tokens)
        print("Resultado:", resultado)
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()