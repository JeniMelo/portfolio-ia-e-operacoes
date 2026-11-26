# Relatório de edição

Todos os tempos estão em segundos. No vídeo 01, cada cena tem um número inteiro de compassos da trilha (2,4 s).

## Cenas do vídeo 01 (origem)

| # | Cena | No 01 | Papel |
|---|---|---|---|
| 01 | Gancho de abertura ("Quanto do seu dia vai para tarefas repetitivas?") | 0,0–4,8 | introdução |
| 02 | Título ("IA e produtividade: o que muda no dia a dia") | 4,8–9,6 | introdução |
| 03 | Contexto: 75% já usam IA generativa no trabalho | 9,6–16,8 | essencial |
| 04 | Por que agora? | 16,8–21,6 | complementar |
| 05 | Onde a IA ganha tempo (4 aplicações) | 21,6–28,8 | essencial |
| 06 | Exemplo: da reunião ao plano de ação | 28,8–36,0 | exemplo |
| 07 | O que os estudos já mediram (+14%, 55%, +40%) | 36,0–43,2 | essencial |
| 08 | IA com responsabilidade | 43,2–48,0 | complementar |
| 09 | Como começar em 3 passos | 48,0–55,2 | complementar |
| 10 | Conclusão ("Multiplica o que elas fazem de melhor") | 55,2–60,0 | essencial |

## Vídeo 02: removido, preservado e reorganizado

| Ordem no 02 | Trecho do 01 | No 02 | Decisão |
|---|---|---|---|
| 1 | 02 · Título (4,8–9,6) | 0,0–4,8 | **preservado**, porque abre direto no tema |
| 2 | 03 · Contexto 75% (9,6–16,8) | 4,8–12,0 | **preservado**, porque é o dado que justifica o assunto |
| 3 | 07 · Evidências (36,0–43,2) | 12,0–19,2 | **reorganizado**: veio para antes das aplicações. Sem o exemplo prático, os dados dos estudos sustentam a sequência "adoção → ganhos medidos → onde aplicar" |
| 4 | 05 · Onde a IA ganha tempo (21,6–28,8) | 19,2–26,4 | **preservado** |
| 5 | 10 · Conclusão (55,2–60,0) | 26,4–31,2 | **preservado**, com o acorde final da trilha |

**Removido (28,8 s):**

| Cena | Trecho do 01 | Motivo |
|---|---|---|
| 01 · Gancho de abertura | 0,0–4,8 | introdução prolongada; o título já apresenta o tema |
| 04 · Por que agora? | 16,8–21,6 | contexto complementar |
| 06 · Exemplo prático | 28,8–36,0 | ilustração; as aplicações continuam listadas na cena 05 |
| 08 · IA com responsabilidade | 43,2–48,0 | complementar; a ressalva "os ganhos variam conforme a tarefa: a IA rende mais com revisão humana" continua dentro da cena de evidências |
| 09 · Como começar | 48,0–55,2 | complementar |

**Música:**
- As 4 junções caem em limites de compasso (compassos 2–4, 4–7, 15–18, 9–12 e 23–25 do 01). Por isso o pulso
  segue igual e os acordes continuam dentro da tonalidade.
- A introdução sem bateria (cena 01) saiu. A entrada recebeu um fade de 0,3 s, porque o 02 já começa com a bateria
  tocando.
- O final é o mesmo do 01: acorde de Dó sustentado.
- A EDL usada está em `validacao/edl-02-video-editado.json`.

## Vídeo 03: trechos do 01 usados, reenquadramento e cortes

Trilha de 128 BPM: 1 batida = 0,469 s. Todas as trocas de bloco e de painel caem numa batida.

| No 03 | Bloco | Material do 01 (início · duração) | Recorte no 01 (x, y, largura, altura) → painel 9:16 |
|---|---|---|---|
| 0,00–1,88 | **Gancho novo**: "Seu time ainda faz tudo à mão?" | fundo: 30,00 s · 1,88 s (transcrição da cena 06, desfocada) | 150, 300, 480×853 → 1080×1920 |
| 1,88–4,69 | Contexto: 75% | 10,00 s · 2,81 s (contador subindo até 75%) | 80, 330, 960×410 → 1000×427 |
| 4,69–5,63 | Evidência: +14% no atendimento | 37,65 s · 0,94 s | 105, 305, 550×550 → 740×740 |
| 5,63–6,56 | Evidência: 55% na programação | 38,25 s · 0,94 s | 685, 305, 550×550 → 740×740 |
| 6,56–7,50 | Evidência: +40% na consultoria | 38,85 s · 0,94 s | 1265, 305, 550×550 → 740×740 |
| 7,50–9,38 | Onde a IA ganha tempo (coluna 1) | 22,95 s · 1,88 s | 100, 312, 860×568 → 1000×660 |
| 9,38–11,25 | Onde a IA ganha tempo (coluna 2) | 23,60 s · 1,88 s | 960, 312, 860×568 → 1000×660 |
| 11,25–15,00 | Conclusão, com a mesma mensagem da cena 10 | texto refeito na vertical, em legenda cinética | — |

- **Selecionado (maior impacto):** o dado de adoção, os três resultados medidos, as quatro aplicações e a frase
  final.
- **Não usado:** cenas 01, 02, 04, 06 (exceto como fundo do gancho), 08 e 09.
- **Reorganizado:** a ordem segue a do 01, mas as evidências foram fatiadas em três cortes rápidos, um por estudo,
  e as aplicações em duas colunas.
- **Adicionado só no 03:**
  - o gancho;
  - as legendas cinéticas com destaque da palavra ativa;
  - o "punch" de zoom em cada corte;
  - um flash curto na troca de bloco.
- Os recortes respeitam blocos inteiros do 01, então nenhum número, rótulo ou fonte ficou cortado. A ampliação
  máxima foi de 1,35×, nos cartões de evidência.
