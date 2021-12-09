def lalign(string, between = ''):
  return "{0:<50}".format(string) if between = '' else "{0:<" + between + "50}".format(string)

def ralign(string, between = ''):
  return "{0:>50}".format(string) if between = '' else "{0:>" + between + "50}".format(string)

def calign(string, between = ''):
  return "{0:^50}".format(string) if between = '' else "{0:^" + between + "50}".format(string)

def lrange(list, rangestart, rangeend):
  return list[rangestart:rangeend+1]

def rsort(list):
  return list.sort().reverse()

def tupadd(tup, index, value):
  list(tup).insert(index, value)
  return tuple(tup)

def tupremove(tup, index):
  del list(tup)[index]
  return tuple(tup)

def sallinc(set1, set2):
  return set1 & set2

def cexpress(condition, sen1, sen2):
  sen1 if condition else sen2
 
def clambda(sen, *args):
  return lambda tuple(args): sen

def br():
  print()

def cwf(path, text):
  open(path, 'w').write(text)

def readf(path, encod = 'utf-8'):
  return open(path, 'r', encoding = encod).read()

def awf(path, text):
  open(path, 'a').write(text)
  
def xwhenmod(sen):
  if __name__ == "__main__":sen
    
def error(sen, error):
  try:sen
  except:error

def nowt():
  return time.strftime('%Y-%m-%d %H:%m:%S (%A, %Z)', time.localtime(time.time()))

def wait(sec):
  sleep(sec)
