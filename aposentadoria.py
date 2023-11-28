from datetime import datetime
dados={}
dados['Nome']=str(input('Qual o nome da pessoa?'))
nascimento=int(input('Em que ano essa pessoa nasceu?'))
dados['idade']=datetime.now().year-nascimento
dados['Carteira']=int(input('Qual a carteira de trabalho?(0 não tem)'))
if dados['Carteira']!=0:
    dados['Salário']=float(input('Qual o seu salário?'))
    dados['contratação']=int(input('Qual o ano da sua contratação?'))
    dados['aposentadoria']=dados['idade']+ ((dados['contratação']+35)-datetime.now().year)
for k,v in dados.items():
    print(f'-{k}: {v}')





