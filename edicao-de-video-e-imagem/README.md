# Sistema inteligente de edição audiovisual

**IA aplicada à produção de conteúdo | Automação de processos | Claude Code**

## O desafio

Editar aulas, eliminar pausas, preparar cortes para redes sociais e corrigir imagens são atividades que podem consumir tempo das equipes de conteúdo.

## A solução

Desenvolvi um sistema local de edição audiovisual com Claude Code, Python e FFmpeg, reunindo recursos de edição, transcrição, reaproveitamento de conteúdo e tratamento de imagem.

## Demonstração prática

Os materiais abaixo são fictícios e foram preparados para demonstrar as funcionalidades sem expor conteúdo interno.

### 01 — Edição de aulas

| Antes | Depois |
|---|---|
| [Assistir à aula bruta](antes-aula-bruta.mp4) | [Assistir à aula editada](depois-aula-editada.mp4) |
| 56,4 segundos | 28,8 segundos |

Remoção de esperas, pausas e falha técnica simulada, com normalização do áudio. A duração foi reduzida em aproximadamente 49% nesta demonstração — não se trata de uma medição de economia de tempo de trabalho.

### 02 — Reaproveitamento para redes sociais

[**Assistir ao corte vertical com legendas**](depois-corte-vertical.mp4)

Vídeo de 10,9 segundos em formato 1080 × 1920, com destaque da palavra falada na legenda.

### 03 — Melhoria de imagens com IA

![Comparação visual do realce de imagem](comparacao-zoom.png)

Ampliação de 480 × 270 para 960 × 540 com Real-ESRGAN.

[Imagem original](antes-baixa-resolucao.png) · [Imagem aprimorada](depois-realce-ia-x2.png)

### 04 — Correção de cor da webcam

![Original, máscara e correção](previa-mascara.png)

[Vídeo original](antes-webcam-ficticia.mp4) · [Vídeo corrigido](depois-cor-corrigida.mp4)

A máscara permite tratar a pessoa separadamente do fundo. A demonstração ainda apresenta um halo discreto próximo à cabeça.

## Valor para o negócio

- Potencial de reduzir tarefas repetitivas na edição.
- Reaproveitamento de aulas em diferentes formatos.
- Padronização de etapas de produção audiovisual.

Os benefícios operacionais ainda não foram quantificados em produção.

## Tecnologias e validação

Claude Code, Python, FFmpeg, faster-whisper e Real-ESRGAN.

A transcrição orienta a seleção dos trechos, e os cortes são conferidos no áudio e nos quadros do vídeo.

[Validação da abertura](validacao-inicio.png) · [Validação do encerramento](validacao-fim.png) · [Áudio antes](onda-antes.png) · [Áudio depois](onda-depois.png)

[Voltar ao portfólio](../)
