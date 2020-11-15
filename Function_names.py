x=5
print("Hello")

def print_lyrics() :
    print("I'm a lumberjack and I'm OK")
    print("I sleep all night and I work all day")

print ("Yo")
print_lyrics()
x=x+2
print(x)

def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    else :
        return 'Hello'

print (greet('en'),'Glenn')
print (greet('es'),'Sally') 
print (greet('fr'),'Michael')

def addtwo(a,b) :
    added = a+b 
    return added 

x = addtwo(3,5)
print(x)
