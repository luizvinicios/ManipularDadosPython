ips={}
resp= "S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
    input("Digite os dois ultimos octetos: "))]=input("Nome da máquina:  ")
    resp=input("Digite <S> para continuar: ").upper()

    print("Exibindo ip ́s: ")
    for ip in ips.keys():
        print(ip[0]+"."+ip[1])

    print("Exibindo as máquinas que compõem uma mesma rede: ")
    rede=input("Digite os dois primeiros octetos: ")
    for ip,nome in ips.items():
        if(ip[0]==rede):
            print(nome) 