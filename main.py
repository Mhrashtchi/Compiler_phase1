import pandas as pd
dfa_table=pd.read_csv('dfa_table.csv',index_col=0)
def Lexical_Analysis(data):
    print("input :",data)
    last_token = ''
    state = "S"
    data += '  '
    for i in data:
        if i == ' ':
            i = 'Space'
        if i != 'Space':
            last_token += i

        state = dfa_table.loc[state, i]
        #print(state)
        if state == "P1":
            print({"print": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "P2":
            print({"print": "Keyword"})
            last_token = ''

        if state == "W1":
            print({"While": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "W2":
            print({"print": "Keyword"})
            last_token = ''

        if state == "E1":
            print({"else": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "E2":
            print({"else": "Keyword"})
            last_token = ''

        if state == "EF1":
            print({"elif": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "EF2":
            print({"elif": "Keyword"})
            last_token = ''



        if state == "F1":
            print({"for": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "F2":
            print({"for": "Keyword"})
            last_token = ''

        if state == "I1":
            print({"if": "Keyword"})
            print({"(": "Open"})
            last_token = ''

        if state == "I2":
            print({"if": "Keyword"})
            last_token = ''

        if state == "D1":
            print({last_token.split('=')[0]: "Identifier"})
            print({"=": "Operator"})
            last_token = ''

        if state == "D2":
            print({last_token: "Identifier"})
            last_token = ''

        if state == "D3":
            print({last_token.split(')')[0]: "Identifier"})
            print({")": "Close"})
            last_token = ''

        if state == "D4":
            print({last_token.split('+')[0]: "Identifier"})
            print({"+": "Operator"})
            last_token = ''

        if state == "D5":
            print({last_token.split('-')[0]: "Identifier"})
            print({"-": "Operator"})
            last_token = ''

        if state == "Q23":
            print({last_token: "Operator"})
            last_token = ''

        if state == "Q24":
            print({last_token: "Operator"})
            last_token = ''

        if state == "Q25":
            print({last_token: "Open"})
            last_token = ''

        if state == "Q26":
            print({last_token: "Close"})
            last_token = ''

        if state == "Q30":
            if last_token.isdigit() or (last_token.startswith('-') and last_token[1:].isdigit()):
                print({last_token.split(' ')[0]: "Number"})
                last_token = ''

        if state == "Q31":
            print({last_token.split('+')[0]: "Number"})
            print({"+": "Operator"})
            last_token = ''

        if state == "Q32":
            print({last_token.split('-')[0]: "Number"})
            print({"-": "Operator"})
            last_token = ''

        if state == "Q33":
            print({last_token.split(')')[0]: "Number"})
            print({")": "Close"})
            last_token = ''

        if state == "Q34":
            print({last_token.split('+')[0]: "N number"})
            print({"+": "Operator"})
            last_token = ''

        if state == "Q35":
            print({last_token.split('-')[0]: "N number"})
            print({"-": "Operator"})
            last_token = ''

        if state == "Q36":
            print({last_token.split(')')[0]: "N number"})
            print({")": "Close"})
            last_token = ''

        if state == "ER1":
            print({last_token: "ERROR"})
            break

        if state == "ER2":
            print({last_token: "error"})
            print("identifier error")
            last_token = ''
            break




data="if (hashem==real) name=hashem  else name=reza    elif (GPA==19) job=full_stack_of_cbb else  job=nothing"
Lexical_Analysis(data)

print()
data="data=if (day==Saturday) mood=happy elif (day==Sunday) mood=relaxed else mood=neutral"
Lexical_Analysis(data)


print()
data="while (balance == 1000) balance = balance + 100 print(balance)"
Lexical_Analysis(data)


print()
data="for (i=1 i==3 i=i+1) for (j=1 j==3  j=j+1) print( i  j)"
Lexical_Analysis(data)


print()
data=" print 12z1 "
Lexical_Analysis(data)

print()
data="x = 5 + 3 + (10 + 4)"
Lexical_Analysis(data)





