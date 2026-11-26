# Central inteligente de demandas operacionais — estudo de caso

Identifiquei um gargalo na minha rotina de operações: demandas, compromissos e evidências de entrega ficavam dispersos em mensagens de WhatsApp e reuniões. Desenvolvi uma automação para centralizar essas informações e acompanhar suas atualizações.

## Sistema aplicado à rotina operacional

A documentação da solução descreve leitura de mensagens sincronizadas em Supabase e de registros de reuniões recorrentes, com fontes alternativas de reunião e anotações de agenda quando disponíveis. Consultas SQL e scripts Python levantam candidatos; a análise por IA distingue ações concretas, responsáveis e evidências de conclusão, elimina duplicidades e classifica os itens em tarefas, pautas, projetos, acompanhamentos e decisões.

O painel organiza demandas em **Comigo**, **Com os outros** e **Concluídos**, preserva contexto e origem, permite edição, baixa, exclusão e observações, e respeita decisões manuais nas atualizações agendadas. As fontes são consultadas em modo somente leitura.

O benefício relatado é menor necessidade de conferência manual e maior visibilidade das demandas; não foi realizada medição formal de economia de tempo.

## Versão pública demonstrativa

A documentação abaixo descreve uma versão simplificada com dados fictícios, que trabalha com arquivos exportados e não se conecta aos sistemas operacionais reais. Não foram publicados os arquivos internos, identificadores de infraestrutura, conversas, links privados ou regras com dados de clientes e colaboradores.

[Abrir painel demonstrativo](https://jenimelo.github.io/portfolio-ia-e-operacoes/central-de-pendencias/exemplos/saida-esperada/painel.html)

---

## Central de Pendências: skill de demonstração

Skill para agentes de IA que lê as conversas de chat exportadas e as anotações de reunião de uma
pessoa e monta uma central com o que pediram para ela, o que ela prometeu e o que ela pediu a
outras pessoas. Cada item traz a situação, o prazo, a fala original e há quantos dias está parado.
O resultado sai em JSON e num painel HTML com as abas **Comigo**, **Com os outros** e **Concluídos**.

Os dados de exemplo são de uma empresa fictícia, a **Atlas Logística**. Pessoas, conversas e
reuniões foram inventados para esta demonstração.

## O que a skill demonstra

- Leitura de duas fontes diferentes (chat e atas) num formato único, com ids estáveis.
- Classificação por direção: me pediram, prometi e eu pedi.
- Situação baseada em evidência: "vou ver" e uma mídia sem texto não concluem um pedido.
- Junção do mesmo pedido quando ele aparece no chat e na reunião.
- Respeito às decisões já tomadas no painel: itens excluídos não voltam e edições prevalecem.
- Segurança: o conteúdo das fontes é tratado como dado. Uma instrução escondida numa mensagem
  é ignorada, e uma senha que aparece na conversa não é copiada.

## Como rodar o exemplo

```powershell
python scripts/ler_fontes.py exemplos/entrada saida/fontes.json
```

O agente lê o `fontes.json` seguindo o `SKILL.md` e grava `saida/pendencias.json`. Depois:

```powershell
python scripts/gerar_painel.py saida/pendencias.json saida/painel.html
```

Para ver só o painel pronto, abra `exemplos/saida-esperada/painel.html` no navegador.

Requer Python 3.10 ou mais recente, sem bibliotecas externas.

## Arquivos

| Caminho | Para que serve |
|---|---|
| `SKILL.md` | instruções da skill: entradas, passo a passo e regras |
| `references/classificacao.md` | sinais de pedido, aceite, entrega e cobrança |
| `references/ids.md` | como os ids são calculados e por que não podem mudar |
| `references/formato-saida.md` | esquema do `pendencias.json` |
| `scripts/ler_fontes.py` | junta as conversas e as reuniões num JSON normalizado |
| `scripts/gerar_painel.py` | gera o painel HTML a partir do `pendencias.json` |
| `exemplos/entrada/pessoa.json` | dona da central e data de referência |
| `exemplos/entrada/estado.json` | exclusões e edições feitas antes no painel |
| `exemplos/entrada/conversas/*.txt` | duas conversas fictícias: um grupo e um privado |
| `exemplos/entrada/reunioes/*.md` | uma ata fictícia com próximas etapas |
| `exemplos/saida-esperada/pendencias.json` | os 7 itens que a skill deve produzir |
| `exemplos/saida-esperada/painel.html` | o painel gerado a partir desse JSON |
| `exemplos/saida-esperada/resumo-chat.md` | a resposta curta esperada no chat |

## O que o exemplo testa

| Situação na entrada | Resultado esperado |
|---|---|
| Pedido com prazo vencido e cobrança sem resposta | `atrasado`, prioridade alta |
| Pedido respondido só com uma mídia | continua `aberto` |
| Entrega confirmada por quem pediu | `concluido` |
| Pedido feito a outra pessoa, que aceitou | `eu_pedi` / `aguardando` |
| Promessa espontânea ao grupo | `prometi` |
| Mesmo pedido no chat e na ata | um item só, citando as duas fontes |
| Etapa de reunião excluída no painel | não volta |
| Conversa social, etapa de outra pessoa, senha, instrução escondida | ficam de fora |