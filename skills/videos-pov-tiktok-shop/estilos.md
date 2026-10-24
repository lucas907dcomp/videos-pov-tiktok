# Estilos, takes e testes

Um vídeo = **ESTILO** (a cara: cenário, imagem, texto, ritmo, cor) + **COMBINAÇÃO DE TAKES** (as cenas e a ordem).
O estilo fica fixo; os takes variam de vídeo para vídeo para descobrir o que segura e vende. Não existe fórmula: a gente descobre testando e medindo.
Todo vídeo novo é gerado no **Veo 3.1 Fast** (20 créditos/take), qualquer que seja o estilo.

## Estilos (presets)

### 1. Estilo Lucena (padrão atual)
Espelho do @eulucsantos. Receita completa e prompts em `receita-padrao.md`.
- Cenário: lençol azul royal acetinado, luz laranja forte da esquerda, contraste alto.
- Imagem: peças grandes, tamanho adulto, mangas vazando pelas bordas, uma por cima da outra (Nano Banana Pro, imagem gerada e depois editada pra aumentar).
- Ritmo: 1.3x, 60 fps, trechos de 1,5–4 s, zoom digital de 1,35x num close.
- Texto: `HL_STYLE=nativo` (TikTok Sans 700 pequeno, contorno + halo), frase de gíria sem preço.
- Duração livre (10–15 s).

### 2. Estilo Original (o dos vídeos do Lucas que bombaram)
O formato das 2 únicas postagens acima de 1.000 views (jaqueta 1.204, camisa do Brasil 1.831), feitas pelo Lucas no Flow + CapCut.
- Cenário: cama com lençol amassado, luz laranja (esquerda) e azul (direita), mais lilás/apagado que o Lucena, câmera um pouco mais longe.
- Abre JÁ com o pacote preto nas mãos sendo rasgado no 0,0 s; o produto aparece em ~1,5–2 s.
- Texto: legenda nativa pequena do TikTok no topo ("Essa jaqueta dry-fit é outro nível 🤯"), posta no app. `HL_STYLE=nativo` com `HL_Y_NATIVO=0.07` é o mais próximo.
- Cortes feitos à mão, "com malícia": tirar o segundinho que fica feio entre as ações.
- 12 s, sem narração.

### 3. Estilo Headline (testado, fraco até agora)
O que eu fiz nos primeiros vídeos com IA: headline grande Arial Black com contorno (`HL_STYLE=grande`), 1.6x, pacote ou colocar na cama.
Até 20/10: 101–296 views em 6 vídeos. Manter só como controle de teste.

### 4. Estilo Narração
Estrutura de vídeo viral + narração edge-tts + legenda palavra por palavra. Até 20/10: 242 e 296 views.

## Catálogo de takes (blocos combináveis)
| id | Take | Gera como | Bom para |
|---|---|---|---|
| T1 | **Unboxing**: rasga o pacote preto e tira as peças | Frames: início = pacote nas mãos, fim = peças na cama | Gancho; os 2 vídeos que bombaram abrem assim |
| T2 | **Jogar na cama**: joga uma peça, depois a outra por cima | Frames: início = cama vazia, fim = peças na cama | Gancho dinâmico (Lucena) |
| T3 | **Esticada longa** pela barra, rente à cama | Animar a imagem das peças | Tecido elástico, dry fit, compressão |
| T4 | **Vai e volta**: levanta um pouco e estica/solta 4–5x, moderado | Animar | Elasticidade sem parecer que vai rasgar |
| T5 | **Levantar perto da câmera** e mostrar o peito/estampa | Animar | Estampa forte, logo |
| T6 | **Palma na estampa** + zoom 1,35x na edição | Animar (o mesmo take do T3 serve) | Logo, estampa, textura |
| T7 | **Zíper**: abre/fecha o zíper | Animar; prompt diz quantos zíperes, lado, cor, comprimento ("about one hand long") | Peça com zíper (jaqueta, meia-zíper, bolso) |
| T8 | **Tirar da cama**: uma peça de cada vez, fecha na cama vazia | Frames: início = peças, fim = cama vazia | Final |
| T9 | **Tapar a câmera** com a palma | Animar (card 8) | Transição / final alternativo |
| T10 | **Tecido de perto**: leva a peça à câmera e passa os dedos | Animar (card 15) | Tecido premium |

## Estilo de corte (regra do Lucas, 2026-10-23 — vale para TODOS os estilos)
Medido no vídeo da jaqueta que vendeu (12,2 s): só **4 trechos longos**, cada ação completa antes de trocar:
abrir pacote 2,4 s → deitar + alisar + esticar de leve 5,8 s (sem corte no meio) → aproximar da câmera e esfregar o tecido 2,9 s → tirar 1,1 s.
- Trechos de **2,5–6 s**. Nunca cortar uma ação no meio; corte só ENTRE ações. Trecho de 1 s só no final.
- O close na logo/tecido precisa de tempo (≥ 2,5 s) para dar pra ver a mão passando.
- Jogar na cama: se o vídeo tem 2 peças, **jogar as duas juntas** num movimento só (nunca uma e depois a outra).
- Sempre ter a **esticadinha de vai e volta** (T4) e o **aproximar da câmera + passar a mão no tecido** (T10).
- Revisão: olhar o take de tirar/jogar a **6 fps**; deformação de peça (derreter, torcer) reprova o take, não dá pra deixar passar.
- Legenda: variar a frase a cada vídeo (banco abaixo); não repetir a do vídeo base.

## Banco de legendas (tom de amigo, sem preço; girar)
"Irmão essa aqui é braba demais" · "Essa aqui é padrão ein" · "Essa tá padrão demais e no precinho de amigo" · "Essa aqui merece um lugar no teu guarda roupa" · "Irmão essa aqui é selecionada" · "Olha o nível dessa aqui irmão" · "Essa não sai do meu corpo" · "Treino, rolê, trabalho… essa vai em tudo" · "Tecido gelado que não marca suor" · "Essa aqui chegou e eu já pedi outra" · "Quem viu essa aqui não esquece" · "Tá ligado na qualidade dessa?"

## Como escolher os takes (raciocínio a cada produto)
- Tecido elástico (dry fit, compressão, legging, poliamida) → T3 ou T4.
- Estampa/logo forte → T5 + T6.
- Tem zíper → testar T7.
- Kit com várias cores → T1 (unboxing tirando uma por uma) ou T2.
- Sempre: gancho com o produto visível e mão mexendo até 1,5 s; final T8 ou T9.
- **A cada vídeo, mudar UMA coisa** em relação ao último (o gancho, ou um take, ou o estilo) e registrar no diário abaixo. Propor ao Lucas a variação com o motivo ("esse é dry fit, vou testar abrir com T4 em vez de T1"); quando ele não escolher, decidir e seguir.

## Diário de testes (atualizar a cada postagem; métricas do TikTok Studio em 48 h e 7 dias)
| Data/hora postagem | Vídeo | Estilo | Takes (ordem) | Texto | Views | Médio | Completo |
|---|---|---|---|---|---|---|---|
| 13/10 23:58 | Jaqueta dry fit (Lucas) | Original | T1 → T3 → T10 → T8 | nativo topo | 1.204 | 3,04 s | 4,4% |
| 14/10 01:30 | Camisa do Brasil (Lucas) | Original | T1 → T5 → T6 | nativo topo | 1.831 | 3,39 s | 4,8% |
| 15/10 23:41 | Calça poliamida | Headline | colocar → T3 → T10 → T8 | grande | 182 | 3,22 s | 2,6% |
| 19/10 20:45 | Camiseta dry fit | Narração | T6 → T5 → T6 → CTA | grande + legenda | 242 | 1,75 s | 0,6% |
| 19/10 22:01 | Jaqueta v3 | Narração | T1 → T3 → T5 → T10 → T8 | grande + legenda | 296 | 3,33 s | 4,0% |
| 20/10 07:51 | Calça (nova) | Headline | T1 → T3 → T6 | grande | 110 | 2,31 s | 1,2% |
| 20/10 07:53 | Camiseta oversized | Headline | T1 → T10 → T6 | grande | 101 | 1,56 s | 1,1% |
| 20/10 07:56 | Camisa compressão v2 | Headline | T1 → T2 → T3 → T10 → T8 | grande | 159 | 2,39 s | 2,9% |
| (a postar) | Camisa compressão d4 | Lucena | T2 → T3 → T4 → T6 → T8 | nativo | | | |
| (a postar) | Camiseta CAC zíper v2 (3 legendas) | Lucena + corte do Lucas | jogar as 2 → T4 → T7 zíper → T10 perto+logo → T8 (5 trechos de 2,5–4,5 s, 1.25x) | nativo, 3 frases | | | |

### O que os dados dizem até agora (20/10)
- Os 2 únicos acima de 1.000 views: estilo Original, **texto nativo pequeno** e postados de madrugada (23:58 e 01:30).
- Todos com **headline grande** ficaram entre 101 e 296 views.
- A jaqueta v3 com narração teve retenção igual à dos vencedores (3,33 s, 4%) e mesmo assim só 296 views: retenção sozinha não explica.
- Os 3 de 20/10 saíram com 5 minutos de diferença entre eles, às 7h50: provavelmente competiram entre si.
- **Amostra pequena: são hipóteses, não conclusão.** Próximos testes, um de cada vez: postar no horário dos vencedores (23h–1h), espaçar 3 h ou mais entre posts, e o estilo Lucena (texto nativo) contra o Original.
