def calculator(firstOperand, secondOperand, operator):
    if operator == "+":
      return str(firstOperand + secondOperand)
    else:
      return str(firstOperand - secondOperand)

def arithmetic_arranger(problems, withResults = False):
    
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    firstOperands = []
    secondOperands = []
    operators = []
    results = []
    longestLens = []

    for problem in problems:
      splitProblem = problem.split()
      longestLens.append(max(len(splitProblem[0]), len(splitProblem[2])))

      if not splitProblem[0].isnumeric() or not splitProblem[2].isnumeric():
        return 'Error: Numbers must only contain digits.'  
        
      if len(splitProblem[0]) > 4 or len(splitProblem[2]) > 4:
        return 'Error: Numbers cannot be more than four digits.'

      if splitProblem[1] not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'."
        
      firstOperands.append(splitProblem[0])
      secondOperands.append(splitProblem[2])
      operators.append(splitProblem[1])
      results.append(calculator(int(splitProblem[0]), int(splitProblem[2]), splitProblem[1]))
      
    return formattingFunc(firstOperands, secondOperands, operators, longestLens, results, withResults)

def formattingFunc(firstOperands, secondOperands, operators, longestLens, results, withResults):
  
    formattedOperations = ''
  
    for idx, operand in enumerate(firstOperands):
      formattedOperations += f'{operand.rjust(longestLens[idx] + 2)}'
      
      if idx != len(firstOperands) - 1:
        formattedOperations += ' '*4
        
    formattedOperations += '\n'
  
    for idx, operand in enumerate(secondOperands):
      formattedOperations += f'{operators[idx]} {operand.rjust(longestLens[idx])}'
      
      if idx != len(firstOperands) - 1:
        formattedOperations += ' '*4
        
    formattedOperations += '\n'
  
    for idx, length in enumerate(longestLens):
      formattedOperations += f'{"-"*(length + 2)}'
      
      if idx != len(firstOperands) - 1:
        formattedOperations += ' '*4
   
    if withResults == True:
      
      formattedOperations += '\n'
      
      for idx, result in enumerate(results):
        formattedOperations += f'{result.rjust(longestLens[idx] + 2)}'
        
        if idx != len(firstOperands) - 1:
          formattedOperations += ' '*4
      
    return formattedOperations
      
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)