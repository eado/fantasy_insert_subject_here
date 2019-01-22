import re
import math
import random

# Helper functions
def closestNumber(n, m) : 
    q = int(n / m) 
      
    n1 = m * q 
      
    if((n * m) > 0) : 
        n2 = (m * (q + 1))  
    else : 
        n2 = (m * (q - 1)) 
      
    if (abs(n - n1) < abs(n - n2)) : 
        return n1 
      
    return n2 



def gen_question(question_string):
    res = re.findall("({[^.}]+})+", question_string)
    blanks = []

    for request in res:
        request = request[1:-1]
        req = request.split(":")
        if req[0] == 'int':
            if '*' not in req[1]:
                values = req[1].split("-")
                blanks.append(random.randint(int(values[0]), int(values[1])))
            else:
                params = req[1].split("*")
                multi = params[1]
                values = params[0].split("-")
                ls = []
                i = closestNumber(int(values[0]), int(multi))
                while (i < int(values[1])):
                    ls.append(i)
                    i += int(multi)

                index = random.randint(0, len(ls)-1)
                blanks.append(ls[index])

    regex = re.compile("({[^.}]+})+", re.S)

    def ret_and_rep(match):
        index = res.index(match.group())
        res[index] = None

        return str(blanks[index])

    return re.sub(regex, ret_and_rep, question_string), blanks


def gen_answer(answer_string, b):
    exec('global i; i = %s' % answer_string)
    global i
    return i


stri = input()

question, blanks = gen_question(stri)
print(question)

stra = input()

print(gen_answer(stra, blanks))
