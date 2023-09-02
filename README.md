# HelpTE_API

## Solução

Os autistas podem ter dificuldade em identificar, compreender e expressar suas emoções e sentimentos, o que pode resultar em problemas de comunicação e relacionamento. Para ajudar a superar esses desafios, criamos o HelpTE que tem como objetivo criar uma solução que utilize a fala, texto e a API do Microsoft Azure para traduzir as emoções de pessoas autistas em palavras, permitindo uma comunicação mais eficiente,sendo esses os três principais recursos que podem ser utilizados.
O principal objetivo do projeto é desenvolver uma solução que permita às pessoas autistas reconhecer as emoções expressadas através de uma interface de voz e texto. A solução poderia utilizar os três recursos API de reconhecimento de fala e processamento de linguagem natural do Microsoft Azure para identificar as entradas dos usuários (textoáudio) e através do processamento do chat gpt interpretar as emoções contidas na entrada do usuário.API de análise de sentimento Outro recurso que poderíamos utilizar é a API de análise de sentimento do Azure ela determina o tom emocional das palavras expressas pelos usuários, ajudando a entender melhor suas emoções e sentimentos, no entanto, por se tratar de uma plataforma paga optamos em usar ferramentas gratuitas e o chatgpt que foi solicitado pela plusoft.
Existem outras  funcionalidades que o Microsoft Azure oferece de computação em nuvem, essas que citamos fala, análise de texto e análise de sentimento. São as que seriam úteis para o nosso projeto, com o recurso de fala, é possível transformar áudio em texto. Já a análise de texto permite extrair percepções valiosas dos sentimentos, enquanto a API de análise de sentimento permitiria uma eficácia na tradução dos sentimentos . Com essas ferramentas,acreditamos estar utilizando da melhor forma o Azure em nosso projeto dando ênfase nas principais funcionalidades do nosso software,  por se tratar de uma plataforma de nuvem altamente confiável, que oferece uma série de recursos de segurança e privacidade de dados. sentimos confiantes em deixar as funções no servidor.

` Áudio `

| Método HTTP | EndPoint | Descrição | 
|-------------|----------|-----------|
| POST | '/audio_texto' | Pegar o input de áudio e traduzir para texto |

 ` Texto `

| Método HTTP | EndPoint | Descrição | 
|-------------|----------|-----------|
| POST | '/texto_audio' | Pegar a tradução de texto e traduzir para áudio |

` Tradução `

| Método HTTP | EndPoint | Descrição | 
|-------------|----------|-----------|
| POST | '/tradutor' | Pegar o input do usuário e traduzir as suas emoções |

##   

| Verbos HTTP |
|-------------|
| GET: Obter dados |
| POST: Criar um novo recurso |
| PUT: Atualizar um recurso existente |
| DELETE: Excluir um recurso existente |

## Funcionamento da API em Flask

![API_FLASK](https://github.com/risuhoki/HelpTE_API/blob/main/API_FLASK.png?raw=true)

## Vídeo

[![video](https://github.com/risuhoki/HelpTE_API/blob/main/helpte.png?raw=true)](https://www.youtube.com/watch?v=g6m1TLmUnws&ab_channel=matheusgomesmontemurro)
