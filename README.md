# PUC
Atividades acadêmicas e anotações da minha graduação em Ciência de Dados e Inteligência Artificial na PUC-SP
### Trilha de estudos
```mermaid
%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'primaryColor': '#1f77b4',
      'primaryTextColor': '#fff',
      'primaryBorderColor': '#7F7F7F',
      'lineColor': '#F8B229',
      'secondaryColor': '#006100',
      'tertiaryColor': '#fff'
    }
  }
}%%

flowchart LR
    one-->two
    two-->three
    subgraph three["3 ano"]
    direction LR
    c1("Redes Neurais")
    c2("<a href='http://google.com' style='color: inherit;text-decoration: inherit;'>Aprendizado Profundo</a>")
    end
    subgraph two["2 ano"]
    direction LR
    b1("<a href='https://github.com/olucaslopes/PUC/tree/main/Aprendizado%20de%20M%C3%A1quina' style='color: inherit;text-decoration: inherit;'>Aprendizado de Máquina</a>")
    b2("<a href='https://github.com/olucaslopes/PUC/blob/main/Minera%C3%A7%C3%A3o%20de%20Dados' style='color: inherit;text-decoration: inherit;'>Mineração de Dados</a>")
    b3("Simulação e Otimização")
    b4("Engenharia de Software")
    end
    subgraph one["1 ano"]
    direction LR
    a1("Programação")
    a2("Matemática")
    a3("Estatística")
    end
```
