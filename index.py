# Lista para armazenar posts
posts = []

# Lista simulada de avisos de desastres
avisos = [
    "Alerta de enchente na região sul!",
    "Tempestade prevista para as próximas 24 horas!",
    "Risco de deslizamento em áreas de encosta!"
]

# Função para publicar um post
def publicar_post():
    print("\n=== Publicar Post ===")
    tipo = input("Digite o tipo de post (pedido ou oferta): ").strip().lower()
    descricao = input("Descreva o que você precisa ou está oferecendo: ").strip()
    local = input("Informe sua localização: ").strip()
    
    post = f"{tipo.upper()} - {descricao} (Local: {local})"
    posts.append(post)
    print("✅ Post publicado com sucesso!")

# Função para exibir posts
def ver_posts():
    print("\n=== Posts Publicados ===")
    if len(posts) == 0:
        print("Nenhum post publicado ainda.")
    else:
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post}")

# Função para exibir avisos
def mostrar_avisos():
    print("\n=== Avisos de Desastres ===")
    for aviso in avisos:
        print(aviso)

# Menu principal
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Publicar um post")
        print("2. Ver posts publicados")
        print("3. Ver avisos de desastres")
        print("4. Sair")
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == '1':
            publicar_post()
        elif escolha == '2':
            ver_posts()
        elif escolha == '3':
            mostrar_avisos()
        elif escolha == '4':
            print("Saindo... Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
