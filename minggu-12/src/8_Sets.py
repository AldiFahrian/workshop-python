basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
'orange' in basket                 # fast membership testing
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a   
a - b
a | b 
a & b 
a ^ b    
a = {x for x in 'abracadabra' if x not in 'abc'}
a