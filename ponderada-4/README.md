# Ponderada 4

Esse projeto visa criar um chatbot com base em um LLM usando uma API para fornecer informações sobre seguranção em um ambiente industrial. 
O objetivo é fornecer informações completas e precisas sobre normas de segurança e comportamento dos funcionários que mitiga riscos a sua segurança. 
Essa aplicação foi feita para interpretar questôes sobre segurança de ambiente industrial, ou seja, fazer perguntas sobre o vestimento do local, comportamento humano dentro desse ambiente etc. A aplicação funciona.

**Gradio:** é responsavel pela interface gráfica
**Ollama:** é responsavel pelo modelo utilizado para fazer as respostas
**Langchain:** é responsavel por usar a biblioteca cliente Ollama para se conectar a um servidor LLM executando o modelo llama2
**API local:** é responsavel por fazer requisição pro modelo

# Instruções de execução

Caso não tenha instalado utlize esses comandos para instalar o gradio, langchain e ollama:

```
pip install langchain
pip install gradio
curl https://ollama.ai/install.sh | sh
```

Para baixar o modelo necesário basta rodar o comando a seguir:

```
ollama run llama2
```

Vai ser necessario clonar o repositório usando o seguinte comando para clonar:

```
git clone https://github.com/LucaSarhan/modulo8.git
```

Depois vai ser necesário se locomover para o local do arquivo relevante

```
cd modulo8/ponderada-4/src/main/main
```

Feito isso segue o comando para executar a aplicação

```
python3 integration.py
```

Link do video comprovando o funcionamento: https://drive.google.com/file/d/1EAZIHlE3FcrM2d1HTHi7Pbp_d1Bb3yA2/view?usp=sharing
