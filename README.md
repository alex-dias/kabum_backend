# kabum_backend - Teste Técnico
### Alexandre Dias Negretti

Essa é a minha solução para o teste proposto de Teste Técnico - Desenvolvedor Back-End

## Decisões Técnicas

Eu tive pouca experiência com linguagem web durante a minha graduação e carreira profissional. Por isso não pude implementar grandes soluções relacionadas à usabilidade da aplicação. Foquei mais na funcionalidade e na estrutura por trás de tudo. Ainda assim foram necessárias algumas horas de estudo e pesquisa sobre o framework e HTML.

O web framework escolhido foi Django, isso se deu pelo meu breve contato com a ferramenta durante a graduação, além da mesma usar uma interface python, que é a linguagem que tenho mais familiaridade.

Para carregar os dados de Clientes e Produtos decidi usar um arquivo .csv, desse modo a aplicação funcionaria perfeitamente para diferentes arquivos que seguissem o mesmo padrão de colunas estabelecido.

A plataforma de hospedagem web escolhida foi a PythonAnywhere, justamente pelo uso do framework e sua interface com python. A aplicação pode ser acessada pelo link: http://negrettialex.pythonanywhere.com/

## Arquitetura

O foco na estrutura da aplicação foi dividir os arquivos de template e de backend. Quanto ao backend, segui a estrutura pré-estabelecida pelo Django, trabalhando com views, forms e urls separadamente. Além disso criei o arquivo _businessRules.py_ para armazenar a função de regras de negócio; ainda que apenas uma função foi necessária, novas melhorias e funções podem ser adicionadas nesse arquivo.

## Workflow

As implementações e commits seguiram o meu aprendizado da ferramenta. Cada nova ideia que eu tinha necessitava um novo aprendizado, e muitas vezes esse novo aprendizado era útil para melhorar implementações passadas.

Escolhi terminar toda a aplicação para então documentá-la, pois assim tive mais propriedade e conhecimento de tudo o que tinha implementado.

## Considerações Finais

Foi bastante interessante aprender mais sobre linguagem web, além de subir a minha primeira aplicação online. Valeu muito o aprendizado, mas ao mesmo tempo senti que poderia entregar uma solução melhor caso dominasse mais a linguagem. Um dos pontos de melhoria seria o flow das páginas e talvez adicionar o mínimo de frontend para tornar a aplicação mais interessante.
