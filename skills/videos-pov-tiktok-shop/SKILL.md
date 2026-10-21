---
name: videos-pov-tiktok-shop
description: "Vídeos POV (mãos + produto) para TikTok Shop com IA: roteiro da Vyral ou vídeo viral de referência → cenas, imagem base e takes no Google Flow, narração com legenda palavra por palavra e edição no FFmpeg."
---

# Vídeos POV para TikTok Shop

Use quando o usuário mandar um roteiro da Vyral (blocos GANCHO / DESENVOLVIMENTO / PROVA / OBJEÇÃO / CTA) ou o link de um vídeo viral de referência, pedir para planejar as cenas de um vídeo POV ou pedir um prompt de cena.

Mesma loja, mesmas mãos, mesmo cenário para todos que usam esta skill. Abaixo, `<skill>` = o diretório base desta skill (aparece quando ela carrega).

## COMECE AQUI: `<skill>/estilos.md`
Todo vídeo = um **estilo** (Lucena, Original, Headline, Narração) + uma **combinação de takes** (catálogo T1–T10). Antes de gerar:
1. Leia `estilos.md` (estilos, catálogo de takes, como escolher, diário de testes com métricas).
2. Pergunte ou proponha o estilo (padrão: **Lucena**, receita em `receita-padrao.md`) e a combinação de takes com o motivo ligado ao produto (elástico → esticar; logo → close; zíper → T7). Mude UMA coisa em relação ao último vídeo.
3. Gere sempre no **Veo 3.1 Fast**.
4. Ao entregar: abra o vídeo e a pasta dele no Explorer (`Start-Process <mp4>; Start-Process explorer.exe "/select,<mp4>"`) e acrescente a linha do vídeo no diário de testes.
O resto desta skill é detalhe e histórico; se algo conflitar, vale `estilos.md` / `receita-padrao.md`.

## Primeira vez nesta máquina (faça sozinho, sem perguntar)
Se o usuário disser "vamos começar" ou for o primeiro vídeo:
1. Confira e instale o que faltar: `ffmpeg -version` (senão `winget install Gyan.FFmpeg`), `python -c "import edge_tts"` (senão `pip install edge-tts`), `python -m yt_dlp --version` (senão `pip install "yt-dlp[default,curl-cffi]"`).
2. Pasta dos vídeos: `~/tiktok-shop/videos/` (crie se não existir).
3. Navegador: precisa da extensão Claude in Chrome conectada e do usuário logado no Google Flow (https://flow.google.com). Login é sempre ele quem faz.
4. Projeto no Flow: se o usuário ainda não tem um projeto com a imagem base, crie um projeto novo e suba `<skill>/imagens/base-maos-cama.jpg` (é a cama + mãos de luva preta + relógio). Pelo `file_upload` da extensão ou pedindo para ele arrastar o arquivo.
5. Depois peça o produto (link do TikTok Shop) e o roteiro da Vyral ou o link de um vídeo viral de referência.

**Vários modelos de vídeo, sempre (regra do Lucas):** o playbook lista os modelos em teste (A, B, C, D...). Um modelo novo nunca substitui os outros; cada vídeo registra qual modelo usou. O que já foi aprendido (escala, Nano Banana Pro, fechamento completo, relógio) vale para todos.
**Detectar corte em vídeo de referência:** scdet com limiar baixo (4) e conferir quadro antes/depois de cada pico; limiar alto perde jump cut entre cenas parecidas (erro de 2026-10-20).
**Antes de planejar:** leia `<skill>/playbook.md` (o que já sabemos e as hipóteses em teste). Cada vídeo testa no máximo uma variável nova.
**Ao entregar o vídeo:** crie `ficha.md` na pasta do vídeo (o que foi feito, takes descartados, edição, headline; métricas em 48h e 7 dias). Se existir `~/cerebro/pessoal/tiktok-shop/videos/` (máquina do Lucas), a ficha vai para lá.

**Crítico cego (Gauntlet):** não rode por conta própria, gasta muito token. Só quando o usuário pedir.

**Ferramentas:** `<skill>/ferramentas/editar.sh` e `<skill>/ferramentas/narrar_legenda.py`.

Responda sempre em português. Os prompts saem em inglês, como no original (exceto os que já são em português).

## Fonte dos prompts: `<skill>/prompts.md`
- Banco com o texto ORIGINAL de todos os cards abaixo (biblioteca VSA Ultra + Doc de prompts). **Não acesse a biblioteca nem o Doc**: está tudo lá. Ache pelo id (`## 43 ·`).
- Use o texto FIEL ao original. Só mude o que a seção "Adaptação masculina" manda. O prompt fica igual ao que funciona.
- Além dos cards numerados: **colocar** (colocar peças na cama uma por uma, 2 imagens: início e fim) e **fechamento** (tirar peças da cama uma por uma).

## Catálogo POV (ids do `prompts.md`)

### Imagens (montar a cena)
| id | Card | O que faz | Imagens |
|---|---|---|---|
| 2 | Remover roupas/textos | Limpa um print de vídeo de referência: tira roupa, mãos e textos. Trocar a descrição do cenário pelo que aparece no print. | 1: print |
| 3 | Colocando a mão no ambiente | Põe as mãos no cenário vazio. **Só se precisar refazer a imagem base: usar o kit da mão abaixo.** | 1: cenário vazio |
| 4 | Colocar roupa no ambiente | Coloca a peça do produto na cena com as mãos. Base dos vídeos. | 1: cena com mãos · 2: produto |
| 1 | Recriando cenário | Troca a peça numa cena que já tem roupa, "como se tivesse saído da embalagem" na cama. | 1: cena com mãos+roupa · 2: produto |
| 5 | Roupa no pacote | Troca a roupa dentro de um pacote transparente (para o gancho do pacote). | 1: cena com pacote · 2: produto |
| 6 | Colocar embalagem do TikTok | Põe o pacote preto do TikTok Shop nas mãos. Lembrete do card: o pacote deve ser pequeno. | A: cena com mãos · B: pacote |

Se a imagem da cena NÃO tem roupa (caso da imagem base com mãos), no card 4 troque "Remove the clothing item from Image 1 and include..." por "Add the clothing item from Image 2..." e posicione a peça no centro, entre as mãos.

### Vídeos (todos Google Flow, vertical 9:16, salvo indicado)
| id | Card | Ação | Entrada | Melhor para |
|---|---|---|---|---|
| 43 | Gancho esticar rápido POV (IA) | Pega a peça de cima, estica forte 3x perto da câmera, devolve; repete com a próxima. Regra de pegada: blusa pelo peito, **calça/short pela cintura**. ~10s, com áudio de tecido. | imagem do card 4 | GANCHO (elasticidade, resistência) |
| 7 | Gancho esticar a roupa | Estica a peça de cima devagar, em loop. | imagem do card 4 | GANCHO calmo |
| 11 | Gancho pacote transparente | Rasga o pacote transparente com som e levanta a peça. ~5s. Ativar som no Flow. | imagem do card 5 | GANCHO unboxing |
| 12 | Gancho embalagem TikTok Shop | Rasga o pacote preto e tira as peças uma por uma (prompt em PT, editar ROUPA 1/2/3). Ativar som no Flow. | imagem do card 6 | GANCHO unboxing com várias peças |
| 10 | Gancho jogar roupa — opção 2 | Tira as peças do quadro e recoloca. Tem versão ESPECÍFICA (descrever cada peça) e PADRÃO (PT). | imagem do card 4 | GANCHO / variedade |
| 15 | Mostrar o tecido de perto | Pega uma peça, leva perto da câmera e passa os dedos no tecido. 8s. Original diz "blouse": trocar pela peça certa. | imagem do card 4 | DESENVOLVIMENTO (tecido, conforto) |
| 13 | Passar a mão na roupa | Peça fica na cama; mãos abrem e mostram detalhes (alça, gola, costura). Até 2 peças. | imagem do card 4 | DESENVOLVIMENTO / OBJEÇÃO |
| 39 | Passar a mão na roupa + zoom | Igual ao 13, com aproximação sutil da câmera no tecido. | imagem do card 4 | DESENVOLVIMENTO (qualidade) |
| 38 | Abrir zíper + zoom | **O texto é idêntico ao 39 e não fala em zíper.** Quando precisar do zíper, acrescente uma linha descrevendo a ação (ex.: abrir o zíper do bolso e mostrar o interior). | imagem do card 4 | OBJEÇÃO (bolso, zíper, fechamento) |

> **Zíper no Flow (testado 2026-10-15, calça):** o card 38 com a linha do zíper não abriu nada (o zoom tomou o vídeo). Prompt próprio com o zíper como ação principal abriu um zíper inventado no meio da calça. Funcionou no lugar certo só quando o prompt disse: quantos zíperes existem, de que lado da imagem, cor da fita e do puxador, e "o centro NÃO tem zíper". Ainda assim o zíper abriu longo demais (até o joelho) e fechou num salto: diga também o comprimento ("short pocket zipper, about one hand long").
| 14 | Mostrar as peças | Pega 2 peças, uma de cada vez, mostra perto da câmera, estica e devolve. | imagem do card 4 | PROVA (cores/variações) |
| 8 | Gancho tapar câmera e pegar produto | Mostra detalhes na cama e, no fim, a palma tampa 100% da câmera (transição). | imagem do card 4 | Transição entre cenas / CTA |

## Mapa roteiro → cena (ponto de partida, ajustar ao produto)
- **GANCHO**: 43 (peça elástica) · 11 ou 12 (unboxing) · 7 · 10.
- **DESENVOLVIMENTO** (tecido, conforto, toque gelado): 15 · 39 · 13.
- **PROVA** (várias cores, comprei todas, preço): 14 · "colocar peças na cama uma por uma" (doc) · 10.
- **OBJEÇÃO / detalhes** (bolso, zíper, cintura, costura): 38 (com linha do detalhe) · 13.
- **CTA**: 8 (palma tampa a câmera) · "fechamento tirar peças" (doc). O card 8 é o texto do 13/39 + palma: se a cena anterior for 13, 38 ou 39, use o fechamento do doc.
- Evite repetir a mesma ação em cenas seguidas. Um vídeo típico: 4 a 6 cenas.

## Kit da mão masculina (identidade fixa da loja)
- Mãos masculinas com **luvas pretas de nitrilo**, **antebraços com tatuagens em preto e cinza** (fechamento de braço) e **relógio de pulseira de metal preta e mostrador preto no pulso esquerdo**.
- Cenário: cama com lençol amassado, **iluminação laranja (esquerda) e azul (direita)**, câmera de cima.
- Imagem base pronta: `<skill>/imagens/base-maos-cama.jpg` (no Flow do Lucas se chama "Adding masculine hands to scene"). É a imagem 1 do card 4.
- Se precisar gerar as mãos de novo: adaptar o card 3 trocando "feminine hands / fair skin / nails / bracelets / ring / small tattoo" por: two masculine adult hands wearing fitted matte black nitrile gloves; forearms with black and grey sleeve tattoos (no text in the tattoos); a black metal link wristwatch with black dial on the left wrist; no rings, no bracelets.

## Adaptação masculina (únicas mudanças permitidas no texto original)
- "feminine hands" / "the woman's hands" / "she" → "masculine hands" / "the man's hands" / "he".
- Onde o prompt fala de mãos/unhas/acessórios ("white nails", "nails", "manicure", "bracelets", "rings", "red nails") → "black nitrile gloves, tattooed forearms, wristwatch".
- Em HAND CONSISTENCY, trocar "Keep the exact same manicure" por "Keep the exact same black gloves • Keep the exact same tattoos • Keep the exact same wristwatch".
- "carpet" / "rug" → "bed sheet" (ou o cenário que estiver em uso), e manter "the same orange and blue lighting" quando for o cenário da cama.
- "blouse" → nome da peça real (pants, shorts, t-shirt...).
- Corrigir erros de digitação do original (ex.: "Ωproducts" no card 7).
- Não reescrever, resumir nem "melhorar" o resto do prompt.

## Checagem do roteiro
- A Vyral pode gerar o roteiro em voz feminina ("lindas", "as minhas"). Se o produto/conteúdo é masculino, avisar e oferecer a versão masculina do texto.

## Referência viral (TikTok) → estrutura do vídeo
Testado 2026-10-16 (camiseta dry fit). O usuário manda o link de um vídeo de IA que estourou; copiamos a estrutura, não o roteiro da Vyral (que costuma ser de vídeo com pessoa real).
1. Baixar: `python -m yt_dlp --impersonate chrome -o "referencia/ref.%(ext)s" <link>` (precisa de `pip install "yt-dlp[default,curl-cffi]"`; sem o impersonate o TikTok recusa). No Chrome o vídeo do TikTok não toca na automação (só a capa).
2. Métricas públicas: `python -m yt_dlp --impersonate chrome --skip-download --print "%(duration)s | views=%(view_count)s likes=%(like_count)s" <link>`.
3. Folha de contato (fps=2) + detecção de corte (`scdet`) + volume (`ebur128`). Se tiver legenda queimada, recorte só a faixa da legenda a fps=6 e leia as palavras: vira a transcrição sem precisar de Whisper.
4. Anote: duração, nº de cortes, o que as mãos fazem em cada trecho, headline, estilo de legenda, narração. Depois mapeie cada trecho num take nosso.

## Imagem base no Flow (produto na nossa cama)
1. Foto do produto: o link do TikTok Shop traz a imagem principal no parâmetro `og_info` da URL (CDN ibyteimg) — baixe com curl. A página do produto pode abrir CAPTCHA: feche, nunca resolva.
1b. **Link é de vídeo, não de produto** (vt.tiktok.com → /video/): a web não mostra a sacolinha. Baixe com yt-dlp e tire a foto de um quadro onde o produto aparece inteiro e esticado (ffmpeg -ss T -frames:v 1), recortando texto e fundo. Testado 2026-10-19 (camisa de compressão).
1c. **Subir arquivo local no Flow (testado 2026-10-19):** copie a imagem para a área de transferência do Windows (PowerShell: `[System.Windows.Forms.Clipboard]::SetImage(...)`), clique na caixa de comando e aperte Ctrl+V. Avise o usuário que a área de transferência dele foi trocada.
2. Subir a foto no Flow sem seletor de arquivo: no console da página do Flow, `fetch(url)` → `File` → disparar `paste` com `DataTransfer` na caixa de comando (contenteditable). Ela entra como ingrediente.
3. A imagem base (`base-maos-cama.jpg`) já está no projeto: ⋮ → Incluir no comando.
4. Configuração → Imagem (**Nano Banana Pro, nunca o 2.1** — regra do Lucas, 2026-10-19; 9:16, x1). Prompt = card 4 adaptado + **escala explícita**: "cada peça tem uns 4 palmos de largura; juntas ocupam ~85% da largura do quadro; nunca pequenas". Sem isso as peças saem pequenas (calça).
4b. **Tamanho da peça (erro repetido: calça e camisa de compressão).** Peça pequena em relação às mãos derruba a qualidade. Inclua como referência de escala a imagem da jaqueta que vendeu (`produto no ambiente.jpg`, também em `imagens/` da pasta 2026-10-13-jaqueta) e diga: "match the garment scale of the jacket reference: adult size, torso about three gloved hands wide, sleeves fully visible". Compare com o vídeo de referência antes de gerar os takes. **Medida:** tronco de camisa adulta = 4 a 5 larguras de mão; com as nossas mãos perto da câmera, 2 camisas NÃO cabem lado a lado em tamanho real. **O que funcionou (camisa de compressão, 2026-10-19):** gerar primeiro a disposição certa (pode sair pequena) e depois EDITAR essa imagem: "make both shirts much bigger… the white underneath shifted right, the black on top shifted left overlapping half". Pedir tamanho grande + 2 peças de uma vez (com a jaqueta de referência) fez o Nano Banana fundir as duas numa camisa só, metade preta e metade branca (3 de 3 tentativas).
5. No vídeo há durações 4/6/8/10s no mesmo painel.
6. **Estrutura obrigatória (regra do Lucas):** pacote → **jogar/colocar as peças na cama** → esticar → tecido → **fechamento tirando TODAS as peças** (nunca parar com peça na cama). O take de colocar é feito no modo **Elementos** (não Frames): imagem da cama vazia com as mãos + imagem final com as peças, prompt "colocar" do banco.

## Gerar no Flow (Claude opera o Chrome do usuário)
Testado em 2026-10-14 (cena 4 da calça, ~40s para gerar).
1. Abra o projeto numa aba sua do grupo MCP (`https://flow.google.com/project/<id>`). Não feche a última aba do grupo no meio: o grupo some e as ids mudam.
2. Na imagem de entrada, menu ⋮ → **Animar**: ela vira o frame "Início". Para 2 frames (ex.: colocar uma por uma), preencha também "Fim".
2c. **Esticar (regra do Lucas, 2026-10-20):** esticada moderada com vai e volta (4–5 vezes, "nheque-nheque"), a peça volta ao lugar. Nunca puxão brusco, como se fosse rasgar, nem peça voando. Escreva isso no prompt: "gentle rhythmic stretch-and-release… NOT a strong yank".
2b. **Modelo de vídeo: Veo 3.1 Fast (20 créditos), nunca o Omni 1.1 Flash padrão** para takes de esticar/manusear — o Flash deixa o tecido emborrachado (teste 2026-10-20). Quality (100) só para o take principal. Confira também a proporção 9:16: ao trocar de modelo ela pode voltar para 16:9, e o x2 da imagem passa para o vídeo.
3. Clique na caixa "O que você quer criar?", digite o prompt **numa linha só** (Enter pode enviar) e confira o rodapé: `Vídeo · 720p · 8s · 9:16 · x1`.
4. Clique na seta. O vídeo aparece como 1º card do projeto.
5. **Revisar cada take antes de mostrar ao usuário** (o player é canvas, sem `<video>` no DOM). Abra o card no editor; a régua da timeline vai de x≈20 (0s) a x≈836 (8s), ~102 px/s, em y≈345. Para cada tempo (0, 1, 2 … 7,9s; 0,5s onde houver ação): clique na régua → botão tela cheia → espere 0,7s → zoom no quadro → botão sair da tela cheia (NÃO Esc: Esc sai do editor). Nunca revisar com o vídeo rodando em loop.
6. Checklist por take: a ação principal do prompt aconteceu? peça inventada/duplicada ou detalhe novo (bolso, zíper, estampa)? peça some/teletransporta? mão/braço sem corpo ou deformado? câmera pula ou zoom volta de uma vez? último quadro bate com o que a próxima cena espera? Veredito: APROVADO / REPROVADO + o motivo com o segundo.

## Narração + legenda palavra por palavra (estilo da referência)
- `python <skill>/ferramentas/narrar_legenda.py narracao.txt audio/narracao [voz] [rate]` (precisa de `pip install edge-tts`) → `audio/narracao.mp3` + `audio/narracao.ass` (1 palavra por vez, Arial Black branca contorno preto, ~83% da altura). Voz padrão pt-BR-AntonioNeural +15%.
- Texto da narração segue a estrutura da referência: produto/oferta → benefício do tecido → caimento → escassez → CTA ("carrinho laranja aqui embaixo"). Não cite preço sem conferir a variação do kit.
- Encaixe cada frase num take pelo tempo da 1ª palavra da frase no .ass (`grep` nas palavras-chave).
- Escreva a narração numa frase só, separada por vírgulas: com ponto final o edge-tts faz pausas de ~0,8s (23% do vídeo mudo na 1ª versão da camiseta).
- Legenda em caixa preta sólida (BorderStyle 3), como a referência: contorno sozinho some em cima de camiseta branca.
- CTA "aponta pro carrinho": a IA não entende "apontar pro canto" (fez os indicadores apontarem um pro outro). Funcionou com alvo físico: "o indicador direito toca a cama no canto inferior esquerdo 3 vezes, como apertando um botão".
- Acessório (relógio etc.) troca de cor entre takes ou no meio do take: descreva "black metal wristwatch with black dial" no prompt de todo take e corte os trechos em que ele muda.
- O crítico cego não conhece gíria: "não marca pizza" (mancha de suor) é expressão brasileira e fica.
- Edição: `bash <skill>/ferramentas/editar.sh` dentro da pasta do vídeo, com `cortes.txt` (`take inicio fim velocidade`), `headline.txt` e `audio/`. Velocidade por trecho (1x a 1.25x com narração; 1.6x no formato só-música).

## Baixar e editar (FFmpeg)
Testado em 2026-10-15 (calça, 4 takes → 12,9s).
1. Baixar cada take no Flow: ⋮ → Fazer o download → **1080p** (não existe 2K; 4K pede upgrade). O upscale leva ~1 min; um por vez. Cai em `~/Downloads`; copie para `<pasta do vídeo>/takes/N-nome.mp4`.
2. Folha de contato por take (1 quadro a cada 0,5s com tempo): `ffmpeg -i take.mp4 -vf "fps=2,scale=180:-1,drawtext=fontfile=revisao/arial.ttf:text='%{pts\:hms}':...,tile=8x2" -frames:v 1 revisao/take.png` (copie a arial.ttf do sistema para `revisao/`: caminho com `C:` quebra o filtro). Leia a imagem e escolha os trechos sem erro.
3. Padrão que funcionou: **13s no total, 1.6x**, ordem colocar na cama → esticar → tecido de perto → tirar da cama. 13s × 1.6 = ~20,8s de bruto para distribuir entre os takes.
4. Escreva `cortes.txt` (uma linha por trecho: `take inicio fim velocidade`, ex. `2-tecido 0.5 6.0 1.6`) e rode `bash <skill>/ferramentas/editar.sh` dentro da pasta do vídeo → `final.mp4` (1080x1920, 30fps). Lê também `headline.txt` e `audio/` se existirem. Ajustes por variável: `HL_Y`, `HL_SIZE`, `BG_VOL`, `OUT`.
5. Na escolha dos trechos, corte também a TRANSIÇÃO entre ações: peça deslizando/arrastando por cima de outra (ex.: bege passando na diagonal sobre a preta) parece errado mesmo sem deformar. Entre direto na ação já acontecendo (jump cut funciona no TikTok). Erro pego na revisão humana da calça, não na do Claude.
   **Regra: só corte no meio de um take se tiver erro** (corte sem motivo fica abrupto). Para caber nos 13s, apare o começo e o fim dos takes.
6. **Headline** (obrigatória): `headline.txt` na pasta do vídeo, uma frase por linha (3 linhas curtas, MAIÚSCULAS). **Nunca preço na headline (regra do Lucas, 2026-10-19).** Título chamativo sobre achado/qualidade (ex.: "NÃO ACREDITO QUE ESSAS / 3 CALÇAS SAÍRAM / QUASE DE GRAÇA!", "ESSA JAQUETA DRY FIT / É OUTRO NÍVEL"). O `editar.sh` desenha em Arial Black (`ariblk.ttf` copiada para a pasta), branca com contorno preto (borderw=7), fontsize 58, a 20% da altura, o vídeo todo. Emoji fica de fora (drawtext não desenha emoji colorido); use "!". Confira um quadro: a linha mais longa não pode encostar nas bordas (os botões do TikTok ficam à direita).
6b. **Take do Flow pode abrir com 3–4 quadros da cena vazia** (fechamento da jaqueta, 2026-10-19): a folha de contato a fps=2 não pega. Comece todo corte em ≥0,2s ou confira os 8 primeiros quadros (`select=lt(n,8)`).
7. Revise o `final.mp4` com folha de contato (fps=3) e amplie qualquer trecho suspeito antes de entregar.
8. **Ao terminar, abra o vídeo E a pasta dele** (regra do Lucas): Windows `Start-Process <mp4>; Start-Process explorer.exe "/select,<mp4>"`; Mac `open <mp4>; open -R <mp4>`.
FFmpeg: do PATH; no Windows, se não estiver no PATH, `winget install Gyan.FFmpeg` (o `editar.sh` acha sozinho).

## Formato da resposta (Claude Code)
O usuário copia os prompts de uma página com botão de copiar, não do terminal.
1. Pasta do vídeo: `~/tiktok-shop/videos/AAAA-MM-DD-<produto>/`. **Toda imagem usada vai para `imagens/` dentro dela** (foto do produto, produto no ambiente, frames de início/fim), baixada do Flow em 1080p. É o que permite replicar um produto que vendeu sem caçar no Flow.
2. Escreva `conteudo.html` lá, copiando a estrutura de `exemplo-conteudo.html` (nesta skill): header com título e `.progress`, bloco do roteiro, bloco das imagens na ordem, um `<article class="scene">` por prompt (número, título, `.beat` com bloco + card, `.line` com a fala, `.meta` com ferramenta/entrada e `li.warn` para som ligado ou alerta, `<pre>` com o prompt, actions com copy/more/checkbox), e uma `.note` de no máximo 2 linhas sobre o que foi adaptado. Escape `&` e `<` no `<pre>`.
3. Monte com `template.html` desta skill trocando `{{TITULO}}` (nome curto: "<Produto> POV") e `{{CONTEUDO}}`, salve como `prompts.html`, e publique com a ferramenta Artifact (icon `video`).
4. No chat: só o link, a tabela roteiro → cena e os alertas. Nada de prompt no terminal.
