# Tipos de Dados e Protocolos

Um objeto eh um endereco de memoria, um tipo e um valor.

Ao atribuirmos um valor para uma variavel, o Python realiza uma inferencia de tipos onde o tipo do objeto eh resolvido.
#
### Porque usamos tipos de dados?

Para não precisar manipular os dados manualmente, por exemplo, não precisamos nos preocupar com o fato de que cada letra de um texto é armazenada como um número binário, usamos os tipos de dados definidos pelas classes para utilizar abstrações que nos entreguem diretamente a letra "B" que queremos.

Também não precisamos nos preocupar com a posição da memória, para nós tanto faz se o Python armazenou na primeira ou na última pasta da memória, o importante em nossa camada de abstração é sabermos qual é a etiqueta colada lá, e quando precisamos do valor usamos a etiqueta para encontrar, portanto se quisermos obter o "B" usamos a referência "letra".

Os tipos de dados estão divididos em 2 categorias, os primários e os compostos
#
### Primários

Os tipos primários também chamados de tipos "escalares" (scalar types) são utilizados para armazenar uma única unidade de informação como por exemplo um número ou um texto como vimos anteriormente.
#
### Inteiros

O tipo usado para armazenar os números inteiros em Python é representado pela classe `int`, em Python nós não precisamos declarar qual o tipo de dado a ser usado pois o Python faz a inferência de tipos dinâmicamente, o interpretador primeiro verifica como o valor se parece e então decide por conta própria qual a classe a ser utilizada, exemplos de uso de `int`.
```
# a idade de uma pessoa
idade = 25

# o código de um produto
codigo_produto = 4587

# quantidade de itens
quantidade = 3
```

Verificando quais comportamentos estão no protocolo de um tipo de dado.

```
>>> dir(int)
# atributos especiais da classse int
['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floor__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__index__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__le__',
 '__lshift__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rlshift__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rrshift__',
 '__rshift__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__trunc__',
 '__xor__',
 
 # daqui para baixo estão atributos públicos que podemos usar diretamente
 'as_integer_ratio',
 'bit_count',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes']
```
#
### Float

Floats são parecidos com inteiros mas além de armazenar a parte inteira do número eles também podem armazenar o ponto flutuante, a fração, e são usados para armazenar resultados que não podem ser armazenados em inteiros, por exemplo.

```
>>> valor = 5 / 2  # cindo dividido por 2
>>> print(valor)
2.5
```
A presença de um `.` em um número faz com que o Python entenda que queremos armazena-lo em um objeto da classe float e assim como os inteiros ela possui todos os métodos especiais dunder para os protocolos que implementa e também métodos que são particulares apenas dos números floats.

Exemplos de uso de um float:
```
# Resultados de divisão
valor = 5 / 2

# Coordenadas geográficas
latitude = -37.80467681 
longitude = 144.9659498

# Saldo de pontuação (em jogos por exempo)
pontos = 355.8
```
#
### Booleanos

O tipo booleano é representado pela classe `bool` e ele pode armazenar apenas 2 estados `Verdadeiro` e `Falso`, em teoria poderiamos aplicar aqui a lógica binária e em nosso programa dizer que `0` é falso enquanto `1` é verdadeiro, e de fato é isso que Python faz por debaixo dos panos, porém para ficar com uma sintaxe mais bonita termos o tipo `bool` e suas variações `True` e `False`.

Quando utilizamos esse tipo? sempre que precisamos de **flags**, variavéis que podem estar em um desses dois estados, veja alguns exemplos:
```
# Tornar um usuário administrador
is_admin = True

# Verificar se o usuário quer continuar uma operação
continuar = False

# Definir se um produto está ativo em uma loja
active = True
```
#
### NoneType

Em alguns casos precisamos inicializar uma variável porém ainda não temos o valor para armazenar nela, nesse caso usamos o objeto `None`.
Este é um tipo especial que serve para quando não possuimos um valor mas precisamos da variável definida pois em algum momento no decorrer do programa iremos refazer a atribuição daquela variável.
```
produto = None

if produto is None:
    produto = funcao_para_definicao_do_produto()
```

O objeto `None` é um singleton, só existe um `None` mesmo que você defina várias variáveis como `None` todas elas farão referência ao mesmo `None`.
```
>>> a = None
>>> b = None

>>> id(a)
139862040616512

>>> id(b)
139862040616512

>>> a is b
True

a == b
True
```
#
### String

String sao formadas por cadeias de bytes.
O tipo `str` possui a maioria das carecteristicas que já abordamos nos outros tipos de dados e uma grande quantidade de protocolos implementados, vamos ver alguns.

```
# Sliceable (pode ser fatiado)
>>> "Bruno"[1]
'r'
# que internamente invoca o método `__getitem__`
>>> "Bruno".__getitem__(1)
'r'

# Addible (pode ser adicionado a outro texto)
# Essa operação se chama "Concatenação"
>>> nome = Bruno" 
>>> sobrenome = "Rocha"
>>> nome + " " + sobrenome
'Bruno Rocha'
# que internamente invoca o método `__add__`
>>> nome.__add__(" ".__add__(sobrenome))
'Bruno Rocha'

# Multipliable (que pode ser multiplicado)
>>> "Bruno" * 5
'BrunoBrunoBrunoBrunoBruno'

# Iterable (que pode ser iterado/percorrido)
>>> for letra in "Bruno":
...     print("-->" + letra.upper())
-->B
-->R
-->U
-->N
-->O
# Internamente o statement `for` invoca o método `__iter__`
>>> iterador = "Bruno".__iter__()
>>> next(iterador)
'B'
>>> next(iterador)
'r'
```

Além disso tudo, o tipo `str` também oferece muitos métodos públicos, que nós podemos usar explicitamente e que são muito úteis.

```
>>> "Bruno".upper()
'BRUNO'

>>> "BRUNO".lower()
'bruno'

>>> "bruno rocha".capitalize()
'Bruno rocha'

>>> "bruno rocha".title()
'Bruno Rocha'

>>> "bruno rocha".split(" ")
['bruno', 'rocha']

>>> "bruno".startswith("b")
True

>>> "bruno".endswith("b")
False

>>> "bruno rocha".count("o")
2

>>> "bruno rocha".index("c")
8
>>> "bruno rocha"[8]
'c'
```

E também algumas coisas que podemos fazer com qualquer objeto sequencial do Python:

```
>>> len("Bruno Rocha")
11

>>> sorted("Bruno Rocha")
[' ', 'B', 'R', 'a', 'c', 'h', 'n', 'o', 'o', 'r', 'u']

>>> list(reversed("Bruno Rocha"))
['a', 'h', 'c', 'o', 'R', ' ', 'o', 'n', 'u', 'r', 'B']
```

#
### Interpolação e Formatação de textos

Uma das coisas mais úteis de se fazer com texto é a interpolação de variáveis dentro do texto e a formatação de acordo com template pre-definido.

**Interpolação** é uma alternativa a **concatenação**, enquanto a concatenação usa o sinal de `+` como em `"Bruno"` + `"Rocha"` na interpolação usamos templates com posicionamento.


Python oferece 3 maneiras de fazer **Interpolação**, a primeira e mais antiga delas segue um padrão universal adotado em muitos sistemas e em outras linguagens de programação e utiliza o sinal de `%` como marcador de template.

%
```
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %f pontos."
>>> nome = "Bruno"
>>> numero = 4
>>> pontos = 42.5
>>> print(mensagem % (nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.500000 pontos.
```

Este tipo de formatação usa o `%` acompanhado de `s` para str, `d` para int, ou `f` para float, e além de demarcar o **placeholder** onde a substituição irá ocorrer também podemos definir a precisão numérica como em `%.2f` que significa que queremos imprimir apenas 2 casas decimais do número float.
```
>>> mensagem = "Olá %s, você é o participante número %d e pode ganhar %.2f pontos."
>>> print(mensagem % (nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```
E também é possivel utilizar parâmetros nomeados.
```
>>> mensagem = "Olá %(nome)s, você é o participante número %(num)d e pode ganhar %(pon).2f pontos."
>>> print(mensagem % {"nome": "Bruno", "num": 4, "pon": 42.5})
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```
Apesar do uso de `%` ter caido em desuso no Python3, ainda existem bibliotecas como a `logging` que ainda utiliza este formato.

`format`
Esta é a forma preferida para fazer interpolação de textos pois além de permitir a substituição de variáveis também permite a formatação dos valores, vejamos alguns exemplos:
```
>>> mensagem = "Olá {}, você é o participante número {} e pode ganhar {} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.5 pontos.
```

Repare que ao invés de `%` agora usamos `{}` para marcar um placeholder e ao inves de `%` usamos a chamada do método `.format` do próprio tipo `str` para passar os valores em sequência.

E também podemos especificar tipos e a precisão numérica usando `:` e os mesmos marcadores dentro de `{}`.
```
>>> mensagem = "Olá {:s}, você é o participante número {:d} e pode ganhar {:.2f} pontos."
>>> print(mensagem.format(nome, numero, pontos))
Olá Bruno, você é o participante número 4 e pode ganhar 42.50 pontos.
```

Podemos utilizar outras opções de formatação em cada uma das marcações entre `{}`. existe toda uma mini linguagem de formatação:
```
{[[fill]align][sign][#][0][width][grouping_option][.precision][type]}
fill - <any charac­ter>
align - "­<" | "­>" | "­=" | "­^"
sign - "­+" | "­-" | " "
width - digit+
grouping_option - "­_" | "­,"
precision - digit+
type - "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

Exemplos:
```
# Centralizar fazendo ocupar exatamente 11 caracteres.
>>> "{:^11}".format("Bruno")
'   Bruno   '

# A mesma coisa porém alinhado à direita.
>>> "{:>11}".format("Bruno")
'      Bruno'

# Agora preenchendo os espaços com outro carectere
>>> "{:*^11}".format("Bruno")
'***Bruno***'

# Definindo tipo e precisão para números
>>> "{:*^11.2f}".format(45.30000041)
'***45.30***'
```

O site [Pyformat](https://pyformat.info/) oferece um guia bastante intuitivo para utilizar as opções de formatação, elas são tantas que não daria para abordarmos todas elas neste treinamento, mas não se preocupe que durante os nossos exercícios vamos utilizar as mais comuns.

Uma outra forma mais rápida de obter essa ajuda é abrindo o python e digitando
```
help('FORMATTING')
```
`f strings`
No Python 3 foi introduzido um atalho bastante útil para usar o `format` e de uma forma mais natural agora podemos escrever strings que se auto formatam usando as variáveis existentes, o funcionamento respeita as mesmas opções vistas anteriormente, o que muda é só a forma de escrever, ao invés de chamar explicitamente `.format()` usamos `f"texto"`.
```
# Texto
>>> nome = "Bruno"
>>> f"{nome:*^11}"
'***Bruno***

# Número
>>> valor = 45.30000041
>>> f"{valor:*^11.2f}"
'***45.30***'
```
Uma útilidade interessante das f-strings é usar para fazer debugging.

```
>>> nome = "Bruno"
>>> print(f"{nome=}")
nome='Bruno'
```
#
### Tipos compostos

Com os tipos `primários` temos a limitação de representar apenas uma única informação em cada objeto, porém existem casos em que desejamos compor um objeto único que contém mais de uma informação e para isso usamos os tipos compostos.

### Tuplas

As tuplas são o tipo composto mais simples de todos e bastante comum de serem usadam em Python, da mesma forma que anteriormente vimos que a string "ABC" é uma sequência de carecteres, com as tuplas conseguimos fazer uma sequência de valores que podem ser de qualquer tipo.

Exemplo de um sistema que armazena coordenadas sem o uso de tuplas:
```
coord_x = 140
coord_y = 200
coord_z = 9
```

Exemplo de um sistema que armazena coordenadas com o uso de tuplas:
```
coord = 140, 200, 9

# ou

coord = (140, 200, 9)
```

Em Python sempre que um ou mais objetos forem encadeados com `,` isso será interpretado como um objeto do tipo `tupla` e a tupla pode opcionalmente ter paranteses, nos já usamos tupla lembra? quando falamos de interpolação de textos.
```
"Olá %s você é o %03d da fila" % (nome, senha)
```

No exemplo acima de interpolação os parenteses são obrigatórios mas no caso das nossas coordenas o jeito mais comum de declarar é mesmo usando a sintaxe sem os parenteses e usar os parenteses comente quando for necessário para desambiguar

Portanto com este tipo de objeto não temos mais as variaveis `x` e `y` e `z`, agora temos uma única `coord` e para acessar os objetos que estão dentro da tupla usamos o protocolo de **subscrição**, os objetos que possuem um método chamado `__getitem__` permitem que a gente acesse seus elementos usando `[ ]` e nós também já fizemos isso lá no primeiro script quando fatiamos a variável de ambiente. `(current_language = os.getenv("LANG")[:5])`
```
coord = 140, 200, 9

mover_x_para_coordenada(coord[0])
mover_y_para_coordenada(coord[1])
mover_z_para_coordenada(coord[2])
```

Repare que podemos acessar `coord[0]` e assim por diante usando `[numero]` e este número se refere a posição do valor que queremos dentro da tupla.

### Desempacotamento

A caracteristica mais interessante das tuplas se chama **unpacking** ou desempacotamento em português. (algumas linguagens chamam isso de **spread**, **espalhamento**, **explode**)

O desempacotamento permite fazer a operação contrária da atribuição olha que interessante.
```
# Empacotamento (atribuição)
coord = 140, 200, 9

# Desempacotamento (atribuição multipla)
x, y, z = coord
```

No desempacotamento o Python automaticamente vai pegar cada um dos elementos da tupla e usar para definir as variaveis que separarmos por `,`.

### Imutabilidade

Outra caracteristica importante e que talvez seja decisiva na hora de escolher usar tuplas é o fato de que elas são imutáveis, uma vez criada a tupla, não é possivel alterar, não dá para mudar os valores ou adicionar novos. (este tópico contém algumas excessões que veremos na nossa aula sobre escopos)

### Algumas coisas que podemos fazer com as tuplas
```
# Atribuir sem parenteses
coord = 140, 200, 9

# atribuir com parenteses
coord = (140, 200, 9)

# desempacotar
x, y, z = coord

# ignorar elementos (será atribuito apenas o x)
x, *_ = coord

# pegar apenas o primeiro e o último elemento
x, *_, y = coord

# Verificar o tamanho
len(coord)
3

# Acessar via subscrição pelo indice
coord[0]
140

# fatiar
coord[1:]
(200, 9)
```
### Listas

Listas são bastante similares as tuplas e a maioria das operações que podemos fazer com tuplas também podemos fazer com as listas, uma das grandes diferenças está na implementação de protocolos de edição dos elementos, portanto as listas são mutáveis e permitem que incluamos novos itens, permitem a remoção de itens existentes e a reordenação.

As listas são criadas usando os literais `[ ]` ou a chamada para a classe `list`.

Criando uma lista vazia:
```
colors = []  # forma preferida
# ou
colors = list()
```

Adicionando elementos ao final da lista:
```
colors.append("green")
```

Adicionando elementos ao inicio da lista:
```
colors.insert(0, "red")
```

Adicionando em uma posição especifica:
```
colors.insert(2, "blue")
```

Obtendo o tamanho da lista:
```
len(colors)
```

Acessando elementos via indice:
```
button_color = colors[0]
```

Desempacotamento (igual as tuplas):
```
red, green, blue = colors
```

E também é possível já iniciar uma lista com valores.
```
>>> colors = ["red", "green", "blue"]
>>> colors[0]
"red"
```

Podemos somar 2 listas (criando uma nova lista como resultado):
```
>>> nova_lista = colors + ["yellow"]
>>> print(nova_lista)
["red", "green", "blue", "yellow"]
```

E podemos extender uma lista `in-place`:
```
>>> colors.extend(["purple"])
>>> print(colors)
["red", "green", "blue", "purple"]


# Ou usando um operador de acréscimo
>>> colors += ["purple"]
>>> print(colors)
["red", "green", "blue", "purple"]
```

Remover elementos:
```
colors.remove("purple")
# ou
colors.pop()
```

Contar elementos:
```
>>> colors.count("green")
1=
```
#
### Sets

Sets podem ser criados usando as sintaxes:
```
# A partir de qualquer objeto iterável

iteravel = [1, 2, 3]  # list
iteravel = 1, 2, 3  # tuple
iteravel = "Banana"  # str

# usando a classe
set(iteravel)

# usando literais com { e }
{1, 2, 3, 4}

# desempacotando tuplas, listas ou textos
{*iteravel}
```
Aplicamos a teoria dos conjuntos usando operadores:
```
>>> conjunto_a = [1, 2, 3, 4, 5]
>>> conjunto_b = [4, 5, 6, 7, 8]

# | para união
>>> set(conjunto_a) | set(conjunto_b)
{1, 2, 3, 4, 5, 6, 7, 8}

# & para intersecção
>>> set(conjunto_a) & set(conjunto_b)
{4, 5}

# – para diferença
>>>  set(conjunto_a) - set(conjunto_b)
{1, 2, 3}

# para ^ diferença simétrica
>>> set(conjunto_a) ^ set(conjunto_b)
{1, 2, 3, 6, 7, 8}
```
### Performance

Fazer buscar em sequencias é uma operação bastante pesada, imagina que no seu twitter você tem 5000 seguidores e você deseja buscar um deles ou fazer essas operações de comparação como fizemos com os conjuntos.

Se você tiver uma lista `["joao", "bruno", "maria", ...]` contendo os elementos, e quiser por exemplo buscar pelo usuario `"alfredo"` o python vai ter que percorrer toda a lista e comparar elemento por elemento até encontrar o alfredo, e se o alfredo estiver no final? Vai demorar muito, essa é uma operação que tem uma complexidade algoritmica `O(n)` pois Python vai ter que efetuar uma comparação para cada item n da lista.

Os sets implementam uma hash table! 🎉

É como se eles tivessem um indice gravado neles com uma tabela invertida dizendo
```
"joao" -> "esta na posição 0"
"alfredo" -> "esta na posicao 345"
```
Portanto quando precisarmos buscar o `alfredo` o python olha primeiro essa tabela e já vai diretamente na informação que está em `345` como se fizessemos `users[345]` em uma lista e a complexidade desta operação passa a ser `O(1)` pois agora só tem uma comparação a ser feita.

Por quê isso importa? Sets são mais rápidos!

operações como `if "alfredo" in usuarios:` se `usuarios` for um set irá ser bem mais rápido do que caso `usuarios` seja uma lista ou tupla.

### Mutabilidade
Você pode criar um conjunto vazio e ir adicionando elementos e também pode remover elementos, eles são mutáveis
```
>>> a = set([1,2,3])
>>> a.add(4)
>>> a.remove(1)
>>> print(a)
{2, 3, 4}
```

### Deduplicação
Esta é uma das caracteristica mais interessante dos sets e talvez a sua maior utilidade, sets não permitem itens duplicados, então ao criar um set você elimina as duplicidades.
```
>>> conjunto = set()
>>> conjunto.add("Bruno")
>>> conjunto.add("Maria")
>>> conjunto.add("Bruno")
>>> conjunto.add("Maria")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")

# Digamos que por algum motivo (ou engano) adicionou o mesmo item mais de uma vez
# sem problemas :)

>>> print(conjunto)
{'Bruno', 'Maria'}

# E isso também functiona em tempo de atribuição
>>> {1, 2, 3, 1, 1, 1, 1, 5, 5, 5, 5}
{1, 2, 3, 5}
```
### Desvantagens dos sets?
- Não respeitam a ordem de inserção, os elementos são ordenados automaticamente
- Não permitem subscrição para acesso aos valores

Ou seja, você não pode fazer `set[0]` para acessar o primeiro elemento.
```
>>> conjunto = {4, 5, 6, 7, 8}

conjunto[0]
---------------------------------------------
TypeError   Traceback (most recent call last)
Input In [60], in <module>
----> 1 conjunto[0]

TypeError: 'set' object is not subscriptable
```
mas pode usar `in` ou converter o set em uma lista.
```
>>> 4 in conjunto
True


>>> list(conjunto)[0]
4
```





