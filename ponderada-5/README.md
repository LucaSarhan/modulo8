# Atividade ponderada 5

Esse projeto visa criar um chatbot com base em um LLM usando uma API para fornecer informações sobre segurança em um ambiente industrial. 
O objetivo é fornecer informações completas e precisas sobre normas de segurança e comportamento dos funcionários que mitigam riscos à sua segurança. Essa aplicação agora consegue acessar links da internet para usar como contexto para ajudar responder perguntas.
Essa aplicação foi feita para analisar questões sobre segurança no ambiente industrial, ou seja, responder perguntas sobre os equipamentos de segurança do local, bem como o comportamento humano dentro desse ambiente etc... A aplicação funciona.

**Gradio:** é responsável pela interface gráfica.

**Ollama:** é responsável pelo modelo utilizado para entregar as respostas.

**Langchain:** é responsável por usar a biblioteca cliente Ollama para se conectar a um servidor LLM executando o modelo llama2.

**API local:** é responsável por fazer requisição pro modelo.

# Instruções de execução

Caso não tenha instalado, utlize esses comandos para instalar o gradio, langchain e ollama:

```
pip install langchain
pip install gradio
curl https://ollama.ai/install.sh | sh
```

Para baixar o modelo necesário basta rodar o comando a seguir:

```
ollama run orca-mini
```

Vai ser necessario clonar o repositório usando o seguinte comando:

```
git clone https://github.com/LucaSarhan/modulo8.git
```

Após isso será necesário se locomover para o local do arquivo relevante usando o comando a seguir:

```
cd modulo8/ponderada-5
```

Feito isso, segue o comando para executar a aplicação:

```
python3 integration.py
```

Para essa ponderada eu peguei o link que você indicou no enunciado e usei para indicar o contexto.

Link do video comprovando o funcionamento: https://drive.google.com/file/d/1DbS2LygapY8CL68xibomaXXvPfj10o0z/view?usp=sharing
