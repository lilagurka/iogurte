#loteria, Heverton 12/04/2019
palpite = '1234567'
vidas = 9
import random

lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','U','V','W','X','Y','Z',]
l1 = random.choice(lista)
l2= random.choice(lista)
l3= random.choice(lista)
l4= random.choice(lista)
l5= random.choice(lista)
l6= random.choice(lista)
senha =  (l1 + l2 + l3+  l4 + l5 + l6 )
p1 = '_'
p2= '_'
p3= '_'
p4= '_'
p5= '_'
p6= '_'

while True:

    
    print ('você tem ',vidas,' vidas \n ')
    
    if vidas == 0:
        print('Você perdeu :(' )
        print ('A senha era: ',senha)
        print('------------------- \n Fim de jogo')
        break
    
    while len(palpite) !=6:
        print('Qual você acha que é a senha?\n   ',p1,p2,p3,p4,p5,p6)
        palpite = str(input('-->')).upper()
        if   len(palpite) != 6:
            print("Seu palpite deve ter 6 Digitos")
            
            
            
        
    if palpite[0] == senha[0]: p1 = senha[0]
    if palpite[1] == senha[1]: p2 = senha[1]
    if palpite[2] == senha[2]: p3 = senha[2]
    if palpite[3] == senha[3]: p4 = senha[3]
    if palpite[4] == senha[4]: p5 = senha[4]
    if palpite[5] == senha[5]: p6 = senha[5]
        
        




#=====================================
    if (palpite == senha):
        print ('Você Acertou a senha :)')
        print (senha)
        print ('-------------------------------- \n Fim de jogo')
        
        break    
    
    if palpite.count('A')  > 0 :    
        print ('Você acertou a letra "A" {}  vezes' .format(senha.count('A')))
        if (palpite.find('A') == senha.find('A')):
            print ('está na casa certa')
        
    if palpite.count('B')  > 0 :
        print ('Você acertou a letra "B {}  vezes' .format(senha.count('B')))
        if (palpite.find('B') == senha.find('B')):
            print (' B está na casa certa')
            
    if palpite.count('C')  > 0 :
        print ('Você acertou a letra "C" {}  vezes' .format(senha.count('C')))
        if (palpite.find('C') == senha.find('C')):
            print ('C está na casa certa')
        
    if palpite.count('D')  > 0 :
        print ('Você acertou a letra "D" {}  vezes' .format(senha.count('D')))
        if (palpite.find('D') == senha.find('D')):
            print ('D está na casa certa')
            
    if palpite.count('E')  > 0 :
        print ('Você acertou a letra "E" {}  vezes' .format(senha.count('E')))
        if (palpite.find('E') == senha.find('E')):
            print ('E está na casa certa')
            
    if palpite.count('F')  > 0 :
        print ('Você acertou a letra "F" {}  vezes' .format(senha.count('F')))
        if (palpite.find('F') == senha.find('F')):
            print ('F está na casa certa')
            
    if palpite.count('G')  > 0:
        print ('Você acertou a letra "G" {}  vezes' .format(senha.count('G')))
        if (palpite.find('G') == senha.find('G')):
            print ('G está na casa certa')
            
    if palpite.count('H')  > 0 :
        print ('Você acertou a letra "H" {}  vezes' .format(senha.count('H')))
        if (palpite.find('H') == senha.find('H')):
            print (' H está na casa certa')
            
    if palpite.count('I')  > 0 :
        print ('Você acertou a letra "I" {}  vezes' .format(senha.count('I')))
        if (palpite.find('I') == senha.find('I')):
            print ('i está na casa certa')
            
    if palpite.count('J')  > 0 :
        print ('Você acertou a letra "J" {}  vezes' .format(senha.count('J')))
        if (palpite.find('J') == senha.find('J')):
            print ('está na casa certa')
            
    if palpite.count('K')  > 0 :
        print ('Você acertou a letra "K" {}  vezes' .format(senha.count('K')))
        if (palpite.find('K') == senha.find('K')):
            print ('K está na casa certa')
    if palpite.count('L')  > 0 :
        print ('Você acertou a letra "L" {}  vezes' .format(senha.count('L')))
        if (palpite.find('L') == senha.find('L')):
            print ('L está na casa certa')
            
    if palpite.count('M')  > 0 :
        print ('Você acertou a letra "M" {}  vezes' .format(senha.count('M')))
        if (palpite.find('M') == senha.find('M')):
            print ('está na casa certa')
            
    if palpite.count('N')  > 0:
        print ('Você acertou a letra "N" {}  vezes' .format(senha.count('N')))
        if (palpite.find('N') == senha.find('N')):
            print ('está na casa certa')
            
    if palpite.count('O')  > 0:
        print ('Você acertou a letra "O" {}  vezes' .format(senha.count('O')))
        if (palpite.find('O') == senha.find('O')):
            print (' O está na casa certa')
            
    if palpite.count('P')  > 0:
        print ('Você acertou a letra "P" {}  vezes' .format(senha.count('P')))
        if (palpite.find('P') == senha.find('P')):
            print ('P está na casa certa')
            
    if palpite.count('Q')  > 0:
        print ('Você acertou a letra "Q" {}  vezes' .format(senha.count('Q')))
        if (palpite.find('Q') == senha.find('Q')):
            print ('está na casa certa')
            
    if palpite.count('R')  > 0:
        print ('Você acertou a letra "R" {}  vezes' .format(senha.count('R')))
        if (palpite.find('R') == senha.find('R')):
            print ('R está na casa certa')
            
    if palpite.count('S')  > 0:
        print ('Você acertou a letra "S" {}  vezes' .format(senha.count('S')))
        if (palpite.find('S') == senha.find('S')):
            print ('S está na casa certa')
            
    if palpite.count('T')  > 0:
        print ('Você acertou a letra "T" {}  vezes' .format(senha.count('T')))
        if (palpite.find('T') == senha.find('T')):
            print ('T está na casa certa')
            
    if palpite.count('U')  > 0:
        print ('Você acertou a letra "U" {}  vezes' .format(senha.count('U')))
        if (palpite.find('U') == senha.find('U')):
            print ('U Está na casa certa')
            
    if palpite.count('V')  > 0:
        print ('Você acertou a letra "V" {}  vezes' .format(senha.count('V')))
        if (palpite.find('V') == senha.find('V')):
            print (' V  está na casa certa')
            
    if palpite.count('W')  > 0:
        print ('Você acertou a letra "W" {}  vezes' .format(senha.count('W')))
        if (palpite.find('W') == senha.find('W')):
            print (' W está na casa certa')
            
    if palpite.count('X')  > 0:
        print ('Você acertou a letra "X" {}  vezes' .format(senha.count('X')))
        if (palpite.find('X') == senha.find('X')):
            print (' X está na casa certa')
            
    if palpite.count('Y')  > 0:
        print ('Você acertou a letra "Y" {}  vezes' .format(senha.count('Y')))
        if (palpite.find('Y') == senha.find('Y')):
            print (' Y está na casa certa')
            
    if palpite.count('Z')  > 0:
        print ('Você acertou a letra "Z" {}  vezes' .format(senha.count('Z')))
        if (palpite.find('Z') == senha.find('Z')):
            print (' Z está na casa certa')
        
    print('-'*40)
    palpite = '0123456789'
    vidas =  vidas -1
    



