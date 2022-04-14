# Tipos de Dados e Protocolos

Um objeto eh um endereco de memoria, um tipo e um valor.

Ao atribuirmos um valor para uma variavel, o Python realiza uma inferencia de tipos onde o tipo do objeto eh resolvido.

### Porque usamos tipos de dados?

Para não precisar manipular os dados manualmente, por exemplo, não precisamos nos preocupar com o fato de que cada letra de um texto é armazenada como um número binário, usamos os tipos de dados definidos pelas classes para utilizar abstrações que nos entreguem diretamente a letra "B" que queremos.

Também não precisamos nos preocupar com a posição da memória, para nós tanto faz se o Python armazenou na primeira ou na última pasta da memória, o importante em nossa camada de abstração é sabermos qual é a etiqueta colada lá, e quando precisamos do valor usamos a etiqueta para encontrar, portanto se quisermos obter o "B" usamos a referência "letra".

Os tipos de dados estão divididos em 2 categorias, os primários e os compostos

### Primários

Os tipos primários também chamados de tipos "escalares" (scalar types) são utilizados para armazenar uma única unidade de informação como por exemplo um número ou um texto como vimos anteriormente.

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









