# Meu Portfólio
![Screenshot 1](/screenshots/header.png)
Acesse a versão live [aqui!](https://web-production-efab.up.railway.app/)

---

## Sobre o Projeto

Este repositório foi construído com **Flask** e **Bootstrap**, oferecendo uma estrutura prática e simples para criar e gerenciar um portfólio dinâmico.

## Gerenciamento Simples

Os arquivos JSON localizados na pasta `/content` permitem que você adicione ou remova conteúdos facilmente. Com um simples commit, as alterações são refletidas na versão final do portfólio.

## Funcionalidades Dinâmicas

Graças ao Flask e ao **Jinja2**, este projeto possibilita a renderização de páginas dinâmicas a partir de dados estruturados. Por exemplo:

```html
<!-- Exemplo de uso do Jinja para exibir uma lista de projetos -->
<ul>
  {% for project in projects %}
  <li>{{ project.name }} - {{ project.description }}</li>
  {% endfor %}
</ul>
```
Como resultado é criado uma lista dinamicamente com base nos dados presentes em `/content/projects.json` (Carregados e processados em app.py).

Com essa abordagem, e um pouco de HTML, o conteúdo do portfólio é atualizado automaticamente com base nos dados fornecidos.

## Fonte de aprendizado
O template do projeto tem como referência um mini curso disponibilizado gratuitamente pelo [Thi Code](https://www.thicode.com.br/) e disponibilizado em seu [Canal do youtube](https://www.youtube.com/@thi_code)

