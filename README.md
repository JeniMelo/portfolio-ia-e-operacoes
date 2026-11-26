# Demonstração: um conteúdo, três formatos

Três vídeos sobre **como a inteligência artificial pode transformar a produtividade no trabalho**, produzidos e
editados com o sistema de criação e edição audiovisual que desenvolvi e que opero pelo Claude Code.

O objetivo é mostrar o ciclo completo:
- **criar** uma peça original;
- **reduzir e reorganizar** essa peça sem acelerar nada;
- **adaptar** a mesma peça para o formato vertical das redes sociais.

O vídeo 02 e o vídeo 03 usam o **arquivo MP4 do 01 como material de origem**. Os dois não foram refeitos do zero.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `01-video-original.mp4` | 1920×1080 · 16:9 · 60,0 s · 10 cenas |
| `02-video-editado.mp4` | 1920×1080 · 16:9 · 31,2 s · 5 cenas, cortadas do 01 e reorganizadas |
| `03-video-redes-sociais.mp4` | 1080×1920 · 9:16 · 15,0 s · gancho novo + trechos reenquadrados do 01 |
| `thumbnails/` | uma capa por vídeo, em PNG e JPG |
| `comparativo-formatos.png` | os três formatos lado a lado e a linha do tempo do que cada versão aproveitou do 01 |
| `RELATORIO-EDICAO.md` | o que foi removido, preservado e reorganizado, com os tempos |
| `LICENCAS.md` | origem e licença de cada recurso (música, fontes, dados citados) |
| `recursos/` | as duas trilhas originais em WAV |
| `validacao/` | relatório técnico de validação (JSON) e folhas de quadros de cada vídeo |

## Como cada vídeo foi feito

### 01 · Original (60 s)
- **Motor de motion graphics do sistema** (`motion.py`):
  - cada quadro é desenhado em Python (Pillow) e codificado pelo FFmpeg;
  - nada de banco de imagens: gráficos, ícones e painéis são desenhados por código;
  - há tipografia animada, caixas que "pintam" o texto, contadores com degradê, gráfico de 100 quadrados, mapa
    de rede, cartões e linha do tempo.
- **Roteiro em 10 cenas:**
  - introdução;
  - contexto (dado de adoção);
  - por que agora;
  - aplicações;
  - exemplo prático;
  - evidências de estudos;
  - boas práticas;
  - primeiros passos;
  - conclusão.
  - O 01 tem, de propósito, **informação complementar** que pode sair sem prejudicar a compreensão.
- **Trilha original** de 100 BPM, composta e sintetizada por código e sem vocais. Cada cena dura um número inteiro
  de compassos (1 compasso = 2,4 s), então toda troca de cena cai no início de um compasso.
- Cada cena **começa e termina no mesmo fundo limpo**, com um fade de saída de 0,35 s. Por isso o vídeo pode ser
  cortado entre quaisquer cenas sem salto visual.

### 02 · Editado (31,2 s), feito a partir do MP4 01
- O editor do sistema (`gaolib.render_edl`, o mesmo das aulas longas) recebe uma lista de cortes (EDL) e corta o
  MP4 01, **vídeo e trilha juntos**:
  - a duração é exata por quadro;
  - há micro-fade de 15 ms nas junções;
  - a entrada da música tem fade de 0,3 s;
  - o volume é normalizado em −16 LUFS.
- Como os cortes caem em limites de compasso, a **música continua no ritmo** e termina no acorde final original.
  Não houve aceleração.
- **Ficaram 5 cenas**, e a ordem mudou: as evidências entram antes das aplicações. Os detalhes estão no relatório.

### 03 · Redes sociais (15 s, vertical), feito a partir do MP4 01
- **Recurso novo do motor, `motion.Clip`:** lê quadros reais do MP4 01 já recortados e os coloca em painéis
  verticais.
  - Cada painel é um **bloco inteiro** do 01 (o número com o texto, um cartão, uma coluna de cartões). Assim,
    nenhuma informação é cortada pela mudança de formato.
- **Gancho novo:** "Seu time ainda faz tudo à mão?", sobre um trecho desfocado do próprio 01.
- **Legendas cinéticas:** cada palavra entra numa batida, e a palavra ativa ganha uma caixa de destaque.
- **Trilha mais dinâmica:** 128 BPM, mesma tonalidade e mesmo tema do 01. **Todos os cortes caem na batida**: a
  validação mediu 7 de 7 cortes a no máximo 1 quadro da batida.
- Os textos ficam fora da área coberta pela interface do Reels, TikTok e Shorts (topo e rodapé).

## Diferenças entre as versões

| | 01 Original | 02 Editado | 03 Redes sociais |
|---|---|---|---|
| Objetivo | conteúdo completo | o essencial | impacto e retenção |
| Formato | 16:9 · 1920×1080 | 16:9 · 1920×1080 | 9:16 · 1080×1920 |
| Duração | 60,0 s | 31,2 s | 15,0 s |
| Estrutura | 10 cenas | 5 cenas, reordenadas | gancho + 4 blocos |
| Origem | criação | cortes do MP4 01 | trechos reenquadrados do MP4 01 + gancho e legendas novos |
| Música | 100 BPM, introdução suave | a mesma, cortada nos compassos | 128 BPM, cortes na batida |
| Ritmo | cenas de 4,8–7,2 s | cenas de 4,8–7,2 s | cortes a cada 0,9–1,9 s |
| Volume | −16 LUFS | −16 LUFS | −14 LUFS (padrão de redes) |

## Funcionalidades do sistema usadas

| Funcionalidade | Onde |
|---|---|
| Motor de motion graphics (`motion.py`: tipografia animada, caixas, render com trilha e volume normalizado) | 01, 03 e thumbnails |
| Editor por lista de cortes com sincronia exata (`gaolib.render_edl`) | 02 |
| Validação automática do arquivo final (`gaolib.validate`) | 01, 02, 03 |
| Medição de loudness EBU R128 com ganho fixo (`gaolib.loudness_gain`) | 01, 02, 03 |

### Melhorias feitas no sistema para esta demonstração
1. **Identidade visual configurável:** `motion.set_theme()` troca cores, fontes e o fundo com grade de pontos
   sem mudar as cenas. Antes, o motor só desenhava a identidade original do projeto.
2. **Vídeo de origem dentro das cenas:** `motion.Clip` lê os quadros de um trecho de vídeo com seek exato, recorte
   e escala, para reenquadrar 16:9 em 9:16 e montar fundos. É a base do vídeo 03.
3. **Correção de transparência:** na versão atual do Pillow, desenhar com cor translúcida sobre um quadro RGBA
   gravava o alfa em vez de misturar as cores, então fades e caixas translúcidas saíam opacos. Agora o quadro é
   montado em RGB e a mistura funciona.
4. **Ajustes menores:** entrada da música configurável (`fade_in`) e logo colada com máscara.

## Validação de qualidade (resumo)

O relatório completo está em `validacao/relatorio-validacao.json`.

| Verificação | 01 | 02 | 03 |
|---|---|---|---|
| Resolução / fps | 1920×1080 / 30 | 1920×1080 / 30 | 1080×1920 / 30 |
| Duração do vídeo = duração do áudio | 60,000 = 60,000 | 31,200 = 31,200 | 15,000 = 15,000 |
| Decodificação completa sem erros | ✅ | ✅ | ✅ |
| Telas pretas indevidas / imagem congelada | nenhuma | nenhuma | nenhuma |
| Loudness integrada / pico | −16,0 LUFS / −7,0 dBFS | −15,9 LUFS / −7,3 dBFS | −14,0 LUFS / −5,5 dBFS |
| Música × edição | trocas de cena em início de compasso | 4 junções em limite de compasso | 7/7 cortes a ≤1 quadro da batida |

Além das medições automáticas:
- conferi visualmente as folhas de quadros: legibilidade, enquadramento, transições e coerência do texto depois
  dos cortes;
- o menor texto é de 17 px em 1080p (notas de fonte); títulos e números ficam entre 64 e 250 px.

**O que não dá para medir por script:** a avaliação estética da música (agradável, moderna) depende de ouvir. A
trilha é sintetizada e tem timbre eletrônico simples. Revise antes de publicar.
