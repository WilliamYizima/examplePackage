# ExamplePackage

## Descrição
- Receber um objeto para serealizar e deserealizar, transformando em um payload BASE.
- Payload BASE:
    - status
    - event
    - created_at

- Payload 01:
    - estado
    - evento
    - data_criacao

- Payload 02:
    - state
    - name-event
    - date

## Falta
- Comentários
- tratativa de erro
- Refactor com Template Method
- Melhorar a Implementação do Factory

obs:
    - É possível fugir do mapeamento?
    - 
## Rodar
- help:
```
    python setup.py --help-commands
```
- Para fazer o build("organização do módulo") do pacote  ExamplePackage:
```
    python setup.py build
```
- Para criar o build o "examplePackage-0.0.1.tar.gz":
```
    python setup.py sdist
```
- Caso você tenha um ambiente virtual sem o pacote,é possível instalar com esse arquivo gerado pelo sdist:
```
   pip install {seucaminho}/examplePackage-0.0.1.tar.gz
```

