"""Gera o painel HTML da Central de Pendências a partir do pendencias.json.

Uso: python gerar_painel.py <pendencias.json> <painel.html>

O painel é um arquivo único, sem dependências externas. As baixas feitas nele ficam
salvas no navegador (localStorage) e podem ser copiadas para o estado.json da próxima rodada.
"""
import html
import json
import sys
from pathlib import Path

MODELO = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Central de Pendências</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--txt:#1d2330;--sub:#5f6878;--linha:#e3e6eb;--marca:#2f6fdf;
--alta:#c8372d;--media:#b7791f;--baixa:#4a7c59;--ok:#2e7d4f;--chip:#eef1f6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#12151b;--card:#1b2029;--txt:#e7eaf0;
--sub:#9aa3b2;--linha:#2a313d;--marca:#6c9cf0;--chip:#252c38}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--txt);
font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:24px 16px 48px}
header h1{margin:0;font-size:24px}header p{margin:4px 0 0;color:var(--sub)}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:20px 0}
.stat{background:var(--card);border:1px solid var(--linha);border-radius:10px;padding:12px}
.stat b{display:block;font-size:24px}.stat span{color:var(--sub);font-size:13px}
.tabs{display:flex;gap:6px;border-bottom:1px solid var(--linha);margin-bottom:14px;flex-wrap:wrap}
.tab{border:0;background:none;color:var(--sub);padding:10px 14px;font:inherit;cursor:pointer;
border-bottom:2px solid transparent}.tab.on{color:var(--txt);border-color:var(--marca);font-weight:600}
.card{background:var(--card);border:1px solid var(--linha);border-left:4px solid var(--linha);
border-radius:10px;padding:14px 16px;margin-bottom:10px}
.card.alta{border-left-color:var(--alta)}.card.media{border-left-color:var(--media)}
.card.baixa{border-left-color:var(--baixa)}.card.concluido{opacity:.75;border-left-color:var(--ok)}
.top{display:flex;gap:8px;align-items:flex-start;justify-content:space-between}
.card h3{margin:0;font-size:16px}.meta{color:var(--sub);font-size:13px;margin-top:4px}
.pills{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.pill{background:var(--chip);border-radius:99px;padding:2px 10px;font-size:12px}
.pill.atrasado{background:var(--alta);color:#fff}.pill.concluido{background:var(--ok);color:#fff}
details{margin-top:8px}summary{cursor:pointer;color:var(--marca);font-size:13px}
blockquote{margin:8px 0;padding:6px 12px;border-left:3px solid var(--linha);color:var(--sub);white-space:pre-wrap}
button.baixa{border:1px solid var(--linha);background:var(--card);color:var(--txt);border-radius:8px;
padding:6px 10px;font:inherit;font-size:13px;cursor:pointer;white-space:nowrap}
.vazio{color:var(--sub);padding:24px 0;text-align:center}.obs{color:var(--sub);font-size:13px;margin-top:24px}
</style>
</head>
<body>
<div class="wrap">
<header><h1>Central de Pendências · __PESSOA__</h1>
<p>__EMPRESA__ · atualizado em __REF__</p></header>
<div class="stats" id="stats"></div>
<nav class="tabs" id="tabs"></nav>
<main id="lista"></main>
<p class="obs">__OBS__</p>
</div>
<script>
const DADOS = __DADOS__;
const CHAVE = "central-demo-baixas";
let baixas = {};
try { baixas = JSON.parse(localStorage.getItem(CHAVE) || "{}"); } catch (e) {}
const ABAS = {comigo: "Comigo", outros: "Com os outros", concluidos: "Concluídos"};
const DIR = {me_pediram: "Me pediram", prometi: "Prometi", eu_pedi: "Eu pedi"};
const ST = {aberto: "Em aberto", atrasado: "Atrasado", aguardando: "Aguardando", concluido: "Concluído"};
const PRI = {alta: 0, media: 1, baixa: 2};
let aba = "comigo";
const status = i => baixas[i.id] ? "concluido" : i.status;
const daAba = i => status(i) === "concluido" ? "concluidos" : (i.direcao === "eu_pedi" ? "outros" : "comigo");
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const br = d => d ? d.slice(8,10) + "/" + d.slice(5,7) : "";
function desenhar() {
  const cont = {comigo: 0, outros: 0, concluidos: 0};
  DADOS.itens.forEach(i => cont[daAba(i)]++);
  const atrasados = DADOS.itens.filter(i => status(i) === "atrasado").length;
  document.getElementById("stats").innerHTML =
    `<div class="stat"><b>${cont.comigo}</b><span>comigo</span></div>` +
    `<div class="stat"><b>${atrasados}</b><span>atrasados</span></div>` +
    `<div class="stat"><b>${cont.outros}</b><span>aguardando outros</span></div>` +
    `<div class="stat"><b>${cont.concluidos}</b><span>concluídos</span></div>`;
  document.getElementById("tabs").innerHTML = Object.entries(ABAS).map(([k, v]) =>
    `<button class="tab ${k === aba ? "on" : ""}" data-aba="${k}">${v} (${cont[k]})</button>`).join("");
  const itens = DADOS.itens.filter(i => daAba(i) === aba).sort((a, b) =>
    (status(b) === "atrasado") - (status(a) === "atrasado") || PRI[a.prioridade] - PRI[b.prioridade] ||
    (a.prazo || "9999").localeCompare(b.prazo || "9999"));
  document.getElementById("lista").innerHTML = itens.length ? itens.map(i => {
    const s = status(i);
    const quem = i.direcao === "eu_pedi" ? `Para ${esc(i.para_quem)}` : `Pedido por ${esc(i.quem_pediu)}`;
    return `<article class="card ${s === "concluido" ? "concluido" : i.prioridade}">
      <div class="top"><div><h3>${esc(i.titulo)}</h3>
      <div class="meta">${quem} · ${esc(i.fonte)} · ${br(i.quando)}${i.prazo ? " · prazo " + br(i.prazo) : ""}</div></div>
      <button class="baixa" data-id="${i.id}">${baixas[i.id] ? "Desfazer" : (s === "concluido" ? "" : "Dar baixa")}</button></div>
      <div class="pills"><span class="pill ${s}">${ST[s]}</span><span class="pill">${DIR[i.direcao]}</span>
      <span class="pill">Prioridade ${i.prioridade}</span>${s !== "concluido" && i.dias_parado ? `<span class="pill">${i.dias_parado} dia(s) parado</span>` : ""}
      <span class="pill">${i.origem === "reuniao" ? "Reunião" : "Conversa"}</span></div>
      <details><summary>Ver origem e último movimento</summary>
      <blockquote>${esc(i.fala)}</blockquote><div class="meta">${esc(i.ultimo_movimento)}</div></details>
    </article>`; }).join("") : `<p class="vazio">Nada por aqui.</p>`;
  document.querySelectorAll("button.baixa").forEach(b => { if (!b.textContent) b.remove(); });
}
document.addEventListener("click", e => {
  const t = e.target.closest("[data-aba]"); if (t) { aba = t.dataset.aba; desenhar(); return; }
  const b = e.target.closest("button.baixa"); if (!b) return;
  if (baixas[b.dataset.id]) delete baixas[b.dataset.id]; else baixas[b.dataset.id] = new Date().toISOString().slice(0, 10);
  try { localStorage.setItem(CHAVE, JSON.stringify(baixas)); } catch (err) {}
  desenhar();
});
desenhar();
</script>
</body>
</html>
"""


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    dados = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    ref = dados.get("referencia", "")
    ref_br = f"{ref[8:10]}/{ref[5:7]}/{ref[:4]} {ref[11:16]}" if len(ref) >= 16 else ref
    pagina = (MODELO
              .replace("__PESSOA__", html.escape(dados.get("pessoa", "")))
              .replace("__EMPRESA__", html.escape(dados.get("empresa", "")))
              .replace("__REF__", html.escape(ref_br))
              .replace("__OBS__", html.escape(dados.get("observacao", "")))
              .replace("__DADOS__", json.dumps(dados, ensure_ascii=False).replace("</", "<\\/")))
    Path(sys.argv[2]).write_text(pagina, encoding="utf-8")
    print(f"{len(dados.get('itens', []))} itens -> {sys.argv[2]}")


if __name__ == "__main__":
    main()