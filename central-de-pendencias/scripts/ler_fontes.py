"""Normaliza as fontes da Central de Pendências num único JSON.

Uso: python ler_fontes.py <pasta_de_entrada> <saida.json>

Lê:
  pessoa.json            dono da central e data de referência
  estado.json            baixas, excluidos e edicoes já feitas no painel (opcional)
  conversas/*.txt        exportação de chat: "dd/mm/aaaa hh:mm - Autor: mensagem"
  reunioes/*.md          anotações com "## Próximas etapas" e linhas "- [Responsável] Assunto: ação"
"""
import hashlib
import json
import re
import sys
from pathlib import Path

CABECALHO = re.compile(r"^(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+): (.*)$")
TITULO_REUNIAO = re.compile(r"^#\s+(.+?)\s*\((\d{2}/\d{2}/\d{4})\s+(\d{2}:\d{2})\)")
ETAPA = re.compile(r"^-\s*\[([^\]]+)\]\s*([^:]+):\s*(.+)$")


def sha8(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:8]


def iso(data: str, hora: str) -> str:
    d, m, a = data.split("/")
    return f"{a}-{m}-{d} {hora}"


def ler_conversa(arq: Path) -> list[dict]:
    msgs: list[dict] = []
    for linha in arq.read_text(encoding="utf-8").splitlines():
        m = CABECALHO.match(linha)
        if m:
            data, hora, autor, texto = m.groups()
            msgs.append({"data": data, "hora": hora, "autor": autor.strip(), "texto": texto.strip()})
        elif msgs and linha.strip():  # continuação de mensagem com quebra de linha
            msgs[-1]["texto"] += "\n" + linha.strip()
    saida = []
    for x in msgs:
        saida.append({
            "id": sha8(f"{arq.name}|{x['data']} {x['hora']}|{x['autor']}|{x['texto']}"),
            "origem": "conversa",
            "fonte": arq.stem,
            "quando": iso(x["data"], x["hora"]),
            "autor": x["autor"],
            "texto": x["texto"],
            "midia": x["texto"] == "<Mídia oculta>",
        })
    return saida


def ler_reuniao(arq: Path) -> dict:
    linhas = arq.read_text(encoding="utf-8").splitlines()
    nome, quando = arq.stem, ""
    for l in linhas:
        m = TITULO_REUNIAO.match(l)
        if m:
            nome, quando = m.group(1).strip(), iso(m.group(2), m.group(3))
            break
    secao, resumo, etapas = None, [], []
    for l in linhas:
        if l.startswith("## "):
            secao = l[3:].strip().lower()
            continue
        if secao == "resumo" and l.strip():
            resumo.append(l.strip())
        elif secao and secao.startswith("próximas etapas"):
            m = ETAPA.match(l.strip())
            if m:
                etapas.append({
                    "id": sha8(f"{arq.name}|{l.strip()}"),
                    "responsaveis": [r.strip() for r in m.group(1).split(",")],
                    "assunto": m.group(2).strip(),
                    "acao": m.group(3).strip(),
                    "linha": l.strip(),
                })
    return {"origem": "reuniao", "fonte": nome, "quando": quando, "resumo": " ".join(resumo), "etapas": etapas}


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    pasta, destino = Path(sys.argv[1]), Path(sys.argv[2])
    pessoa = json.loads((pasta / "pessoa.json").read_text(encoding="utf-8"))
    estado_arq = pasta / "estado.json"
    estado = json.loads(estado_arq.read_text(encoding="utf-8")) if estado_arq.exists() else {}
    conversas = {a.stem: ler_conversa(a) for a in sorted((pasta / "conversas").glob("*.txt"))}
    reunioes = [ler_reuniao(a) for a in sorted((pasta / "reunioes").glob("*.md"))]
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({
        "pessoa": pessoa,
        "estado": {"baixas": estado.get("baixas", {}), "excluidos": estado.get("excluidos", {}),
                   "edicoes": estado.get("edicoes", {})},
        "conversas": conversas,
        "reunioes": reunioes,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    n_msg = sum(len(v) for v in conversas.values())
    n_et = sum(len(r["etapas"]) for r in reunioes)
    print(f"{len(conversas)} conversas ({n_msg} mensagens), {len(reunioes)} reuniões ({n_et} próximas etapas) -> {destino}")


if __name__ == "__main__":
    main()