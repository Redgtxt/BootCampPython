# Dicionários

## Sintaxe
```
{chave: valor}
```

## Exemplo de um Dicionário
```python
dicionarie = {
    "apple": "red",
    "banana": "yellow",
}
```

## Acessando Valores
```python
print(dicionarie["banana"])  # Output: yellow
```

## Adicionando um Item
```python
dicionarie["melon"] = "green"
```

## Limpando o Dicionário
```python
dicionarie = {}
```

## Iterando através de um Dicionário
```python
for key in dicionarie:
    print(key)
    print(dicionarie[key])
```

## Dicionários Aninhados

### Exemplo Básico
```python
capital = {
    "France": "Paris",
    "Germany": "Berlin",
}
```

### Dicionário dentro de Dicionário
```python
tavel_log = {
    "France": {
        "num_time_visited": 7,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
}
```

### Acessando Valores Aninhados
```python
# Acessar uma lista dentro de um dicionário aninhado
print(tavel_log["France"]["cities_visited"][2])  # Output: Dijon
```

## Listas Aninhadas
```python
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2])  # Output: ['C', 'D']
print(nested_list[2][0])  # Output: C
```
