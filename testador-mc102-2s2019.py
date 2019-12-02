import os, re, subprocess, sys

# Checa se os argumentos estão corretos
if (len(sys.argv) != 2 or (not re.compile("^lab([0-9]{2})").match(sys.argv[1]))):
    print("Uso: python testador.py labXX")
    sys.exit(0)

# Abre o arquivo para redirecionamento de saídas
try:
    FNULL = open(os.devnull, "w")
except:
    print("Unknown error")
    sys.exit(0)

# Testa presença do programa diff
try:
    diffOutput = subprocess.call(["diff"], stdout=FNULL, stderr=FNULL)
except:
    print("Falta instalar diff: http://gnuwin32.sourceforge.net/packages/diffutils.htm")
    sys.exit(0)

# Inicia o script
lab = sys.argv[1] + ".py"
if (os.path.isdir("testes_abertos")):
    testAmount = len(os.listdir("testes_abertos"))//2
    if (testAmount > 0):
        # Roda os testes (joga as saídas para arqXX.out)
        for i in range(1, testAmount+1):
            inputFile = "testes_abertos/arq" + str(i) + ".in"
            outputFile = "arq" + str(i) + ".out"
            print("Executando teste " + str(i))
            os.system("python " + lab + " < " + inputFile + " > " + outputFile)
        print()
        
        # Compara as saídas com as respostas esperadas, exibindo as diferenças se houverem
        erros = 0
        for i in range(1, testAmount+1):
            inputFile = "arq" + str(i) + ".out"
            resultFile = "testes_abertos/arq" + str(i) + ".res"

            print("Comparando teste " + str(i) + "...")
            if (subprocess.call(["diff", "--strip-trailing-cr", inputFile, resultFile]) != 0):
                erros += 1
                print()
        
        # Exibe o número de erros encontrados
        if (erros > 0):
            print(str(erros) + " erros encontrados em seu programa. Corrija-os e teste novamente!")
        else:
            print("Nenhum erro encontrado.")
        
        # Deleta os arquivos de saída gerados
        for i in range(1, testAmount+1):
            outputFile = "arq" + str(i) + ".out"
            os.system("del " + outputFile)
    else:
        print("Mova os testes para a pasta testes_abertos!")
else:
    print("Mova a pasta testes_abertos para esta pasta!")
