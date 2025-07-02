def all (logs):
  def devide (log):
    return log.split()[1].isdigit()
  
  letter = []
  number = []

  for log in logs:
    if devide(log):
      number.append(log)
    else:
      letter.append(log)

  
  letter.sort(key=lambda log: (
    log.split(" ", 1)[0],
    log.split(" ", 1)[1]
  ))
  return letter + number

logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero"
]
print(all(logs))
