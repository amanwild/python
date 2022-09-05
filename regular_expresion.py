import re
# from typing import Sequence

block = '''Distributed network The 86698-89436 decentralized P2P architecture has nodes consisting of network participants where each member stores an identical copy of the Blockchain and is authorized to validate and certify digital transactions for the network
Shared ledger The members in the network record the ongoing digital 1 transactions into a shared ledger They run algorithms and verify the proposed transaction and once a majority of members validate the transaction it is added to the shared ledger
Digital transaction Any information or digital 1 asset that could be stored in a Blockchain could qualify as a digital transaction Each transaction is structured into a block and each block contains a cryptographic hash to add the transactions in a linear chronological order
'''
#this is a string

#meta characters 
# blocks = re.compile(r'ledger')#it create ledger (any) obj on which we can do operations 
# blocks = re.compile(r'.')   #it create any character on which we can do operations 
# blocks = re.compile(r'.er')   #it create any character on which we can do operations 
# blocks = re.compile(r'^Dis')   # ( '^ ' ) any character  that starts with 
# blocks = re.compile(r'er$')   # ( '^ ' ) any character  that end with 
# blocks = re.compile(r'o*')   # ( '* ' ) zero or more occurence o ke bad kuch bhi ho
# blocks = re.compile(r'as+')   # ( '+ ' ) one or more occurence a ke bad kitne bhi s ho
# blocks = re.compile(r'as{2}')   # ( '{} ' ) exactly specific no. of occurence 
# blocks = re.compile(r'(the){2}')   # ( '{} ' ) catch group of exactly specific no. of occurence 
# blocks = re.compile(r'as{1}| t')   # ( '{} ' ) exactly specific no. of occurence or t

# special Sequence
# blocks = re.compile(r'\A Distributed')# returns match if specific characters are at the begining of the string
# blocks = re.compile(r'r\B')# returns match if specific characters are not at the begining or end of the word
# blocks = re.compile(r'r\b')# returns match if specific characters are at the begining or end of the word
# blocks = re.compile(r'\d{10}')# returns match if string contain no. digits
blocks = re.compile(r'\d{5}-\d{5} ')# returns match if string contain no. digits
blocks = re.compile(r'\d{5} ')# returns match if string contain no. digits
# blocks = re.compile(r'Block\w')# returns match if string contains  words characters
# blocks = re.compile(r'a\W')# returns match if string contains  words characters

matches = blocks.finditer(block)#find operation
for match in matches:
    print(match)

