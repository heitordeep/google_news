# Projeto Google News :octocat:
Coleta de dados no google news com Python


## :pushpin: Pré-requisitos:

- Instalação das bibliotecas: ```$ make requirements```

## :rocket: Executar script:

- Antes de iniciar a execução, é necessário construir a sua pesquisa no arquivo **config_queries.json**, exemplo:
    ```javascript
    [
        {
            "word": "bolsonaro",
            "days_ago": "1",
            "language": "pt-BR"
        }
    ]
    ```
    
    Multiplas pesquisas:
    
    ```javascript
    [
        {
            "word": "bolsonaro",
            "days_ago": "1",
            "language": "pt-BR"
        },

        {
            "word": "desemprego no Brasil",
            "days_ago": "3",
            "language": "pt-BR"
        },

        {
            "word": "Brasil",
            "days_ago": "2",
            "language": "pt-BR"
        },

        {
            "word": "vacina",
            "days_ago": "5",
            "language": "pt-BR"
        }
    ]
    ```

- Após configurar a pesquisa, basta digitar:
  - Linux: ```$ make xml```
  - Windows: ```$ python control/google_news.py```
  
  
## :minidisc: Resultado:

![resultado](https://user-images.githubusercontent.com/17969551/101181933-3b858880-362c-11eb-919f-a185fec9ead8.png) 

Exemplo de resultado no json:

```javascript
[
    {
        "title": "Total de mortes por covid-19 no Brasil ultrapassa 175 mil - Valor Econômico",
        "date": "Thu, 03 Dec 2020 22:41:00 GMT",
        "url": "https://valor.globo.com/brasil/noticia/2020/12/03/total-de-mortes-por-covid-19-no-brasil-ultrapassa-175-mil.ghtml"
    },
    {
        "title": "Brasil fica em 25º lugar em ranking global de desempenho do PIB com 51 países - Economia & Negócios Estadão",
        "date": "Thu, 03 Dec 2020 18:18:15 GMT",
        "url": "https://economia.estadao.com.br/noticias/geral,brasil-fica-em-25-lugar-em-ranking-global-de-desempenho-do-pib-com-51-paises,70003538666"
    },
    {
        "title": "Programa Titula Brasil quer aumentar capacidade operacional para promover regularização fundiária - Portal Brasil",
        "date": "Fri, 04 Dec 2020 12:22:00 GMT",
        "url": "https://www.gov.br/pt-br/noticias/agricultura-e-pecuaria/2020/12/programa-titula-brasil-quer-aumentar-a-capacidade-operacional-para-promover-regularizacao-fundiaria"
    }
]
```


