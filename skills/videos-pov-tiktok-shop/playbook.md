# Playbook TikTok Shop

> Regra: aqui só entra o que tem fonte ou foi medido nos nossos vídeos. Hipótese fica marcada como hipótese.
> Cada vídeo tem `ficha.md` na pasta dele. Ao juntar 3+ fichas com métricas, comparar e atualizar este playbook.

## O que as fontes dizem (pesquisa de 2026-10-15)
- **Estrutura oficial do TikTok Shop** (guia da Academy, maio/2026, via resumo da PPC Land): gancho → mensagem principal → CTA. O gancho ocupa os **primeiros 3 a 6 segundos** e precisa ser sobre o produto. CTA pode ser falado ou em texto na tela. O próprio guia chama isso de diretriz, não regra.
- **Formatos que o guia lista:** review pessoal, antes e depois, unboxing, tutorial. O nosso POV é um "unboxing/demonstração" sem rosto.
- **Demonstrar > descrever**, produto visível desde o primeiro quadro, responder a principal objeção (blogs de agência e guia em PT; direcional, sem dado público).
- **Métricas que importam:** taxa de conclusão (vídeo longo ou meio arrastado derruba), CTR de produto (cliques ÷ views × 100), conversão clique → compra, vendas/GMV. Benchmarks publicados divergem entre agências: não usar como meta até termos os nossos números.
- **Não existe fórmula:** o caminho é produzir variações, medir retenção, cliques e vendas, e repetir o que funcionou.

## O que os nossos vídeos ensinaram
- Erro de IA (peça deslizando, zíper inventado, mão sem braço) tem que ser cortado: o Lucas pega na hora. Revisão quadro a quadro antes de entregar.
- Corte no meio do take só por erro; corte sem motivo fica abrupto.
- 2026-10-19: 1ª venda: jaqueta (~1.000 views), também feita no Flow pelo Lucas, abrindo com o pacote do TikTok sendo rasgado. A calça (180 views) abriu colocando peças na cama vazia.
- 2026-10-19 (TikTok Studio): todos os vídeos da conta seguram ~3s em média e 0–5% assistem até o fim; a maioria sai em 0:01–0:02. A calça teve retenção igual ou melhor que a jaqueta e a camisa do Brasil (3,22s vs 2,94–3,01s). A diferença de views não veio da retenção. Prioridade: o 1º segundo.

- Crítico cego vale a pena: na calça pegou 5 problemas que eu e a revisão por folha de contato deixamos passar (2026-10-15).

- 2026-10-20 — referência @eulucsantos (17 vídeos >100 mil em 47 dias): 8 s em 3–6 trechos curtos (jump cuts de 1,5–2,5 s), 2 peças sobrepostas ocupando o quadro, ação desde o 1º quadro, texto nativo pequeno do TikTok com emoji ("Essa aqui é padrão ein 🤝💀"), ~3 posts/dia. Hipótese: formato curto com cortes rápidos + volume.

- 2026-10-20 — **O "emborrachado" vinha do modelo de vídeo.** Todos os takes até aqui foram no *Omni 1.1 Flash* (padrão do Flow, 12 créditos). Mesmo prompt e imagem: Flash dobra a peça numa faixa rígida; **Veo 3.1 Fast (20 cr.)** e **Veo 3.1 Quality (100 cr.)** esticam com caimento, brilho e peso real. Fast já resolve; Quality um pouco mais nítido. Kling 3.0 e Seedance 2.0 (API Higgsfield) não testados: conta da API sem créditos.

## Modelos de vídeo em teste (regra do Lucas, 2026-10-20: NUNCA abandonar um modelo por causa de outro — manter vários, medir cada um, comparar)
| Modelo | Estrutura | Texto | Exemplos |
|---|---|---|---|
| A · Nosso completo | pacote → jogar na cama → esticar → tecido → tirar tudo; 12–13 s; 1.6x | headline grande (`HL_STYLE=grande`) | calça, camisa de compressão v2 |
| B · Jaqueta (vendeu) | pacote → esticar → tecido → tirar; ~11–12 s | texto nativo pequeno | jaqueta original (1ª venda) |
| C · Narração | estrutura do vídeo viral + narração edge-tts + legenda palavra por palavra | headline + legenda | camiseta dry fit, jaqueta v3 |
| D · @eulucsantos (**PADRÃO aprovado 2026-10-20**, ver receita-padrao.md) | peça já enchendo o quadro e mão esticando no 0,0 s; 2 peças sobrepostas com mangas vazando pelas bordas; 4–6 trechos de 1,5–2,5 s; 1–2 trechos com zoom 1,3–1,5x (`cortes.txt` 5ª coluna); ~8 s; 60 fps; `EQ="saturation=1.6:contrast=1.08"`; fim varrendo tudo | `HL_STYLE=nativo` (TikTok Sans 700 w110, contorno+halo) | camisa de compressão `modelo-d/final-d.mp4` (takes reaproveitados) |
Cada vídeo novo diz na ficha qual modelo é. Com métricas, comparar por modelo, não por vídeo isolado.

## Hipóteses para testar (uma variável por vez)
- Headline grande (Arial Black) vs texto nativo pequeno do TikTok. (Preço na headline: proibido pelo Lucas.)
- Abrir com a ação mais forte (esticar) vs abrir colocando na cama.
- 13s vs ~20s.
- Narração (edge-tts) vs só música do TikTok — mesma edição, duas versões.
- Fim com cama vazia vs fim com a mão tampando a câmera (card 8).

## Fontes
- https://ppc.land/tiktok-shops-shoppable-video-content-guide-tells-creators-what-actually-works/
- https://www.viniensina.com.br/videos-que-vendem-tiktok-shop/
- https://www.shortformnation.com/blog/tiktok-shop-affiliate-analytics-what-to-track-and-why-most-programs-get-it-wrong
- https://megadigital.ai/en/blog/how-to-become-a-tiktok-shop-affiliate/
