# Pygame Platformová Hra

## Úvod
Toto je jednoduchá platformová hra vyvinutá pomocí knihovny Pygame v Pythonu. Hráč ovládá postavu, která se pohybuje přes různé úrovně, sbírá body a vyhýbá se překážkám. Hra obsahuje několik úrovní, bodovací systém.

## Požadavky
K provozování této hry potřebujete mít nainstalovaný Python a Pygame. 

## Herní Soubory
- `main.py`: Hlavní herní soubor obsahující veškerou herní logiku.
- `assets/character.png`: skin postavy použité ve hře.

## Jak Hrát
1. Spusťte skript `main.py` pro zahájení hry.
2. Budete přesměrováni na úvodní obrazovku. Klikněte na tlačítko "Hrát" pro zahájení hry.
3. Použijte následující ovládací prvky pro hraní hry:
    - `A`: Pohyb vlevo
    - `D`: Pohyb vpravo
    - `SPACE`: Skok
4. Sbírejte body (označené světle zeleně) a vyhýbejte se tmavě zeleným překážkám.
5. Dostaňte se na pravý okraj obrazovky pro postup do další úrovně.
6. Pokud se dotknete tmavě zelené překážky, prohráváte a herní stav se změní na "prohra".
7. Pokud nasbíráte všechny body ve všech úrovních a dostanete se na konec, vyhráváte hru.

## Přehled Kódu
- **Inicializace**: Hra inicializuje Pygame, obrazovku a UI prvky.
- **Herní Smyčka**: Hlavní smyčka hry, která zpracovává události, aktualizuje herní stav a vykresluje hru.
- **Kreslící Funkce**: Funkce pro kreslení mřížky (draw_grid), čtverců (draw_square) a postavy (draw_player) na obrazovce.
- **Aktualizace Hráče**: Zpracovává pohyb hráče, detekci kolizí a herní logiku.
  
Užijte si hru!
