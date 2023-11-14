# Atividade Ponderada 3

O chatbot tem como principal funcionalidade dar retorno os pedidos dos usuarios. Exemplificando vocêe irá mandar o robô se locomover até um determinado local através do chatbot que irá retornara um feedback na tela que ele está locomovendo. Diante o enunciado esse chatbot não foi integrado com o simuldador nem do robô fisico. A aplicação foi feito justamente para fazer a simulação do robô através de linhas de comando no terminal.

# Fazendo funcionar em sua maquina

Para compilar o pacote execte os comandos abaixo:

´´´
colcon build --packages-select chatbot
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
´´´

Para rodar o chatbot em sua maquina execute o seguinte comando:

´´´
ros2 run chatbot chatbot
´´´

Link do video comprovando a funcionalidade: https://drive.google.com/file/d/1ClJBlh9V3JZM3HVPm4FQbD6AKoKqJbp2/view?usp=sharing
