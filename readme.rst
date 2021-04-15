Documentação
============

Distribuição
------------

A distribuição da documentação segue 3 passos:

    1. Gerar a documentação
    2. Subir a documentação para o servidor em produção
    3. Publicar a documentação


Gerar a documentação
^^^^^^^^^^^^^^^^^^^^

A partir do diretório do projeto, execute::

    invoke


Esse comando constrói a documentação e salva em ``./build/html``

Subir a documentação para o servidor em produção
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A partir do diretório do projeto, execute::

    scp -r ./build/html/ administrador@192.168.0.27:/home/administrador/manuais-deploy


Publicar a documentação
^^^^^^^^^^^^^^^^^^^^^^^

A partir do diretório ``administrador@192.168.0.27:/home/administrador/manuais-deploy``, execute::

    sudo cp -r . /var/www/dti.ifpa.edu.br/htdocs/manuais/
