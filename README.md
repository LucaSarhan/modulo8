# Atividade ponderada 2

O Turtlebot foi desenvolvido para realizar o mapeamento de ambientes e posterior navegação com base em coordenadas predefinidas. Essa aplicação utiliza pacotes e launchers do ROS (Robot Operating System) para facilitar o controle e a integração do robô no ambiente, permitindo a execução de tarefas específicas, como a criação de mapas e a navegação autônoma.

## Instalação do Pacote ROS

Para instalar o pacote "ponderada-2", responsável pelas funcionalidades do Turtlebot, é necessário seguir as etapas a seguir.

### Requisitos de instalação essenciais para o correto funcionamento do Turtlebot:

```
Ubuntu
ROS
Nav2
```

### Realizar o clone do repositório no GitHub e obter as dependências necessárias:

Se necessário, faça o download das seguintes dependências:

```
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
pip install setuptools==58.2.0
```

Execute os comandos a seguir:

```
git clone https://github.com/LucaSarhan/modulo8.git
rosdep install -i --from-path src --rosdistro humble -y
```

### Compilar o pacote e configurar variáveis correspondentes:

A fim de garantir o funcionamento adequado do pacote, é crucial realizar a compilação para atualizá-lo à sua versão mais recente e configurar as variáveis correspondentes para que o ROS possa aproveitar plenamente suas funcionalidades.

```
colcon build --packages-select pond2
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

## Turtlebot em Ação

O Turtlebot opera em duas fases distintas. Inicialmente, ocorre a etapa de mapeamento do ambiente, permitindo que o robô adquira conhecimento sobre o espaço. Em seguida, é iniciada a fase de navegação, durante a qual o robô percorre pontos específicos previamente definidos no mapa.


### Mapeamento do Mundo:

O estágio inicial do Turtlebot implica na geração do mapa do ambiente virtual. Para realizar essa operação, procederemos à execução de um arquivo de lançamento:
```
ros2 launch pond2 launch.py
```

Um arquivo de lançamento é responsável por iniciar vários pacotes/nós simultaneamente. O mapping_launch.py ativa o turtlebot3_cartographer, turtlebot3_gazebo, turtlebot3_teleop, e pond2_teleop, os quais desempenham funções como mapeamento, simulação do ambiente e do robô, controle da movimentação e salvamento do mapa, respectivamente.

Ao focalizar o terminal turtlebot3_teleop, movimente o robô de maneira sistemática até que o mapa exibido no simulador Rviz esteja completamente preenchido. Posteriormente, alterne para o terminal do pond2_teleop e salve o mapa conforme as instruções fornecidas (o programa salvará o mapa no diretório em que você executou o mapping_launch.py).


### Navegando pelo Mundo
A segunda e última etapa do Turtlebot é a navegação pelo mapa. Utilize o seguinte comando para rodar o próximo launchfile no mesmo diretório em que está o seu mapa salvo:

```
ros2 launch ponderada-2 launch.py
```

O `movementlaunch.py` ativa o `turtlebot3_navigation2`, `turtlebot3_gazebo` e `turtlebot3`, encarregados de navegar pelo mapa designado, simular o ambiente e enviar as coordenadas de deslocamento, respectivamente.

### Vídeo do Tartabot!
Você pode conferir o funcionamento do Tartabot no vídeo a seguir:



