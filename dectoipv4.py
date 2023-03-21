def converter(dec):
    #converte decimal para binário no tamanho ipv4 (8 bits)
    bi = ["","","","","","","",""]
    #primeiro bit
    if (dec < 128):#menor que 128 mantém o valor
        bi[0] = 0 
        #segundo bit
        if (dec < 64): #menor que 64 mantém o valor
            bi[1] = 0 
            #terceiro bit
            if (dec < 32):#menor que 32 mantém o valor
                bi[2] = 0 
                #quarto bit
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1
            else: #>= que 32 subtrai o valor                     
                bi[2] = 1
                dec -= 32                 
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1                  
        else: #>= que 64 subtrai o valor
            bi[1] = 1                        
            dec -= 64                    
            #terceiro bit
            if (dec < 32):#menor que 32 mantém o valor
                bi[2] = 0 
                #quarto bit
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1
            else: #>= que 32 subtrai o valor                     
                bi[2] = 1
                dec -= 32                 
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1                                        
    else: #>= que 128 subtrai o valor                           
        bi[0] = 1
        dec -= 128
        #segundo bit
        if (dec < 64): #menor que 64 mantém o valor
            bi[1] = 0 
            #terceiro bit
            if (dec < 32):#menor que 32 mantém o valor
                bi[2] = 0 
                #quarto bit
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1
            else: #>= que 32 subtrai o valor                     
                bi[2] = 1
                dec -= 32                 
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1                  
        else: #>= que 64 subtrai o valor
            bi[1] = 1                        
            dec -= 64                    
            #terceiro bit
            if (dec < 32):#menor que 32 mantém o valor
                bi[2] = 0 
                #quarto bit
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1
            else: #>= que 32 subtrai o valor                     
                bi[2] = 1
                dec -= 32                 
                if (dec < 16):#menor que 16 mantém o valor 
                    bi[3] = 0 
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1      
                else: #>= que 16 subtrai o valor
                    bi[3] = 1
                    dec -= 16
                    #quinto bit
                    if (dec < 8):
                        bi[4] = 0 #menor que 8 mantém o valor
                        #sexto bit
                        if (dec < 4):
                            bi[5] = 0 #menor que 4 mantém o valor
                            #sétimo bit
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                        else:
                            bi[5] = 1 #>= que 4 subtrai o valor    
                            dec -= 4
                            if (dec < 2):
                                bi[6] = 0 #menor que 2 mantém o valor
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: 
                                bi[6] = 1 #maior que 2 subtrai o valor
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1      
                    else: #>= que 8 subtrai o valor
                        bi[4] = 1 
                        dec -= 8
                        #sexto bit
                        if (dec < 4): #menor que 4 mantém o valor
                            bi[5] = 0 
                            #sétimo bit
                            if (dec < 2): #menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1):
                                    bi[7] = 0 #menor que 1
                                else:
                                    bi[7] = 1 #igual que 1
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                        else:#>= que 4 subtrai o valor  
                            bi[5] = 1   
                            dec -= 4
                            if (dec < 2):#menor que 2 mantém o valor
                                bi[6] = 0 
                                #oitavo bit
                                if(dec < 1): #menor que 1
                                    bi[7] = 0 
                                else: #igual que 1
                                    bi[7] = 1 
                            else: #>= que 2 subtrai o valor
                                bi[6] = 1 
                                dec -= 2
                                #oitavo bit
                                if(dec < 1):#menor que 1
                                    bi[7] = 0 
                                else:#igual que 1
                                    bi[7] = 1                                   
    return(bi)                                    
x = ""
ipv4 = True
for c in range (4): #4 octetos
    dec = int(input("Digite um número decimal inteiro: "))
    if (dec > 255):
        print("Isto não é um IPV4")
        ipv4 = False #cancela todas as ações
        break
    if (c == 0): #define classe no primeiro octeto
        classe = ""
        if (dec <= 126):
            classe = "CLASSE A"
        elif (dec <= 191):
            classe = "CLASSE B"
        elif (dec <= 223):
            classe = "CLASSE C"
        elif (dec <= 239):
            classe = "CLASSE D (Multicast)"
            netid = "Utilizada apenas em Multicast"
        else:
            classe = "CLASSE E (Uso Futuro)"
            netid = "Reservada para uso futuro"
    x += str(converter(dec)) #adicionando array a x e convertendo a string
    #definindo netid
    if(c == 0 and classe == "CLASSE A"): #um octeto
        netid = x
    if (c == 1 and classe == "CLASSE B"): #dois octetos
        netid = x
    if (c == 2 and classe == "CLASSE C"): #três octetos
        netid = x 

if (ipv4 == True): #exposição
    print ("IP: "+ '\033[31m'+x+'\033[0;0m')
    print ("NET ID :"+'\033[32m'+netid+'\033[0;0m')
    print ('\033[32m'+classe+'\033[0;0m')
