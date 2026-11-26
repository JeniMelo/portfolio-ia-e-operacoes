# Formato do `pendencias.json`

```json
{
  "pessoa": "Nome da pessoa",
  "empresa": "Nome da empresa",
  "referencia": "2026-03-06 09:00",
  "observacao": "Texto curto sobre o que ficou de fora ou faltou nas fontes.",
  "itens": [
    {
      "id": "a1b2c3d4",
      "direcao": "me_pediram | prometi | eu_pedi",
      "status": "aberto | atrasado | aguardando | concluido",
      "prioridade": "alta | media | baixa",
      "titulo": "Frase curta, começando pelo verbo",
      "quem_pediu": "Nome",
      "para_quem": "Nome",
      "origem": "conversa | reuniao",
      "fonte": "Nome da conversa ou da reunião",
      "quando": "2026-03-02 08:12",
      "prazo": "2026-03-05",
      "dias_parado": 1,
      "fala": "Trecho literal que originou o item",
      "ultimo_movimento": "Fato mais recente, com data, que justifica o status"
    }
  ]
}
```

- `prazo` e `para_quem` podem ficar vazios (`""`) quando a fonte não informa.
- Em `eu_pedi`, `quem_pediu` é a própria pessoa e `para_quem` é quem vai entregar.
- A aba **Comigo** mostra `me_pediram` e `prometi` não concluídos; **Com os outros** mostra
  `eu_pedi` não concluídos; **Concluídos** mostra todo `concluido`.