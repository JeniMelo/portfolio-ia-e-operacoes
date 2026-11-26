# Edição de vídeo e imagem com Claude Code

Desenvolvi um sistema local com Claude Code, Python e FFmpeg para editar aulas e reaproveitar trechos em redes sociais. Nesta demonstração, os slides, a voz e a webcam são fictícios.

## De uma aula a dois formatos

| Material | Resultado |
|---|---|
| [Aula bruta](antes-aula-bruta.mp4) | 56,4 segundos com espera inicial, pausas e uma falha técnica simulada |
| [Aula editada](depois-aula-editada.mp4) | 28,8 segundos após os cortes, com áudio normalizado |
| [Corte vertical para redes sociais](depois-corte-vertical.mp4) | 10,9 segundos em 1080 × 1920, com legenda que destaca a palavra falada |

A transcrição local com faster-whisper orienta a seleção dos trechos. Os pontos de corte são conferidos no áudio e nos quadros do vídeo. Veja a [abertura](validacao-inicio.png), o [encerramento](validacao-fim.png) e a forma de onda [antes](onda-antes.png) e [depois](onda-depois.png).

## Realce de imagem por IA

O Real-ESRGAN ampliou uma [arte de 480 × 270](antes-baixa-resolucao.png) para [960 × 540](depois-realce-ia-x2.png). A comparação mostra as letras ampliadas na mesma escala.

![Comparação entre ampliação bicúbica e realce por IA](comparacao-zoom.png)

## Correção de cor da webcam

Uma máscara separa a pessoa do fundo para corrigir o tom azulado da [webcam fictícia](antes-webcam-ficticia.mp4). No [vídeo corrigido](depois-cor-corrigida.mp4), ainda há um halo discreto próximo à cabeça.

![Webcam original, máscara e correção de cor](previa-mascara.png)
