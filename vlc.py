from array_heap import *
import math
"""
Author: Brandon Calabrese
"""

"""Defines the Symbol object"""
class Symbol(struct):
    _slots = ((str, 'name'),(int, 'freq'),(str, 'code'))
    
"""Defines the Node object"""
class Node(struct):
    _slots = ((int, 'freq'), (list, 'symbols'))

"""Returns the node with the lowest requency of the two being sent in"""
def compareFunc(node1, node2):
    return node1.freq < node2.freq

"""Returns a boolean, whether or not a list of Symbols contains a Symbol with name equal to character"""
def contains(lst, character):
    for element in lst:
        if element.name == character:
            return True
    return False

"""Returns a Symbol object from a list that has a name equal to character"""
def get(lst, character):
    for element in lst:
        if element.name == character:
            return element
    return None

"""Returns the Average VLC codeword length, takes a list of Symbols"""
def AVG(symbols):
    num = 0
    den = 0
    for s in symbols:
        num += len(s.code) * s.freq
    for s in symbols:
        den += s.freq
    return num / den

"""Returns the Average fixed-length codeword length, takes a list of Nodes"""
def FCL(nodes):
    return math.ceil(math.log(len(nodes)))

"""Prompts the user for filename and generates chart of values, calls other functions"""
def main():
    file = open(input("Please enter symbol firename: "))

    symbols = []
    for line in file:
        line = line.strip()      
        for c in line:
            if contains(symbols, c):
                get(symbols, c).freq += 1
            else:
                symbols.append(Symbol(c,1,""))
                
    nodes = []
    for s in symbols:
        nodes.append(Node(s.freq, [s]))

    h = createEmptyHeap(len(nodes), compareFunc)

    for i in nodes:
        add(h, i)

    while h.size > 1:
        n1 = peek(h)
        removeMin(h)
        n2 = peek(h)
        removeMin(h)

        for s in n1.symbols:
            s.code = "0" + s.code
        for s in n2.symbols:
            s.code = "1" + s.code

        newNode = Node(n1.freq + n2.freq, n1.symbols + n2.symbols)
        add(h, newNode)
        
    print()
    print("Variable Length Code Output")
    print("-" * 40)

    for el in peek(h).symbols:
        print('Symbol: %2s   ' % el.name, end='')
        print('Codeword: %8s   ' % el.code, end='')
        print('Frequency: %5d   ' % el.freq)

    print()
    print("Average VLC codeword length: " + str(AVG(peek(h).symbols)) + " bits per symbol")
    print("Average Fixed length codeword length: " + str(FCL(nodes)) + " bits per symbol")
    
main()
