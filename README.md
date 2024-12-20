## END to END Machine Learn Project

# Students Performance in Exams

Esse projeto se trata um projeto completo em que foi implementado e feito deploy de um modelo de predição de desempenho de estudantes no teste de matematica com base em um grupo features. O dataset usado para treinamento e as features desse dataset podem ser encontradas abaixo.

Informações do dataset
genero
etinia
nível de educação dos pais
lunch
curso de preparação
score em leitura
score em escrita

prever score em matematica

link: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

# Formas de deploy usadas

Na pasta .ebextensions, está o arquivo de configuração usado para fazer o deploy da aplicação no Elastic Beanstalk.


O arquivo Dockerfile, localizado na raiz do projeto (ou onde está, se aplicável), é usado para fazer o deploy da aplicação como uma imagem Docker, por exemplo, em uma instância EC2.

Na pasta .github/workflows, está o arquivo YAML responsável pelo pipeline de CI/CD que utiliza o AWS ECS para armazenar as imagens Docker.

É possível modificar o pipeline para usa Azure ACR.

# Modelo

O modelo pré-treinado, com uma acurácia de 88%, e o pré-processador estão localizados na pasta artifacts.