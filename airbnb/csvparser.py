def parse_csv(s):
    result = []
    current = ''
    i = 0
    in_quote = False
    while i < len(s):
        if not in_quote:
            if s[i] == '"':
                in_quote = True
            elif s[i] == ',':
                result.append(current)
                current = ''
            else:
                current += s[i]
        else:
            if s[i] == '"':
                if i != len(s) - 1 and s[i + 1] == '"':
                    current += '"'
                    i += 1
                else:
                    in_quote = False
            else:
                current += s[i]
        i += 1
    if current:
        result.append(current)
    return list_to_str(result)



def list_to_str(l):
    return '|'.join(l)


print parse_csv('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1"""Alexandra Alex"""')
