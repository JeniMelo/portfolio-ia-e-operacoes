# Ids estáveis

O painel guarda as decisões da pessoa (baixa, exclusão, edição) pelo `id` do item. Se o id
mudar entre uma atualização e outra, a decisão se perde e a pendência "volta".

O `scripts/ler_fontes.py` calcula:

| Fonte | Fórmula |
|---|---|
| mensagem de conversa | `sha1("<arquivo>|<dd/mm/aaaa hh:mm>|<autor>|<texto>")[:8]` |
| próxima etapa de reunião | `sha1("<arquivo>|<linha da próxima etapa>")[:8]` |

O item da central usa o id da **mensagem ou linha que originou o pedido** (não o da
resposta). Itens repetidos em duas fontes ficam com o id da fonte mais antiga.

Regras:
- nunca gere ids aleatórios para itens vindos das fontes;
- não troque o id de um item já publicado, mesmo que o título mude;
- itens criados à mão no painel usam o prefixo `m` e não colidem com os da fonte.