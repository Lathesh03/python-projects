# Logic Gates Implementation in Python

# AND gate: returns 1 if both inputs are 1
def AND(a, b):
    return a & b   # bitwise AND operator

# OR gate: returns 1 if at least one input is 1
def OR(a, b):
    return a | b   # bitwise OR operator

# NOT gate: returns the opposite of the input
def NOT(a):
    return int(not a)   # "not" returns True/False → convert to int (1/0)

# NAND gate: returns the opposite of AND
def NAND(a, b):
    return NOT(AND(a, b))

# NOR gate: returns the opposite of OR
def NOR(a, b):
    return NOT(OR(a, b))

# XOR gate: returns 1 if inputs are different
def XOR(a, b):
    return a ^ b   # bitwise XOR operator

# XNOR gate: returns 1 if inputs are the same
def XNOR(a, b):
    return NOT(XOR(a, b))

# --- MAIN PROGRAM ---

# All possible input combinations for 2 inputs
inputs = [(0,0), (0,1), (1,0), (1,1)]

# Print header row for truth table
print("A B | AND OR NAND NOR XOR XNOR")
print("-"*30)


# Loop through all input combinations and evaluate each gate
for a, b in inputs:
    print(f"{a} {b} |  {AND(a,b)}    {OR(a,b)}    {NAND(a,b)}    {NOR(a,b)}    {XOR(a,b)}    {XNOR(a,b)}")

# Test NOT gate separately (since it has only one input)
print("\nNOT Gate:")
for a in [0,1]:
    print(f"NOT {a} = {NOT(a)}")
