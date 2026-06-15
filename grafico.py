import networkx as nx
from pyvis.network import Network

# Inicializa o grafo do NetworkX
G = nx.Graph()

# 1. ADICIONANDO OS NÓS (Personagens e seus Grupos para colorir o mapa)
personagens = [
    # Núcleo Alex / Meyers
    ("Alex Meyers", "Família Meyers / Protagonista"),
    ("Gary Meyers", "Família Meyers"),
    ("Anne Beghin", "Família Meyers"),
    ("Billy Meyers", "Família Meyers"),
    ("Beatrice Meyers", "Família Meyers"),
    ("Romeo Meyers", "Família Meyers"),
    ("Silas Meyers", "Família Meyers"),
    ("Ross Meyers", "Conexão Central (Meyers/Boyd)"),
    
    # Núcleo Derek / Boyd / Smith
    ("Derek Boyd", "Família Boyd / Protagonista"),
    ("Diana Boyd", "Família Boyd"),
    ("David Smith", "Família Boyd"),
    ("Elsie Boyd", "Família Boyd"),
    ("Eileen Boyd", "Família Boyd"),
    ("Mason Lewis", "Família Boyd"),
    ("Hazel Boyd", "Família Boyd / Ponte"),
    ("Callum Boyd", "Família Boyd"),
    ("Arabella Boyd", "Família Boyd"),
    
    # Família Lyle
    ("Franklin Lyle", "Família Lyle"),
    ("Julie Lyle", "Família Lyle"),
    
    # Amigos / Outros
    ("Caleb Winters", "Círculo Alex"),
    ("Drew Cooper", "Círculo Alex"),
    ("Daniel Park", "Círculo Alex"),
    ("Philip Lane", "Círculo Alex"),
    ("Hannah Lynch", "Ponte de Amizade (Alex/Derek)"),
    ("Brent Harvey", "Círculo Derek"),
    ("Stephen Reid", "Círculo Derek"),
    ("Meredith Reid", "Círculo Derek")
]

for nome, grupo in personagens:
    G.add_node(nome, group=grupo, title=f"{nome} ({grupo})")

# 2. ADICIONANDO AS ARESTAS (Conexões e o tipo de relação)
conexoes = [
    # Família Meyers
    ("Billy Meyers", "Beatrice Meyers", "Casados"),
    ("Billy Meyers", "Gary Meyers", "Pai/Filho"),
    ("Beatrice Meyers", "Gary Meyers", "Mãe/Filho"),
    ("Gary Meyers", "Anne Beghin", "Casados"),
    ("Gary Meyers", "Romeo Meyers", "Pai/Filho"),
    ("Gary Meyers", "Alex Meyers", "Pai/Filha"),
    ("Gary Meyers", "Silas Meyers", "Pai/Filho"),
    ("Anne Beghin", "Romeo Meyers", "Mãe/Filho"),
    ("Anne Beghin", "Alex Meyers", "Mãe/Filha"),
    ("Anne Beghin", "Silas Meyers", "Mãe/Filho"),
    
    # Família Boyd / Smith / Lewis
    ("Callum Boyd", "Arabella Boyd", "Casados"),
    ("Callum Boyd", "Elsie Boyd", "Pai/Filha"),
    ("Callum Boyd", "Eileen Boyd", "Pai/Filha"),
    ("Arabella Boyd", "Elsie Boyd", "Mãe/Filha"),
    ("Arabella Boyd", "Eileen Boyd", "Mãe/Filha"),
    ("Elsie Boyd", "Eileen Boyd", "Irmãs Gêmeas"),
    ("Elsie Boyd", "David Smith", "Casados"),
    ("Elsie Boyd", "Derek Boyd", "Mãe/Filho"),
    ("Elsie Boyd", "Diana Boyd", "Mãe/Filha"),
    ("David Smith", "Derek Boyd", "Pai/Filho"),
    ("David Smith", "Diana Boyd", "Pai/Filha"),
    ("Eileen Boyd", "Mason Lewis", "Casados"),
    ("Eileen Boyd", "Hazel Boyd", "Mãe/Filha"),
    ("Mason Lewis", "Hazel Boyd", "Pai/Filha"),
    
    # Primos Boyd
    ("Hazel Boyd", "Diana Boyd", "Primas"),
    ("Hazel Boyd", "Derek Boyd", "Primos"),
    
    # O Vínculo Incômodo (Ross e a ligação Meyers/Boyd)
    ("Romeo Meyers", "Diana Boyd", "Ex-Relacionamento"),
    ("Romeo Meyers", "Ross Meyers", "Pai/Filho"),
    ("Diana Boyd", "Ross Meyers", "Mãe/Filho"),
    ("Alex Meyers", "Ross Meyers", "Tia/Sobrinho"),
    
    # Conflito Central
    ("Alex Meyers", "Diana Boyd", "Rivalidade / Convivência por Ross"),
    
    # Romance Central
    ("Alex Meyers", "Derek Boyd", "Namorados"),
    
    # Amigos da Alex
    ("Alex Meyers", "Hazel Boyd", "Melhores Amigas"),
    ("Alex Meyers", "Caleb Winters", "Amigos"),
    ("Alex Meyers", "Drew Cooper", "Amigos"),
    ("Alex Meyers", "Hannah Lynch", "Amigos"),
    ("Alex Meyers", "Philip Lane", "Amigos"),
    ("Drew Cooper", "Daniel Park", "Namorados"),
    ("Alex Meyers", "Daniel Park", "Círculo Social"),
    
    # Amigos do Derek e Rivalidades
    ("Derek Boyd", "Brent Harvey", "Amigos"),
    ("Derek Boyd", "Stephen Reid", "Amigos"),
    ("Derek Boyd", "Meredith Reid", "Amigos"),
    ("Derek Boyd", "Hannah Lynch", "Amigos"),
    ("Stephen Reid", "Meredith Reid", "Irmãos"),
    ("Caleb Winters", "Derek Boyd", "Rivais"),
    ("Meredith Reid", "Alex Meyers", "Rivais"),
    ("Meredith Reid", "Diana Boyd", "Melhores Amigas"),
    
    # Família Lyle
    ("Gary Meyers", "Franklin Lyle", "Melhores Amigos"),
    ("Franklin Lyle", "Julie Lyle", "Casados")
]

for p1, p2, rel in conexoes:
    G.add_edge(p1, p2, title=rel, label=rel)

# 3. GERANDO O MAPA INTERATIVO COM PYVIS
net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white", filter_menu=True)
net.from_nx(G)

# Ajusta a física para os nós se espalharem de forma legível
net.toggle_physics(True)
net.show_buttons(filter_=['physics'])

# Salva e abre o arquivo no navegador
net.write_html("grafo_personagens.html")
print("Grafo gerado com sucesso! Abra o arquivo 'grafo_personagens.html' no seu navegador.")
