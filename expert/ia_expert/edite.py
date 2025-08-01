            else:
                if str(n_cifra.get()) != '':
                    try:

                        root.update()
                        bt['text'] = 'Aguarde a conclusão...'
                        bt['bg'] = 'gray'
                        root.update()
                        if original.get().upper() == 'A':
                            root.update()
                            Trans_A(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Am':
                            root.update()
                            Trans_Am(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'A#':
                            root.update()
                            Trans_Ast(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'A#m':
                            root.update()
                            Trans_Astm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'B':
                            root.update()
                            Trans_B(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Bm':
                            root.update()
                            Trans_Bm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'C':
                            root.update()
                            Trans_C(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()                    
                        if original.get() == 'Cm':
                            root.update()
                            Trans_Cm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'C#':
                            root.update()
                            Trans_Cst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'C#m':
                            root.update()
                            Trans_Cstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'D':
                            root.update()
                            Trans_D(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Dm':
                            root.update()
                            Trans_Dm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'D#':
                            root.update()
                            Trans_Dst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'D#m':
                            root.update()
                            Trans_Dstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'E':
                            root.update()
                            Trans_E(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Em':
                            root.update()
                            Trans_Em(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'F':
                            root.update()
                            Trans_F(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Fm':
                            root.update()
                            Trans_Fm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'F#':
                            root.update()
                            Trans_Fst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'F#m':
                            root.update()
                            Trans_Fstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'G':
                            root.update()
                            Trans_G(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Gm':
                            root.update()
                            Trans_Gm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'G#':
                            root.update()
                            Trans_Gst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END),'')
                            root.update()
                        if original.get() == 'G#m':
                            root.update()
                            Trans_Gstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                      
                        text_area.delete(1.0, END)
                        with open(fr'Minhas_cifras/{n_cifra.get()}.txt', 'r', encoding='utf-8') as texto:
                            text_area.insert(1.0, str(texto.read()))
                            #enviar_email_2(f'Sua nova cifra "{n_cifra.get()}"', f'{text_area.get(1.0, END)}', 'moises.miss@gmail.com')
                            root.update()
                            create_pdf(fr'Minhas_cifras/{n_cifra.get()}', f'Minhas_cifras/{n_cifra.get()}')
                        
                        bt['bg'] = 'lime'
                        bt['text'] = 'Start'
                        root.update()
                        messagebox.showinfo(title='info', message='Sucesso, a troca de escala foi concluída')
                    except Exception as error:
                        messagebox.showerror(title='ERRO!', message=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}')
                        bt['bg'] = 'lime'
                        bt['text'] = 'Start'
                    root.update()
                else:
                    messagebox.showerror(title='ERRO!', message='Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!')
                    bt['bg'] = 'lime'
                    bt['text'] = 'Start'
                root.update()