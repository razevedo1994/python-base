email_tmpl = """
    Ola, %(nome)s
    
    Tem interesse em comprar %(produto)s?
    
    Este produto eh otimo para resolver
    %(texto)s
    
    Clique agora em %(link)s
    
    Apenas %(quantidade)d disponiveis!
    
    Preco promocional %(preco).2f
"""

clientes = ["Rodrigo", "Ricardo", "Sueli", "Izabela"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "sua ausencia de caneta.",
            "link": "https://caneta.com.br",
            "quantidade": 1,
            "preco": 50,
        }
    )
