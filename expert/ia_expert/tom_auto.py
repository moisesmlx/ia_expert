def tom_automatico(n_cifra):

    list = ['A','A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 
                    'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    
    list_m = ['Am','A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 
                    'Am', 'A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m']

    tom = n_cifra
    new_tom = []
    cont = 0
    confirme = False
    if 'm' in str(tom):
        for item in list_m:
            if item == tom:
                confirme = True
            if confirme == True:
                new_tom.append(item)
                cont+=1
                if cont == 12:
                    break
        return new_tom
                
    else:
        for item in list:
            if item == tom:
                confirme = True
            if confirme == True:
                new_tom.append(item)
                cont+=1
                if cont == 12:
                    break
        return new_tom


#Detectar tom
def tom(check):

    detect_tom = ['A','A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 
            'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'
            'Am','A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 
            'Am', 'A#m', 'Bm', 'Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m']
    for item in detect_tom:
        texto = f'Tom: {item}'
        if texto in check:
            return item
        
        
if __name__ == '__main__':
    print(tom_automatico('B'))
