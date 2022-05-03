# Tipos de Instrucoes

- `Expressao/Expression`: Instrucao que espera uma valor de retorno
    - Exemplo:
      ```
      1 + 1 = 2
      8 > 10 = False
      8 < 10 = True
      ```

- `Declaracao/Statement`: Instrucao que prepara o interpretador para uma determinada tarefa mas nao retorna um valor.
    - Exemplo:
      ```
      if, else
      def
      for
      while
      pass
      ```
      
- `Atribuicao/Assignment`: Instrucao que pega o retorno de uma expressao e processa o seu valor com o intuito de armazenar.
    - Exemplo:
      ```
      soma = 40 + 2
      soma += 3
      soma -= 3
      ```
      
# Ambientes Virtuais

O ambiente virtual é um sandbox, é uma cópia de todo o ambiente Python e a recomendação é que você tenha um ambiente virtual em cada um dos seus projetos cada projeto deve usar seu próprio conjunto de bibliotecas isoladamente.

Criando o ambiente virtual

Na pasta do seu projeto usamos o módulo venv e informamos um nome para a pasta do ambiente ser criada, é comum que o nome seja .venv pois o . torna a pasta oculta no seu sistema e esse nome é comumente adotado.

```
cd project
python3 -m venv .venv
```

Mas para usar o ambiente virtual sempre será necessário efetuar a ativação, no linux isso é feito com o comando abaixo:

```
source .venv/bin/activate
```

Outra forma de verificar qual Ambiente Python está ativado é usando o comando `which`

```
which python
```