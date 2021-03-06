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
  - XML: Busca dados em xml no google news rss.
  - CRAWL: Busca dados direto no site do Google noticias.
  - Linux: ```$ make xml``` ou ```make crawl word=paravra```
  - Windows: ```$ python control/google_news.py``` ou ```$ python control/crawl_google_news.py palavra```


## :minidisc: Resultado:

![resultado](https://user-images.githubusercontent.com/17969551/101183881-d0898100-362e-11eb-851b-7eec060f56d5.png)


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

Exemplo de resultado no txt:

![r](https://user-images.githubusercontent.com/17969551/101183978-edbe4f80-362e-11eb-966c-65d3623a43a4.png)
