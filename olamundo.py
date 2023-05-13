
#minha função ola mundo

def olaMundo():
    txt = "olá,mundo !"
    print(f"{txt}")
    
    
olaMundo()

#de outra maneira

def ola(txt):
    from time import sleep
    for letra in txt:
        print(f'{letra}',end='',flush=True)
        sleep(0.2)


nome = "meu nome é python ! e adoro fazer prints !!!"

ola(nome)