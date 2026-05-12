# Exercícios de Python — Listas, Dicionários, Tuplas e Conjuntos

# 5. Streaming de Filmes (Lista + Dicionário)

Uma plataforma de streaming armazena os filmes disponíveis em uma lista de dicionários:

```python
filmes = [
    {"titulo": "Matrix", "nota": 9.0, "visualizacoes": 1500},
    {"titulo": "Interestelar", "nota": 9.5, "visualizacoes": 2300},
    {"titulo": "Avatar", "nota": 8.0, "visualizacoes": 1800}
]
```

Desenvolva um programa em Python que:

- a) Mostre o nome de todos os filmes cadastrados.
- b) Exiba o filme com a maior nota.
- c) Calcule a média das notas dos filmes.
- d) Crie uma lista contendo apenas filmes com mais de 1700 visualizações.

---

# 6. Sistema Escolar (Tuplas + Lista)

Uma escola armazena os alunos em uma lista de tuplas no formato:

```python
alunos = [
    ("Marcos", 7.5),
    ("Fernanda", 9.0),
    ("Lucas", 5.5),
    ("Amanda", 8.0)
]
```

Desenvolva um programa em Python que:

- a) Mostre o nome e a nota do primeiro aluno.
- b) Calcule a média geral da turma.
- c) Mostre o aluno com a maior nota.
- d) Crie uma lista contendo apenas alunos aprovados (nota maior ou igual a 7).

---

# 7. Controle de Estoque (Dicionário + Lista)

Uma loja armazena categorias e produtos em um dicionário:

```python
estoque = {
    "Informática": ["Mouse", "Teclado", "Monitor"],
    "Celulares": ["iPhone", "Samsung Galaxy"],
    "Áudio": ["Fone Bluetooth", "Caixa de Som"]
}
```

Desenvolva um programa em Python que:

- a) Mostre todas as categorias cadastradas.
- b) Exiba todos os produtos da categoria `"Informática"`.
- c) Calcule a quantidade total de produtos cadastrados.
- d) Crie uma lista contendo todos os produtos sem repetição.

---

# 8. Restaurante (Lista + Tuplas + Dicionário)

Um restaurante armazena os pedidos realizados no formato:

```python
pedidos = {
    1: ("Hambúrguer", 2, 35.0),
    2: ("Pizza", 1, 50.0),
    3: ("Refrigerante", 3, 8.0)
}
```

Cada tupla representa:

```python
(nome_do_produto, quantidade, valor_unitario)
```

Desenvolva um programa em Python que:

- a) Mostre todos os pedidos cadastrados.
- b) Calcule o valor total de cada pedido.
- c) Calcule o valor total geral da compra.
- d) Mostre apenas os pedidos com quantidade maior que 1.

---

# Questões Alternativas

## 1.

Qual método adiciona um item ao final de uma lista?

- a) add()
- b) append()
- c) push()
- d) insertLast()

---

## 2.

Qual estrutura permite armazenar chave e valor em Python?

- a) Lista
- b) Tupla
- c) Dicionário
- d) Set

---

## 3.

Qual das alternativas representa corretamente uma tupla?

- a) [1, 2, 3]
- b) {1, 2, 3}
- c) (1, 2, 3)
- d) {"a": 1}

---

## 4.

O que o método `pop()` faz em uma lista?

- a) Ordena a lista
- b) Remove um elemento
- c) Adiciona um elemento
- d) Duplica a lista

---

## 5.

Qual estrutura não permite elementos repetidos?

- a) Lista
- b) Tupla
- c) Dicionário
- d) Conjunto

---

## 6.

Qual função retorna a quantidade de itens de uma lista?

- a) size()
- b) count()
- c) len()
- d) length()

---

## 7.

Como acessar o valor da chave `"nome"` em um dicionário?

```python
usuario = {"nome": "Carlos"}
```

- a) usuario.nome
- b) usuario["nome"]
- c) usuario(“nome”)
- d) usuario->nome

---

## 8.

Qual das alternativas abaixo cria uma lista vazia?

- a) ()
- b) {}
- c) []
- d) set()
