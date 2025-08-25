import numpy as np
import itertools

def matrix_form(x):
    '''
    Input : x -> a string of operator
    Output: l -> a vector of length 2*size(x)
    '''
    if type(x) is not str:
        raise TypeError('x should be a string')
    
    n = len(x)
    l = np.zeros(2*n)
    
    for i,pos in zip(x, range(n)):
        if i == 'X':
            l[pos] = 1
        elif i == 'Z':
            l[n+pos] = 1 
        elif i == 'Y':
            l[pos] = 1
            l[n+pos] = 1
        elif i == 'I':
            pass
        else:
            raise Exception("x should only contain 'X', 'Y', 'Z', or 'I'")
            
    return l

def stab_form(l):
    '''
    Input : l -> a vector of length 2*size(s)
    Output: x -> a string of operator
    '''
    n = int(len(l)/2)
    s = ''
    for i in range(n):
        if l[i] == 1 and l[n+i] == 1:
            s=s+'Y'
        elif l[i] == 1 and l[n+i] == 0:
            s=s+'X'
        elif l[i] == 0 and l[n+i] == 1:
            s=s+'Z'
        else:
            s=s+'I'
    return s    

def symplectic_product(a, b):
    '''
    Input : a, b -> numpy array of even length with entries 0 or 1
    Output: 0 or 1 if [a,b]=0 or {a,b}=0 respectively
    '''
    if len(a) != len(b):
        raise Exception('length of a and b are not same')
    
    if len(a)%2 != 0:
        raise Exception('length of a and b are not even')
    
    l = len(a)
    n = int(l/2)
    a_x = a[0:n]
    a_z = a[n:l]
    b_x = b[0:n]
    b_z = b[n:l]
    
    s = sum(a_x*b_z + a_z*b_x)
    
    return s%2

def stabilizer_matrix(stab):
    '''
    Input : stab -> A list of stabilizer strings
    Ouptut: S_matrix -> A numpy matrix corresponding to input sabilizers
    '''
    
    l = len(stab)
    n = len(stab[0])
    
    S_matrix = np.zeros((l,2*n))
    for s, i in zip(stab, range(l)):
        S_matrix[i] = matrix_form(s)
        
    return S_matrix

def mat2stab(matrix):
    '''
    Input : matrix -> A check matrix
    Output: stab -> A list of stabilizer strings
    '''
    stab = []
    for i in matrix:
        s = stab_form(i)
        stab.append(s)    
    return stab

def weight(string):
    '''
    Input : string -> a string of operator
    Output: weight -> weight of operator
    '''
    weight = 0
    for char in string:
        if char != 'I':
            weight += 1
    
    return weight

def syndrome_lookup(x, s):
    '''
    Input : x -> a string of operator
            s -> a list operator strings
    Output: t -> a list of 0s and 1s each corresponding to one operator in s
    '''
    
    t = ''
    g1 = matrix_form(x)
    s_matrix = stabilizer_matrix(s)
    for g2 in s_matrix:
        t+=str(int(symplectic_product(g1, g2)))
    
    return t

def lookup_dictionary(errors, stabilizers):
    '''
    Input : errors -> an list of operator strings
            stabilizers  -> A list of stabilizer strings
    Output: lookup -> A dictionary with syndrome strings as keys and operator as value
            If len(output)<len(errors), some errors have same lookup
    '''
    
    lookup = {}
    for e in errors:
        lookup[syndrome_lookup(e, stabilizers)] = e
        
    return lookup

def single_qubit_errors(n):
    '''
    Input : n -> number of data qubits
    Output: errors -> list of one qubit errors on n encoded qubits
    '''
    errors = []
    for j in ['X','Y','Z']:
        for i in range(n):
            e = 'I'*(i)+j+'I'*(n-1-i)
            errors.append(e)

    return errors

def error_strings(n, r):
    '''
    Input : n -> number of data qubits
            r -> maximum number of error-ful qubits
    Output: errors -> list of two qubit errors on n encoded qubits
    '''    
    errors = []
    
    # Generate all combinations of positions for symbols
    for r in range(1, r + 1):
        for symbols in itertools.product(['X', 'Y', 'Z'], repeat=r):
            # Generate all combinations of symbols for the chosen positions
            for positions in itertools.combinations(range(n), r):
                # Generate string with 'I' at all positions except for chosen positions
                string = ['I'] * n
                for pos, symbol in zip(positions, symbols):
                    string[pos] = symbol
                errors.append(''.join(string))
    
    return errors

def upto_stabilizers(op, stab):
    '''
    Input : op -> a string of operator
            stab -> A list of stabilizer strings
    Output: t -> a list of operators equivalent to op upto stabilizers
    '''    
    op_row   = matrix_form(op)
    s_matrix = stabilizer_matrix(stab)
    n = len(s_matrix)
    new_ops = []
    recipe  = []
    for i in range(n + 1):
        combinations = itertools.combinations(range(n), i)
        for combination in combinations:
            recipe.append(combination)
            add_row = np.zeros(2*len(op))
            for i in combination:
                add_row+= s_matrix[i]
            new_op = (op_row+add_row)%2
            new_ops.append(stab_form(new_op))
            
    return  new_ops, recipe