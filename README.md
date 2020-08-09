# SmartDiF
Configurando a ferramenta
Crie uma pasta para a ferramenta e clone os arquivos do repositório.
Instale o pip3 e em seguida o virtualenv "pip3 install virtualenv".
Crie um ambiente virtual "virtualenv -p python3 smartdifenv".
Inicie o ambiente virtual "source smartdifenv/bin/activate".
Instale os requerimentos da ferramenta "pip3 install -r requirements.txt".
Fazendo o download da imagem da técnica.
Instale o Docker 18.03.1-ce.
Adicione o docker em um grupo com "sudo groupadd docker".
Adicione o usuário conectado "$ USER" ao grupo docker com "sudo gpasswd -a $USER docker"
Reinicie o computador, para o comando acima surtir efeito.
Utilize "docker login" para se conectar ao docker hub, Username:smartdifdocker Password:smartdif.
Baixe a imagem da técnica Illuminants "docker pull smartdifdocker/tecnicas:illuminants"
Inicializando a ferramenta
Abra o terminal na pasta raiz da ferramenta.
Execute o script python "python3 SmartDiF.py", em seguida o navegador será aberto.
