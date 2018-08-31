CGIPES
======

Os CGIPES (*Comitês de Acompanhamento de Egressos*) são cadastrados em cada *Campi* por usuários do SIGAA com
perfil de GESTOR_EGRESSOS.

O módulo Portal do Egresso pode ser acessado clicando no respectivo botão de acesso no SIGAA (após fazer login),
conforme mostra a figura a seguir:

.. image:: _static/img/menu.png

Gerenciar CGIPES
----------------

Para acessar a página de gerenciamento de CGIPES, basta passar o mouse sobre o menu *CGIPES* e selecionar o sub-menu
*Gerenciar CGIPES* como mostra a imagem a seguir:

.. image:: _static/img/gerenciar_cgipes.png

Em seguida o sistema carrega uma página contendo a listagem de todos os CGIPES cadastrados, junto com as opções para
*Cadastrar*, *Gerenciar membros*, *Alterar* e *Remover CGIPES*:

.. image:: _static/img/comites.png

Cadastrar Novo CGIPES
~~~~~~~~~~~~~~~~~~~~~

Ao clicar no link *Cadastrar*, o sistema carrega o formulário de criação de novo CGIPES.

.. image:: _static/img/cadastrar.png

Todos os campos são requeridos e auto-explicativos. Após preencher todos os campos corretamente, o usuário clica
no botão *cadastrar* para criar um novo
CGIPES. Se o registro for inserido corretamente, o sistema redireciona para a página contendo a listagem de todos os CGIPES e 
ações. Também é possível clicar no botão *voltar*, para retornar para a página de listagem, ou *cancelar*, para
retornar a página inicial do portal do egresso. Lembrando que quaisquer dados não salvos são perdidos caso os botões
*voltar* e *cancelar* sejam clicados (o botão cancelar exibe uma mensagem de notificação antes de retornar para
página inicial do portal do egresso).

.. image:: _static/img/form_novo_cgipes.png

Editar CGIPES
~~~~~~~~~~~~~

Para iniciar o processo de edição, o usuário deve clicar no botão *alterar* do respectivo CGIPES que deve ser editado.

.. image:: _static/img/alterar_cgipes.png

Após o CGIPES ser selecionado, o sistema carrega a página contendo o formulário de novo CGIPES com os campos
preenchidos. O usuário altera os dados a seu critério e em seguida clicar no botão *Atualizar*. Se os campos
estivem com os formatos corretos, o sistema atualiza o CGIPES e redireciona para a página contendo a listagem de todos os CGIPES e ações.
Os botões *voltar* e *cancelar* funcionam de forma idêntica ao do formulário de `Cadastrar Novo CGIPES`_.

.. image:: _static/img/atualizar_cgipes.png

Deletar CGIPES
~~~~~~~~~~~~~~

Para deletar um CGIPES, deve-se clicar no botão *Remover* do respectivo CGIPES na página de listagem. Uma mensagem de confirmação é exibida ao usuário
antes do sistema efetivamente apagar o CGIPES. Um CGIPES não pode ser removido se possuir membros vinculados.

.. image:: _static/img/remover.png

Gerenciamento de Membros
~~~~~~~~~~~~~~~~~~~~~~~~

Para acessar a página de gerencimento de membros, basta clicar no botão *Gerenciar Membros* do respectivo CGIPES.

.. image:: _static/img/membros.png

A página consiste em duas seções, uma contendo o formulário de inclusão de um novo Membro para um determinado CGIPES
e outra contendo a listagem de membros para aquele CGIPES.

.. image:: _static/img/membros_form.png

Cadastro de Novo Membro
***********************

Todos os campos marcados com ``*`` são obrigatórios. O campo *Membro* é do tipo *autocompletar*. O usuário digita
alguns caracteres (pelo menos 3) e o sistema busca por membros cujo nome corresponda a texto inserido. Em seguida o usuário
clica em um dos registros apresentados na lista de resultados para selecioná-lo.

.. image:: _static/img/auto_completar.png

Os campos de *vigência* são do tipo *data*. O usuário clica no ícone do calendário ao lado direito do campo e
um pequeno calendário é exibido na tela. Em seguida é possível usar os controles desse calendário para selecionar mês e ano,
e finalmente clicar no dia do mês para selecioná-lo. É possível digitar uma data diretamente no campo de texto sem
precisar do calendário (nesse caso os caracteres ``/`` que formam a data são incluídos automaticamente).

.. image:: _static/img/campo_data.png

O campo *Vigência Final* não é requerido, mas um membro só poderá ser atualizado caso seja informado o campo
*Portaria de Remoção* **em conjunto** com o campo *Vigência Final*. Isso ocorre devido a data final de vigência
de um membro estar acompanhada de uma portaria específica. Portanto, também não é possível incluir um membro com o campo
*Portaria de Remoção* preenchido se o campo *Vigência Final* estiver vazio.

**Um membro não pode fazer parte de mais de um CGIPES ao mesmo tempo**. Caso o usuário tente inserir um novo membro já pertencente
a outro CGIPES, o sistema impede o cadastro e exibe uma mensagem de erro na tela.

.. image:: _static/img/novo_membro_erro.png

Ao clicar no botão *Voltar*, o sistema redireciona para a página de listagem de CGIPES.

Após a inserção dos dados corretamente, o usuário clica no botão *Salvar* e um novo membro é incluído na listagem
de membros daquele CGIPES.

Editar Membro
*************

Para editar um membro, o usuário clica no botão *Alterar Membro*, do respectivo membro que se quer editar, a partir
da seção que contém a listagem de membros para aquele CGIPES.

.. image:: _static/img/alterar_membro.png

O sistema então carrega o formulário de `Cadastro de Novo Membro`_ preenchido com os dados do membro que acabou
de ser selecionado. O usuário então pode editar os campos do formulário seguindo as mesmas recomendações descritas em
`Cadastro de Novo Membro`_. Após alterar os dados do membro, o usuário clica no botão *Atualizar*. Se os dados inseridos
estiverem com os formatos corretos, o sistema atualiza o membro e atualiza listagem de membros daquele CGIPES (agora
contendo os dados atualizados do membro que acabou de ser editado).

Remover Membro
**************

Para remover um membro, o usuário clica no botão *Remover Membro* do respectivo membro que se quer remover, a
partir da listagem de membros.

.. image:: _static/img/remover_membro.png

O sistema exibe uma mensagem de confirmação antes de desligar o membro daquele CGIPES. Após ser removido, um
membro pode ser incluído em outro CGIPES, se for o caso.

.. raw:: latex

    \newpage
