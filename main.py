import datetime
import calendar

print("Hello Codex")

pasta_origem = r'G:\Outros computadores\Meu laptop\08 - EMPRESA ALVERNAZ CONSTRUÇÕES ELÉTRICAS LTDA\REGISTRO DE PONTO - Alvernaz\Formulário\Planilha de Respostas (Central)\01 - Ponto Funcionários'
pasta_modelos = r'G:\Outros computadores\Meu laptop\08 - EMPRESA ALVERNAZ CONSTRUÇÕES ELÉTRICAS LTDA\REGISTRO DE PONTO - Alvernaz\Formulário\Planilha de Respostas (Central)\02 - Padrão'
pasta_saida = r'G:\Outros computadores\Meu laptop\08 - EMPRESA ALVERNAZ CONSTRUÇÕES ELÉTRICAS LTDA\REGISTRO DE PONTO - Alvernaz\Formulário\Planilha de Respostas (Central)\Folha de Ponto'

mes = int(input("Digite o número do mês (1-12): "))
ano = datetime.datetime.now().year
num_dias = calendar.monthrange(ano, mes)[1]
intervalo_datas = [datetime.date(ano, mes, dia) for dia in range(1, num_dias + 1)]

print("Intervalo de datas do mês:")
for data in intervalo_datas:
    print(data.strftime("%d/%m/%Y"))
