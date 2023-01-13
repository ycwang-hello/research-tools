# Obsidian

Though its markdown editing is not as sophisticated as Typora, we can make it better with some community plugins.

## Community Plugins

### Latex Suite
By [artisticat1](https://github.com/artisticat1) ([GitHub page](https://github.com/artisticat1/obsidian-latex-suite))

We can freely define auto-close, auto-correct with its Snippets. I also find its inline math preview helpful.

#### Snippets

Snippets can be used to automatically close symbols for ~~strikethrough~~ (`~~strikethrough~~`), ==highlight== (`==highlight==`) and `%%comment%%`, which are not autoclosed in Obsidian. I define these snippets:

```ts
{trigger: "==", replacement: "==$0==$1", options: "tAw", description: "highlight"}, 
{trigger: "%%", replacement: "%%$0%%$1", options: "tAw", description: "comment"}, 
{trigger: "~~", replacement: "~~$0~~$1", options: "tAw", description: "strikethrough"},
{trigger: "\\u{", replacement: "<u>$0</u>$1", options: "tAw", description: "underline"},
```

I use these snippests to trigger inline math, displayed math and LaTeX environments, rather than the default ones, which trigger from combination of letters:
```ts
{trigger: "\\(", replacement: "$$0$", options: "tA"},
{trigger: "\\[", replacement: "$$\n$0\n$$", options: "tAw"},
{trigger: "\\begin{", replacement: "\\begin{$0}\n$1\n\\end{$0}$2", options: "mA"},
```

I do not like triggering replacements with certain combinations of lettters, nor do I like triggering it with Tab. I would like an experience of calling LaTeX commands. With the below snippet, we can, e.g., type `\red{` + `text` + Tab to get red <font color='red'>text</font> (`<font color='red'>text</font>`).
```ts
// colors in text
{trigger: "\\red{", replacement: "<font color='red'>$0</font>$1", options: "tAw", description: "red"},
{trigger: "\\blue{", replacement: "<font color='blue'>$0</font>$1", options: "tAw", description: "blue"},
{trigger: "\\color{", replacement: "<font color='$0'>$1</font>$2", options: "tAw", description: "text color"},

// colors in math
{trigger: "\\red{", replacement: "\\textcolor{red}{$0}", options: "mA", description: "red"},
{trigger: "\\blue{", replacement: "\\textcolor{blue}{$0}", options: "mA", description: "blue"},
{trigger: "\\color{", replacement: "\\textcolor{$0}{$1}", options: "mA", description: "color"},
```
Looks nice!

The default snippet defined by the Latex Suite authors serves as a good example of how we can implement AutoCorrect supported in MS Word:
```ts
// Dashes
{trigger: "--", replacement: "–", options: "tA"},
{trigger: "–-", replacement: "—", options: "tA"},
{trigger: "—-", replacement: "---", options: "tA"},
```
Let's implement this:
```ts
{trigger: "...", replacement: "…", options: "tA"},
```

We can press Ctrl+Z to cancel the replacement.

For autoclose of math `$$` and `$$$$`, I think the plugin called "Quick Latex for Obsidian" works better.

### Quick Latex for Obsidian
By [joeyuping](https://github.com/joeyuping) ([GitHub page](https://github.com/joeyuping/quick_latex_obsidian)) 

### Underline
By [Benature](https://github.com/Benature) ([GitHub page](https://github.com/Benature/obsidian-underline))

This makes it simpler to add <u>underline</u> (`<u>underline</u>`) to the text. 

### Advanced Tables for Obsidian
By Tony Grosinger [@tgrosinger](https://github.com/tgrosinger) ([GitHub page](https://github.com/tgrosinger/advanced-tables-obsidian))

Makes it easier to deal with tables (though still not as sophisticated as Typora).
