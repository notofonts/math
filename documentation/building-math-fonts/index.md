# Building OpenType math fonts
Math typesetting is different than regular text typesetting because math formulas are arranged in two dimensions, and there is an interaction between symbols of different styles and sizes. Because of that, math fonts have always been a special kind of fonts. One of, or probably the most, famous math typesetting engines is TeX, and its math fonts required a complex setup of various fonts (for upright, italic, regular, bold, symbols, etc) and special metrics, and font parameters. When OpenType started supporting math typesetting, it built on TeX experience, but upgraded to Unicode and OpenType (TeX predates both).

Instead of multiple fonts, all symbols are contained in a single font, and the various “font styles” use the dedicated Unicode math alphanumerics, and the additional glyphs (super/sub scripts, glyph in multiple sizes, and so one) are included in the same font as variants of the base glyphs. OpenType introduced a new `MATH` table that includes various special math parameters (constants) and metrics, as well as a few registered feature tags for math-specific glyphs substitutions (more about both below).

## Character set
Math fonts require quite a few glyphs (ranges from about 1000 to 6000 glyphs), based on what character set is supported by the font. There is no single, well defined character set for math fonts, Unicode includes thousands of math related characters, so each project defines its own character set based on its own requirements. Here are some of the Unicode blocks related to mathematics:

### Alphanumerics
* Basic Latin (ASCII), [U+0000–007F](https://unicode.org/charts/PDF/U0000.pdf): This includes the upright regular basic Latin character as well as upright digits. It also includes some basic operators and punctuation used in math (e.g. plus and brackets).
* Greek, [U+0370–03FF](https://unicode.org/charts/PDF/U0370.pdf): This includes upright regular Greek characters. The accented, archaic, and coptic-derived characters are not usually used in math, so can be skipped. The variant letter forms, like Greek Phi Symbol (U+03D5) are often used in math in should be included.
* Mathematical Alphanumeric Symbols, [U+1D400–1D7FF](https://unicode.org/charts/PDF/U1D400.pdf): This is a quite large block (around 1000 characters), as it includes the following styles:
  * Latin
    * upright bold
    * italic regular
    * italic bold
    * script regular
    * script bold
    * fraktur regular
    * fraktur bold
    * double-struck regular
    * double-struck bold
    * sans-serif upright regular
    * sans-serif upright bold
    * sans-serif italic regular
    * sans-serif italic bold
    * monospace upright regular
  * Greek
    * upright bold
    * italic regular
    * italic bold
    * sans-serif upright bold
    * sans-serif italic bold
  * Digits:
    * bold
    * double-struck regular
    * sans-serif regular
    * sans-serif bold
    * monospace regular
    
  Some of the styles in this block are missing a few characters, because they were already defined in Unicode in a different block.
* Letterlike Symbols, [U+2100–214F](https://unicode.org/charts/PDF/U2100.pdf): This includes some symbols that can be used in math, and specially some alphanumeric symbols missing from the previous block (e.g. U+210E is used for Latin italic h, which is not included with the other Latin italic letters in the above block).
* Arabic, [U+0600–06FF](https://unicode.org/charts/PDF/U0600.pdf): For Arabic math support, the Arabic-Indic and Extended Arabic-Indic digits need to be included as well as basic Arabic letters (in isolated form only).
* Arabic Mathematical Alphabetic Symbols, [U+1EE00–1EEFF](https://unicode.org/charts/PDF/U1EE00.pdf): This includes Arabic math letters, in isolated, initial, extended, tailed, looped, and double-struck forms (the design of isolated forms for math symbols sometimes differs from the basic isolated forms, so both should be included in fonts intended to support Arabic math).

### Symbols
* Latin-1 Supplement, [U+0080–00FF](https://unicode.org/charts/PDF/U0080.pdf): Includes some operators like multiplication and division.
* Mathematical Operators, [U+2200–22FF](https://unicode.org/charts/PDF/U2200.pdf): Includes a large set of most commonly used math operators.
* Supplemental Mathematical Operators, [U+2A00–2AFF](https://unicode.org/charts/PDF/U2A00.pdf): More commonly used operators.
* Miscellaneous Mathematical Symbols-A, [U+27C0–27EF](https://unicode.org/charts/PDF/U27C0.pdf)
* Miscellaneous Mathematical Symbols-B, [U+2980–29FF](https://unicode.org/charts/PDF/U2980.pdf)
* Miscellaneous Technical, [U+2300–23FF](https://unicode.org/charts/PDF/U2300.pdf): Includes some common math symbols, plus a few legacy ones (like U+23B2 Summation Top).
* General Punctuation, [U+2000–206F](https://unicode.org/charts/PDF/U2000.pdf): Invisible operators and some other symbols.
* Arrows, [U+2190–21FF](https://unicode.org/charts/PDF/U2190.pdf)
* ...

## OpenType features
Math fonts use several OpenType features for proper math layout, although none of these features is strictly required, they are crucial for fine mathematical typography.

### Math script style alternates (`ssty`)
Math often includes glyphs at smaller point sizes (like super scripts, sub scripts, fraction numerators and denominators, and so one). For proper typography these glyphs need to be optically adjusted for the smaller point sizes. In OpenType math this is handled by including two sets of glyphs designed for the first and second level scripts (further levels use the glyphs of the second level) and mapping them using the `ssty` features as multiple alternates substitution. The glyphs should be designed in full size and not moved vertically (unlike `sups` and `subs` features) since the scaling and positioning will be done by the math layout engine (the scaling percent is controlled by two font constants, discussed below).

The lookup should be an alternate substitution lookup with two alternate glyphs for each base glyph, e.g.:
```fea
sub a from [a.ssty1 a.ssty2];
sub b from [b.ssty1 b.ssty2];
```

If only one alternate is provided, a single substitution can be used, e.g.:
```fea
sub a by a.ssty1;
sub b by b.ssty1;
```

Though some math layout engines might revert back to the base glyph for second level scripts when a single substitution is used, and because of that it is preferable to always use multiple alternates with two alternates even if there is actually one alternate glyph (i.e. by repeating the first glyph):
```fea
sub a from [a.ssty a.ssty];
sub b from [b.ssty b.ssty];
```

#### Primes
Prime characters are an interesting case for `ssty` feature. In most fonts the prime are designed as raised apostrophe-like glyphs, but in TeX prime was designed as a full sized glyph that sets near baseline and the math input treats it as a superscript that then gets scaled and moved vertically like any other superscript. OpenType math inherits this, so if the font designed prime as usual in text fonts, the layout engine will further scale it down and raise it up, making it look smaller and higher than expected. There are two ways to fix this:
1. Design the prime glyph like TeX fonts do, but then when prime is used outside math engine it will look wrong.
2. Design the base prime glyph as normal, and provide and alternate glyph that is design like TeX fonts to be activated with the `ssty` feature. This way prime looks good when used in text and math.

This should apply to all prime characters in Unicode, namely: U+2032, U+2033, U+2034, U+2035, U+2036, U+2037, and U+2057.

### Flattened ascent forms (`flac`)
Some times accents over capitals are reduced in height to reduce the height of accented glyphs. In math the pre-composed accented glyphs are not used and accents are placed by the math layout engine (controlled by several constants discussed below). This feature allows providing an alternate set of accents to be used over capital glyphs (actually over any glyphs higher than a constant define by the font). It should use a single substitution lookup:
```fea
sub actutecomb by actutecomb.flac;
```

### Dotless forms (`dtls`)
Sometimes “i” and “j” glyphs loose their dot (title) when an accent is placed over them, e.g. $\hat{\imath}\ \hat{\jmath}$. This feature is used to substitute them with dotless alternate glyphs. It should use a single substitution lookup:
```fea
sub i by idotless;
sub iitalic-math by iitalic-math.dotless;
```

## The `MATH` table
OpenType math fonts has a dedicated table that contains math typesetting-related data. This table contains various font wide math typesetting parameters,, as well as glyph level math-related metrics and data. OpenType math layout engines consult this table when building-up math equations. Some aspects of this table might seem redundant, e.g. in provides it was of positioning accents over base glyphs, which is usually done using `GPOS` table for text fonts, but math accent positioning can involve more complex cases than what can be handled by GPOS table (like accents over multiple letters; $\widehat{abc}$) so `GPOS` table is not used in math layout and `MATH` table is used instead (some implementations might apply `GPOS` kerning, but most don’t).

Editing `MATH` table can be cumbersome since few tools support it. Currently the tools available for editing `MATH` table are FontForge, [Glyphs MATH Plugin](https://github.com/Nagwa-Limited-Community/Glyphs-MATH-Plugin), and FontTools Python Library. There was also a tool from Microsoft, but it does not seem to be publicly available anymore.

The general idea is the same, so the examples here will use Glyphs with the MATH plugin, but it should be applicable to any other tool with the necessary modifications.

Math table can roughly be divided into font-wide parameters (constants) and glyph-level data.

### Constants
Constants are font-wide data that control various aspects of math typesetting.

#### `scriptPercentScaleDown`, `scriptScriptPercentScaleDown`
This is the percent by which first and second level super/sub scripts will be scaled. The spec recommends 80% for `scriptPercentScaleDown` and 60% for `scriptScriptPercentScaleDown`, but this is too big when optically sized alternates are provided (the `ssty` feature), a better value is probably between 60-70% for the `scriptPercentScaleDown` and around 50% for `scriptScriptPercentScaleDown`.

For comparison, TeX’s default setup uses 10pt for base font size, and 7pt for first level scripts, and 5pt for the second level (TeX’s default fonts are optically adjusted to the point size they are used for). This constant should be taken into account when designing the `ssty` variants, i.e. 70% means you are designing for 7pt optical size, and so on.

#### `delimitedSubFormulaMinHeight`
Nobody knows what this constant is for, except that Microsoft’s math layout engine [mistakenly uses it instead of the next constant](https://github.com/MicrosoftDocs/typography-issues/issues/1136), so in reality it needs to be set to whatever value `displayOperatorMinHeight` is set to.

#### `displayOperatorMinHeight`
Math layout engine use bigger glyph for _big_ operators (e.g. integral or summation) when math equations are in display mode (standalone between paragraphs, as opposed of being inline with the regular text). Compare inline $\sum a \prod b \int c$ with display:

$$\sum a \prod b \int c$$

This means at least two glyphs are needed for each big operator, one for text math and the other for display math. It is possible to have more than one glyph, and this constant tells the layout engine what is the minimum size (bounding box height) of the big operator in display style, to skip any glyph that is smaller than it. Even if the font has only two glyphs for each big operator, this constant should be set to a value larger than the size of the first glyph of **all** big operator. There is a catch, however, since Microsoft implementation has a bug where it reads `delimitedSubFormulaMinHeight` instead of this constants, so the value that should be set for `displayOperatorMinHeight`, should also be used for `delimitedSubFormulaMinHeight` so that the font behaves correctly in various implementations.

#### `mathLeading`
No one also knows what this constant is used for, or how to test it, so read the spec description and make up your mind.

#### `axisHeight`
This is a very important constant. In math layout, big operators, fractions, and many other constructs with large vertical size are vertically centered. They are centered around the value of this constant, so it should be the vertical center of the small operators (minus, plus, equal, less than, bigger than, etc). The simplest way to calculate its value is to use the vertical center of the minus glyph, and then make sure all small operators are centered around it (well, not all of them, most of them, some glyphs look better when they set on the base line, so use your judgment and check other math fonts).

#### `accentBaseHeight`
As discussed above, the math layout engine does not use `GPOS` table for positioning anchors. It instead uses data from the `MATH` table, and this constant is one of them. By default the accent will not be shifted vertically unless the height of the glyph exceeds this constant. This is meant so that accents over glyphs without ascenders are kept in their default position, so it should be set to x-height + overshot.

#### `flattenedAccentBaseHeight`
The `flac` feature will be applied to accents over glyphs higher than this constant, so it should be set to cap-height.

#### `subscriptShiftDown`, `subscriptTopMax`, `subscriptBaselineDropMin`
Positioning sub/superscripts in math is a bit involved, as there can be complex structures there, not only numbers or letters.

* First, the baseline of the subscript is shifted by `subscriptShiftDown` value (usually a negative value, since we want to shift down). If your font has `subs` feature, this would be how much the subscript glyphs go down below the baseline, or if your font has a carefully set `OS/2.ySubscriptYOffset`, it would be the same value (most font editors autogenerate `OS/2.ySubscriptYOffset` when not explicitly set, the autogenerated value may or may not be sensible, test it and use your judgment). Test equation $a_a$.
* If the subscript is not a single character, however, the above constant is not used and the subscript baseline is instead shifted below the bottom of the base by `subscriptBaselineDropMin`. Test equation $a_{abc}$.
* Then it measures the top of the subscript (after shifting it down), and if it is higher than `subscriptTopMax`, it will be shifted down so that its height does not exceed it. This way the subscript cant’t get too high to be confusing. The suggested value for this constant is 4⁄5 x-height. Test equation $a_{a\frac{b}{c})}$.

#### `superscriptShiftUp`, `superscriptShiftUpCramped`, `superscriptBottomMin`, `superscriptBaselineDropMax`
Similarly, positioning superscripts uses a bunch of constants:

* First, the baseline of the superscript is shifted by `superscriptShiftUp` (usually a positive value since we want to shift up). If your font has a `sups` feature, this would be how much the superscript glyphs go up above the baseline, or if your font has a carefully set `OS/2.ySuperscriptYOffset` , it would be the same value. Test equation $a^a$.
* When the superscript is in some place where too much vertical shift is undesired (because it will make the formula too high), the layout engine uses `superscriptShiftUpCramped` instead (*cramped* constants are used in cramped places). It should be slightly less than `superscriptShiftUp`, may be 70–80% of it. Test equation $\frac{a^a}{a^a}$.
* If the superscript is not a single character, however, the above two constants are not used and the superscipt baseline is instead shifted above the top of the base by `superscriptBaselineDropMax`. Test equation $a^{abc}$.
* Then if the distance between the baseline of base and the bottom of the superscripts is less than `superscriptBottomMin`, the superscript gets shifted up so that the distance equals it. This way the superscript cant’t get too low to be confusing. The suggested value for this constant is 1⁄4 x-height. Test equation $a^{a\frac{b}{\sqrt{c}})}$.

### Glyph data

#### Italic correction

#### Accent positioning

#### Math kerning

#### Extended shapes

#### Size variants

##### Extensibles

## Building

## Testing
