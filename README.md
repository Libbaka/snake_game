Prompt 1:
Napiš Python kód pro hru Snake využívající knihovnu Pygame. Hra by měla mít následující vlastnosti:
1. Had se pohybuje po herním poli.
2. Had roste o jednu kostku po snědení jídla.
3. Hra končí, pokud had narazí do svého vlastního těla.
4. Po skončení hry se zobrazí zpráva "Game Over" a hra se po 2 sekundách ukončí.
Použij standardní knihovnu Pygame pro vykreslování a detekci událostí.

Prompt 2:
Uprav následující Python kód pro hru Snake, aby:
1. Had rostal o jednu kostku po snědení jídla.
2. Hra končila pouze tehdy, když had narazí do svého vlastního těla. 
Jídlo by mělo být generováno na celočíselných pozicích mřížky.

Prompt 3:
Dokonči a otestuj následující Python kód pro hru Had Snake v Pygame. Ujisti se, že:
1. Had roste o jednu kostku po snědení jídla.
2. Hra končí při nárazu hada na jeho vlastní tělo.
3. Zobrazí se zpráva "Game Over" po skončení hry a hra se po 2 sekundách ukončí.


LLM:

Prompt 1: 
Napište kód pro hru Snake v Pythonu s použitím knihovny Pygame. Hra by měla mít následující prvky:
- Hlavní herní smyčka, která zajišťuje pohyb hada a aktualizaci herního stavu.
- Funkci pro vykreslení hada a jídla.
- Funkci pro zpracování kolizí a konce hry.
- Funkci, která simuluje rozhodování LLM pro pohyb hada (například náhodný výběr mezi 'LEFT', 'RIGHT', 'UP', 'DOWN').

Kód by měl obsahovat inicializaci Pygame, nastavení obrazovky a herní smyčku, která aktualizuje pozici hada na základě rozhodnutí LLM a kontroluje kolize.

Prompt 2:
Vytvořte návod, jak použít LLM pro řízení hry Snake. Vysvětlete, jak LLM může být integrováno do hry, aby rozhodovalo o pohybu hada na základě aktuálního herního stavu. Návod by měl zahrnovat:
- Popis, jak LLM může generovat tahy hada na základě informace o pozici hada, jídla a stavu hry.
- Jak integrovat rozhodování LLM do herní smyčky.
- Jaké vstupy LLM potřebuje a jaké výstupy generuje.
- Příklady použití LLM pro simulaci rozhodování o pohybu hada (například pomocí náhodného výběru mezi směry).
