import os #modulo python
import shutil #modulo python

caminho_original = 'C:/Users/alex/Downloads/'
caminho_pdf = 'C:/Users/alex/Downloads/arquivos_pdf'
caminho_xml = 'C:/Users/alex/Downloads/arquivos_excel'
caminho_todos= 'C:/Users/alex/Downloads/todos_arquivos'

conta= 0
for root,dirs,files in os.walk(caminho_original):
    for file in files:
            old_file = os.path.join(root,file)
            new_file = os.path.join(caminho_pdf,file)
            excel_file = os.path.join(caminho_xml,file)
            todos_file = os.path.join(caminho_todos,file)
            try :
                conta += 1
                if '.pdf' in file:
                    shutil.move(old_file,new_file)
                    print(f' Arquivo {file} movido com sucesso')

                elif '.csv'  in file :
                    shutil.move(old_file,excel_file)
                    print(f' Arquivo {file} movido com sucesso')

                elif '.xlsx'  in file :
                    shutil.move(old_file,excel_file)
                    print(f' Arquivo {file} movido com sucesso')  
                else:
                    shutil.move(old_file,todos_file)

            except Exception  as e:
                print('ERRO')
print()  
print(f'{conta}, arquivos encotrado')              