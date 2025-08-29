'''Write a program to fill in a letter template given below with name and date.'''
letter = ''' Dear <|Name|>,
 Greetings from the Lord.
 Hare Krishna!
 <|Date|>'''

print(letter.replace('<|Name|>', 'Tirtha').replace('<|Date|>', '3rd march 2025')) 
        # replace() method is used to replace a string with another string.
                    

