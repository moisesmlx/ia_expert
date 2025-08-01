# _*_ coding:utf-8 _*_

from time import sleep
from ia_expert.trans_A import *
from ia_expert.trans_Am import *
from ia_expert.trans_Astm import *
from ia_expert.trans_Ast import *
from ia_expert.trans_B import *
from ia_expert.trans_Bm import *
from ia_expert.trans_C import *
from ia_expert.trans_Cm import *
from ia_expert.trans_Cst import *
from ia_expert.trans_Cstm import *
from ia_expert.trans_D import *
from ia_expert.trans_Dm import *
from ia_expert.trans_Dst import *
from ia_expert.trans_Dstm import *
from ia_expert.trans_E import *
from ia_expert.trans_Em import *
from ia_expert.trans_F import *
from ia_expert.trans_Fm import *
from ia_expert.trans_Fst import *
from ia_expert.trans_Fstm import *
from ia_expert.trans_G import *
from ia_expert.trans_Gm import *
from ia_expert.trans_Gst import *
from ia_expert.trans_Gstm import *
#from ia_expert.enviar_file import *
#from ia_expert.pdf import *
from time import sleep
#from ia_expert.escala import *
from PIL import Image
from ia_expert.tom_auto import tom_automatico, tom
from ia_expert.zipp import zipp
from django.conf import settings
from ia_expert import remove

        
def translate_auto(original, mudado, n_cifra, text_area, decode):
        tom_original = original
        if original == '':
            tom_original = tom(text_area)
        #Automatizar troca de escalas
        if str(mudado) == '' and str(tom_original) != '' or str(n_cifra) != '':
            for item in tom_automatico(tom_original):
                try:
                            
                    if tom_original.upper() == 'A' and item.upper() != 'A':
                                
                        Trans_A(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Am' and item.upper() != 'Am':
                                
                        Trans_Am(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'A#' and item.upper() != 'A#':
                                
                        Trans_Ast(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'A#m' and item.upper() != 'A#m':
                                
                        Trans_Astm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'B' and item.upper() != 'B':
                                
                        Trans_B(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Bm' and item.upper() != 'Bm':
                                
                        Trans_Bm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'C' and item.upper() != 'C':
                                
                        Trans_C(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                                    
                    if tom_original == 'Cm' and item.upper() != 'Cm':
                                
                        Trans_Cm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'C#' and item.upper() != 'C#':
                                
                        Trans_Cst(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'C#m' and item.upper() != 'C#m':
                                
                        Trans_Cstm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'D' and item.upper() != 'D':
                                
                        Trans_D(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Dm' and item.upper() != 'Dm':
                                
                        Trans_Dm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'D#' and item.upper() != 'D#':
                                
                        Trans_Dst(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'D#m' and item.upper() != 'D#m':
                                
                        Trans_Dstm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'E' and item.upper() != 'E':
                                
                        Trans_E(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Em' and item.upper() != 'Em':
                                
                        Trans_Em(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'F' and item.upper() != 'F':
                                
                        Trans_F(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Fm' and item.upper() != 'Fm':
                                
                        Trans_Fm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'F#' and item.upper() != 'F#':
                                
                        Trans_Fst(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'F#m' and item.upper() != 'F#m':
                                
                        Trans_Fstm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'G' and item.upper() != 'G':
                                
                        Trans_G(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'Gm' and item.upper() != 'Gm':
                                
                        Trans_Gm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original.upper() == 'G#' and item.upper() != 'G#':
                                
                        Trans_Gst(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                    if tom_original == 'G#m' and item != 'G#m':
                                
                        Trans_Gstm(f'{n_cifra} tom {item}', tom_original, item, text_area, decode)
                                
                                
                    if tom_original == item:
                        with open(fr'./ia_expert/Minhas_cifras/{n_cifra} tom {item}.txt', 'w', encoding='utf-8') as texto:
                            texto.write(text_area)
                        with open(fr'./cifras/{decode}{n_cifra} tom {item}.txt', 'w', encoding='utf-8') as arquivo:
                                arquivo.write(text_area)
                                  
                except Exception as error:
                    print(error)
            zipp(n_cifra, decode)
                        
        if str(tom_original) == '' or str(n_cifra) == '':
                pass
            
        
def translate(original, mudado, n_cifra, text_area, decode):
            # Um só tom
            tom_original = original
            if str(n_cifra) != '' and str(mudado) != '' and str(tom_original) != '':
                
                    try:  
                        
                        if tom_original.upper() == 'A':
                            
                            Trans_A(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Am':
                            
                            Trans_Am(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'A#':
                            
                            Trans_Ast(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'A#m':
                            
                            Trans_Astm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'B':
                            
                            Trans_B(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Bm':
                            
                            Trans_Bm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'C':
                            
                            Trans_C(n_cifra, tom_original, mudado, text_area, decode)
                                                
                        if tom_original == 'Cm':
                            
                            Trans_Cm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'C#':
                            
                            Trans_Cst(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'C#m':
                            
                            Trans_Cstm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'D':
                            
                            Trans_D(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Dm':
                            
                            Trans_Dm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'D#':
                            
                            Trans_Dst(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'D#m':
                            
                            Trans_Dstm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'E':
                            
                            Trans_E(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Em':
                            
                            Trans_Em(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'F':
                            
                            Trans_F(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Fm':
                            
                            Trans_Fm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'F#':
                            
                            Trans_Fst(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'F#m':
                            
                            Trans_Fstm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'G':
                            
                            Trans_G(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original == 'Gm':
                            
                            Trans_Gm(n_cifra, tom_original, mudado, text_area, decode)
                            
                        if tom_original.upper() == 'G#':
                            
                            Trans_Gst(n_cifra, tom_original, mudado, text_area, decode,'')
                            
                        if tom_original == 'G#m':
                            
                            Trans_Gstm(n_cifra, tom_original, mudado, text_area, decode)
                                  
                    except Exception as error:
                        print(error)
                    zipp(n_cifra, decode)
            else:
               pass
