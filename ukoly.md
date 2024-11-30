# ÚKOL 1

Vytvořte adresář s názvem 'project' a:
vstupte do adresáře a vytvořte tři prázdné textové soubory: file1, file2, file3.
otevřete každý soubor postupně pomocí textového editoru (Vim nebo Nano),
zadejte nějaký text a uložte jej do souboru
zobrazte obsah každého souboru příkazem cat.
```bash
mkdir project
```

# ÚKOL 3
Zobrazte obsah libovolného adresáře, a to rekurzivně. Zobrazte také podrobnosti o souborech a jejich velikosti v megabajtech.
```bash
ls -R 
```


ÚKOL 4
Vytvořte následující strom adresářů:

├── America
│ ├── Canada
│ ├── Mexico
│ ├── USA
│ │ ├── Chicago
│ │ ├── Dallas
│ │ ├── Miami

```bash
mkdir America
mkdir America/Canada
mkdir America/Mexico
mkdir America/USA
mkdir America/USA/Chicago
mkdir America/USA/Dallas
mkdir America/USA/Miami
```

ÚKOL 4.1
Zobrazte rekurzivně obsah adresáře America pro ověření hierarchie.