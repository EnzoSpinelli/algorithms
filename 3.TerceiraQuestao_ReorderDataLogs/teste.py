def reorderLogFiles(logs):
    # Função auxiliar: retorna True se for digit-log
    def is_digit_log(log):
        # separa em duas partes: identificador + resto
        return log.split()[1].isdigit()

    # 1) Separa em duas listas
    letter_logs = []
    digit_logs = []
    for log in logs:
        if is_digit_log(log):
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    # 2) Ordena os letter-logs
    #    key = (conteúdo, identificador)
    letter_logs.sort(key=lambda log: (
        log.split(' ', 1)[1],   # tudo após o primeiro espaço
        log.split(' ', 1)[0]    # o identificador
    ))

    # 3) Reconstrói: letter-logs ordenados + digit-logs na ordem original
    return letter_logs + digit_logs

# Exemplo de uso:
logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero"
]
print(reorderLogFiles(logs))
