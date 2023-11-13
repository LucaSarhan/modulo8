# Atividade ponderada 2

O Turtlebot foi desenvolvido para realizar o mapeamento de ambientes e posterior navegação com base em coordenadas predefinidas. Essa aplicação utiliza pacotes e launchers do ROS (Robot Operating System) para facilitar o controle e a integração do robô no ambiente, permitindo a execução de tarefas específicas, como a criação de mapas e a navegação autônoma.

## Instalação do Pacote ROS

Para instalar o pacote "turtlebot3", responsável pelas funcionalidades do Turtlebot, é necessário seguir as etapas a seguir.

Temos 3 prérequisitos para o funcionamento correto: Ubuntu, ROS e Nav2

Depois é preciso realizar o clone do repositório no GitHub e obter as dependências necessárias:

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


A fim de garantir o funcionamento adequado do pacote, é crucial realizar a compilação para atualizá-lo à sua versão mais recente e configurar as variáveis correspondentes para que o ROS possa aproveitar plenamente suas funcionalidades.

```
colcon build --packages-select turtlebot3
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
```

O comando para salvar o mapa é o seguinte:
```
ros2 run nav2_map_server map_saver_cli -f <nome-do-mapa>
```

## Funcionamento do Turtlebot

O Turtlebot opera em duas fases distintas. Inicialmente, ocorre a etapa de mapeamento do ambiente, permitindo que o robô adquira conhecimento sobre o espaço. Em seguida, é iniciada a fase de navegação, durante a qual o robô percorre pontos específicos previamente definidos no mapa.


O mapeamento do mundo funciona da seguinte maneira:

O estágio inicial do Turtlebot implica na geração do mapa do ambiente virtual. Para realizar essa operação, procederemos à execução de um arquivo de lançamento:
```
ros2 launch turtlebot3 launch.py
```

Um arquivo de lançamento é responsável por iniciar vários pacotes/nós simultaneamente. O `launch.py` ativa o `turtlebot3_cartographer`, `turtlebot3_gazebo` e `turtlebot3_teleop` os quais desempenham funções como mapeamento, simulação do ambiente e do robô, controle da movimentação e salvamento do mapa, respectivamente.

Ao focalizar o terminal turtlebot3_teleop, movimente o robô de maneira sistemática até que o mapa exibido no simulador Rviz esteja completamente preenchido. Posteriormente, alterne para o terminal do turtlebot3_teleop e salve o mapa conforme as instruções fornecidas (o programa salvará o mapa no diretório em que você executou o launch.py).


A navegação pelo mundo funciona da seguinte maneira:

A segunda e última etapa do Turtlebot é a navegação pelo mapa. Utilize o seguinte comando para rodar o próximo launchfile no mesmo diretório em que está o seu mapa salvo:

```
ros2 launch turtlebot3 movementlaunch.py
```

O `movementlaunch.py` ativa o `turtlebot3_navigation2`, `turtlebot3_gazebo` e `turtlebot3`, encarregados de navegar pelo mapa designado, simular o ambiente e enviar as coordenadas de deslocamento, respectivamente.

### Vídeo do Turtlebot

Verifique o turtlebot funcionando no video a seguir: https://drive.google.com/file/d/1Sr-6pCcZDMgd41SRd1XOx6BvDoiqvDM2/view?usp=sharing

Verifique o turtlebot mapeando no video a seguir: https://drive.google.com/file/d/1qlAJ2orPShuYH0EF0tue0Fsh0sAUXS_8/view?usp=sharing
