import time

num_ls = ["0","1","2","3","4","5","6","7","8","9"]
func_ls = ["^","/","*","-","+"]
char_ls = ["."]
exit_ls = ["Exit","End","Done","Finish"]
lbracket_ls = ["(","[","{","<"]
rbracket_ls = [")","]","}",">"]
all_ls = num_ls + func_ls + char_ls + exit_ls + lbracket_ls + rbracket_ls

def check_errors(ip, ipls, func_ls, all_ls):
    errors = []
    #CHAR_ERROR
    char_error = False
    loopcnt = 0
    while(loopcnt < len(ipls) and char_error == False):
        char = ipls[loopcnt]
        if (char not in all_ls and ip not in exit_ls):
            char_error = True
        loopcnt += 1
    errors.append(char_error)
    #FUNC_ERROR
    if ((ipls[0] in func_ls) or (ipls[len(ipls) - 1] in func_ls)):
            func_error = True
    else:
        func_error = False
        loopcnt = 1
        while(loopcnt < len(ipls) and func_error == False):
            if (ipls[loopcnt] in func_ls and (ipls[loopcnt - 1]) in func_ls):
                func_error = True
            loopcnt += 1
    errors.append(func_error)
    return(errors)

def check_brackets(ipls, lbracket_ls, rbracket_ls):
    loopcnt = 0
    lbracket_cnt = 0
    rbracket_cnt = 0
    lbracket_checkls = [0,0,0,0]
    rbracket_checkls = [0,0,0,0]
    next_rbracket = ""
    bracket_error = False
    while (loopcnt < len(ipls) and bracket_error == False):
        bracket_check = ipls[loopcnt]
        if (bracket_check in lbracket_ls):
            lbracket_checkls[lbracket_ls.index(bracket_check)] += 1
            next_rbracket = rbracket_ls[lbracket_ls.index(bracket_check)]
            lbracket_cnt += 1
        elif (bracket_check in rbracket_ls):
            rbracket_checkls[rbracket_ls.index(bracket_check)] += 1
            if (bracket_check != next_rbracket or (ipls[ipls.index(bracket_check) - 1] == lbracket_ls[rbracket_ls.index(bracket_check)])):
                bracket_error = True
            rbracket_cnt += 1
        loopcnt += 1
    if (lbracket_checkls == rbracket_checkls and bracket_error == False):
        bracket_cnt = lbracket_cnt
    else:
        bracket_error = True
        bracket_cnt = 0
    loopcnt = 0
    while (loopcnt < len(ipls)):
        if(ipls[loopcnt] in lbracket_ls and ipls[(loopcnt - 1)] not in func_ls and ipls[(loopcnt - 1)] not in lbracket_ls):
            ipls.insert(loopcnt, "*")
        loopcnt += 1
    loopcnt = 0
    while (loopcnt < (len(ipls) - 1)):
        if(ipls[loopcnt] in rbracket_ls and ipls[(loopcnt + 1)] not in func_ls and ipls[(loopcnt + 1)] not in rbracket_ls):
            ipls.insert((loopcnt + 1), "*")
        loopcnt += 1
    if(ipls[0] == "*"):
        ipls.pop(0)
    if(ipls[0] == "*"):
        ipls.pop(len(ipls-1))
    return [bracket_error, bracket_cnt, ipls]
        

def find_expression(ipls):
    loopcnt = len(ipls) - 1
    element = ""
    while (loopcnt >= 0 and element not in lbracket_ls):
        element = ipls[loopcnt]
        loopcnt -= 1
    lbracket = element
    rbracket = rbracket_ls[lbracket_ls.index(lbracket)]
    loopcnt += 1
    expression = ""
    while (loopcnt < len(ipls) and element != rbracket):
        element = ipls[loopcnt]
        expression = expression + str(element)
        loopcnt += 1
    expression_ls = list(expression)
    expression_ls.remove(lbracket)
    expression_ls.remove(rbracket)
    loopcnt = 0
    expression = ""
    while (loopcnt < len(expression_ls)):
        expression = expression + expression_ls[loopcnt]
        loopcnt += 1
    return(expression)

def look_for_funcs(ipls, func_ls):
    loopcnt = 0
    func_todo = []
    while(loopcnt < len(ipls)): 
        element = ipls[loopcnt]
        loopcnt += 1
        if (element in func_ls):
            func_todo.append(element)
    return(func_todo)

def organise_BODMAS(func_todo, func_ls):
    loopcnt = 0
    check_func = 0
    organised_func_todo = []
    while(loopcnt < len(func_todo)):
        while(check_func < len(func_ls)):
            while(func_ls[check_func] in func_todo):
                organised_func_todo.append(func_ls[check_func])
                func_todo.remove(func_ls[check_func])
            check_func += 1
        loopcnt += 1
    return (organised_func_todo)

def create_equation_ls(ipls, func_todo):
    loopcnt = 0
    func_cnt = 0
    equation_ls = []
    while (func_cnt < len(func_todo)):
        part = ""
        while (ipls[loopcnt] != func_todo[func_cnt]):
            part = part + str(ipls[loopcnt])
            loopcnt += 1
        equation_ls.append(part)
        part = ipls[loopcnt]
        equation_ls.append(part)
        loopcnt += 1
        func_cnt += 1
    part = ""
    while (loopcnt < len(ipls)):
        part = part + str(ipls[loopcnt])
        loopcnt += 1
    equation_ls.append(part)
    return(equation_ls)

def show_calculation(equation_ls):
    op = ""
    loopcnt = 0
    while(loopcnt < len(equation_ls)):
        op = op + str(equation_ls[loopcnt])
        loopcnt += 1
    print("=" , op)

#def replace_ans()
    
def calculate(equation_ls, func_todo, math_error):
    loopcnt = 0
    func_cnt = 0
    while (func_cnt < len(func_todo)):
        cur_func = func_todo[func_cnt]
        num_1_index = equation_ls.index(cur_func) - 1
        num_2_index = equation_ls.index(cur_func) + 1
        num_1 = float(equation_ls[num_1_index])
        num_2 = float(equation_ls[num_2_index])
        if (cur_func == "^"):
            ans = num_1 ** num_2
        elif (cur_func == "/"):
            if (num_2 != 0):
                ans = num_1 / num_2
            else:
                math_error = True
                ans = 1
                return[ans, math_error]
        elif (cur_func == "*"):
            ans = num_1 * num_2
        elif (cur_func == "+"):
            ans = num_1 + num_2
        elif (cur_func == "-"):
            ans = num_1 - num_2
        #print(num_1 , cur_func , num_2 , "=" , ans)
        equation_ls[equation_ls.index(cur_func)] = ans
        equation_ls.pop(num_2_index)
        equation_ls.pop(num_1_index)
        func_cnt += 1
    ans = equation_ls[0]
    return[ans, math_error]

def replace_brackets(ipls, ans):
    loopcnt = len(ipls) - 1
    bracket_check = ""
    while (loopcnt >= 0 and bracket_check not in lbracket_ls):
        bracket_check = ipls[loopcnt]
        loopcnt -= 1
    loopcnt += 1
    lbracket = bracket_check
    lbracket_index = loopcnt
    rbracket = rbracket_ls[lbracket_ls.index(lbracket)]
    while (loopcnt < len(ipls) and bracket_check != rbracket):
        bracket_check = ipls[loopcnt]
        ipls.pop(loopcnt)
    ipls.insert(lbracket_index, ans)
    return(ipls)


ip = ""
prev_ans = 0
while(ip not in exit_ls):
    print("Enter formula:")
    ip = str(input(""))
    ipls = list(ip)
    errors = check_errors(ip, ipls, func_ls, all_ls)
    bracket_state = check_brackets(ipls, lbracket_ls, rbracket_ls)
    bracket_error = bracket_state[0]
    errors.append(bracket_error)
    math_error = False
    errors.append(math_error)
    if(errors[0] == False and errors[1] == False and errors[2] == False):
        bracket_cnt = bracket_state[1]
        ipls = bracket_state[2]
        print_ans = bracket_cnt
        while(bracket_cnt > 0 and math_error == False):
            expression = find_expression(ipls)
            expression_ls = list(expression)
            func_todo = look_for_funcs(expression_ls, func_ls)
            expression_ls = create_equation_ls(expression_ls, func_todo)
            func_todo = organise_BODMAS(func_todo, func_ls)
            math_error = errors[3]
            calculate_return = calculate(expression_ls, func_todo, math_error)
            ans = calculate_return[0]
            errors[3] = calculate_return[1]
            ipls = replace_brackets(ipls, ans)
            if(errors[3] == False):
                show_calculation(ipls)
            bracket_cnt -= 1
        func_todo = look_for_funcs(ipls, func_ls)
        equation_ls = create_equation_ls(ipls, func_todo)
        func_todo = organise_BODMAS(func_todo, func_ls)
        math_error = errors[3]
        calculate_return = calculate(equation_ls, func_todo, math_error)
        ans = calculate_return[0]
        math_error = calculate_return[1]
        errors[3] = math_error
    if(errors[0] == True):
        print("----CHARACTER ERROR----")
    elif(errors[1] == True):
        print("----FUNCTION ERROR----")
    elif(errors[2] == True):
        print("----BRACKET ERROR----")
    elif(errors[3] == True):
        print("----MATH ERROR----")
    elif (ip in exit_ls):
        print("--------")
    else:
        print("=" , ans)
        prev_ans = ans
        print("")
        time.sleep(2)















