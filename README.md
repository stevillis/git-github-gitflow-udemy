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
