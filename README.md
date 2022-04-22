# Git - O Curso completo - Git, GitHub e Git Flow - Udemy

## Comandos Git

#### Repositório Local

- Inicializar repositório

  ```bash
  $ git init
  ```

- Adicionar arquivos para staging

  ```bash
  $ git add .
  # ou
  $ git add nome_arquivo
  # ou
  $ git add arquivo1 arquivo2 arquivo3
  # ou
  $ git add diretorio/
  # ou
  $ git add --all
  ```

- Remover arquivos da staging (remove da staging e apaga o arquivo)

  ```bash
  $ git rm -f arquivo
  ```

- Realizar commit

  ```bash
  $ git commit
  # ou
  $ git commit -m "mensagem"
  ```

- Status do repositório

  ```bash
  $ git status
  ```

- Desfazer alterações em um arquivo (versionado) antes de adicioná-lo ao staging

  ```bash
  $ git checkout -- arquivo
  ```

- Histórico de alterações no repositório

  ```bash
  $ git log
  ```

---

#### Repositório Remoto

- Adicionar repositório remoto

  ```bash
  $ git remote add origin url_repositorio_remoto.git
  ```

- Configurar o branch padrão ao enviar alterações do repositório local para o repositório remoto

  ```bash
  $ git push --set-upstream origin master
  ```

- Enviar alterações para o repositório remoto, onde a branch remota já tenha sido configurada

  ```bash
  $ git push
  # ou
  $ git push origin nome_da_branch
  ```

- Atualizar repositório local com as alterações do repositório remoto

  ```bash
  $ git pull
  ```

- Sincronizar referências do repositório local com o repositório remoto (sem fazer merge)

  ```bash
  $ git fetch
  ```

---

#### Tags

- Criar tag

  ```bash
  $ git tag versao
  ```

- Listar tags

  ```bash
  $ git tag -l
  ```

- Enviar tags para repositório remoto

  ```bash
  $ git push origin nome_da_tag # envia uma tag específica
  # ou
  $ git push origin --tags # envia todas as tags
  ```

- Remover uma tag

  ```bash
  $ git tag -d nome_da_tag
  ```

- Navegar entre tags

  ```bash
  $ git checkout nome_da_tag
  ```

---

#### Banches

- Criar branch

  ```bash
  $ git branch nome_da_branch
  ```

- Listar branches

  ```bash
  $ git branch
  ```

- Trocar de branch

  ```bash
  $ git checkout nome_da_branch
  ```

- Renomear branch

  ```bash
  git branch -m nome_antigo nome_novo
  ```

- Excluir uma branch
  ```bash
  $ git branch -d nome_da_branch
  ```

---

#### Merge

- Merge

  1. Entrar na branch onde o merge será realizado `$ git checkout nome_da_branch`
  2. Realizar o merge com a segunda branch `$ git merge segunda_branch`

- Rebase

  ```bash
  $ git rebase nome_branch_de_origem
  ```

---

#### Commit

- Cherry-pick - adicionar commits de outra branch

  ```bash
  $ git cherry-pick nome_da_branch hash_do_commit
  ```

- Reset - exclui commits anteriores ao commit selecionado

  ```bash
  $ git reset hash_do_commit
  # ou
  $ git reset HEAD~quantidade_de_commits_a_serem_excluidos
  ```

- Stash

  - Empilhar alterações versionadas da staging

    ```bash
    $ git stash
    ```

  - Desempilhar alterações versionadas da staging

    ```bash
    $ git stash pop
    ```

  - Listar alterações empilhadas em stash
    ```bash
    $ git stash list
    ```

---

## Comandos Gitflow

#### Repositório

- Inicializar repositório

  ```bash
  $ git flow init
  ```

#### Feature

- Iniciar feature

  ```bash
  $ git flow feature start nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git checkout develop
  $ git checkout -b feature/nome_da_branch
  ```

- Publicar feature

  ```bash
  $ git flow feature publish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git push --set-upstream feature/nome_da_branch
  ```

- Finalizar feature

  ```bash
  $ git flow feature finish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git checkout develop
  $ git merge feature/nome_da_branch
  $ git branch -D feature/nome_da_branch
  ```

#### Release

- Iniciar release

  ```bash
  $ git flow release start nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git flow checkout develop
  $ git checkout -b release/nome_da_branch
  ```

- Publicar release

  ```bash
  $ git flow release publish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git push --set-upstream origin release/nome_da_branch
  ```

- Finalizar release

  ```bash
  $ git flow release finish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git checkout master
  $ git merge release/nome_da_branch
  $ git tag release/nome_da_branch
  $ git checkout develop
  $ git merge release/nome_da_branch
  $ git branch -d release/nome_da_branch
  ```

#### Hotfix

- Iniciar hotfix

  ```bash
  $ git flow hotfix start nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git checkout master
  $ git checkout -b hotfix/nome_da_branch
  ```

- Publicar hotfix

  ```bash
  $ git flow hotfix publish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
  $ git push --set-upstream origin hotfix/nome_da_branch
  ```

- Finalizar hotfix

  ```bash
  $ git flow hotfix finish nome_da_branch
  ```

  Equivalente sem extensão git-flow:

  ```bash
    $ git checkout master
    $ git merge hotfix/nome_da_branch
    $ git checkout develop
    $ git merge hotfix/nome_da_branch
    $ git branch -D hotfix/nome_da_branch
  ```
