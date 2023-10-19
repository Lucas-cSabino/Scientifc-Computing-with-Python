def arithmetic_arranger(problems, show_answer=False):
    lin1 = ""
    lin2 = ""
    lin3 = ""
    lin4 = ""

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        number1, operator, number2 = problem.split()

        if operator not in ('-', '+'):
            return "Error: Operator must be '+' or '-'."
   
        if not number1.isdigit() or not number2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(number1) > 4 or len(number2) > 4:
            return "Error: Numbers cannot be more than four digits." 
        
        max1 = max(len(number1), len(number2))
        lin1 += number1.rjust(max1 + 2) + "    "
        lin2 += operator + number2.rjust(max1 + 1) + "    "
        lin3 += "-" * (max1 + 2) + "    "
        if show_answer:
            result = str(eval(problem)).rjust(max1 + 2)
            lin4 += result + "    "

    arranged_problems = lin1.rstrip() + "\n" + lin2.rstrip() + "\n" + lin3.rstrip()

    if show_answer:
        arranged_problems += "\n" + lin4.rstrip()


    return arranged_problems