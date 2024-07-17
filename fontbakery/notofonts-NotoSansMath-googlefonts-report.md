## FontBakery report

fontbakery version: 0.12.8



## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[2] NotoSansMath-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'smcp' or 'liga' lookups not found in GSUB table.</p>
 [code: missing-lookups]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/NotoSansMath/googlefonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[13] NotoSansMath-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+00C5: LATIN CAPITAL LETTER A WITH RING ABOVE</td>
<td align="left">U+00E5: LATIN SMALL LETTER A WITH RING ABOVE</td>
</tr>
<tr>
<td align="left">U+0190: LATIN CAPITAL LETTER OPEN E</td>
<td align="left">U+025B: LATIN SMALL LETTER OPEN E</td>
</tr>
<tr>
<td align="left">U+01B5: LATIN CAPITAL LETTER Z WITH STROKE</td>
<td align="left">U+01B6: LATIN SMALL LETTER Z WITH STROKE</td>
</tr>
<tr>
<td align="left">U+212B: ANGSTROM SIGN</td>
<td align="left">U+00E5: LATIN SMALL LETTER A WITH RING ABOVE</td>
</tr>
<tr>
<td align="left">U+2132: TURNED CAPITAL F</td>
<td align="left">U+214E: TURNED SMALL F</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>No GF glyphset was found to be supported &gt;80%, so language shaping support couldn't get checked.</p>
 [code: no-glyphset-supported]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>This is a Noto font but it lacks an ARTICLE.en_us.html file.</p>
 [code: missing-article]



* 🔥 **FAIL** <p>This is a Noto font but it lacks a DESCRIPTION.en_us.html file.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x00A1 (INVERTED EXCLAMATION MARK)


- 0x00A8 (DIAERESIS)


- 0x00AA (FEMININE ORDINAL INDICATOR)


- 0x00AB (LEFT-POINTING DOUBLE ANGLE QUOTATION MARK)


- 0x00AF (MACRON)


- 0x00B4 (ACUTE ACCENT)


- 0x00BA (MASCULINE ORDINAL INDICATOR)


- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)


- 0x00BF (INVERTED QUESTION MARK)


- 0x00C0 (LATIN CAPITAL LETTER A WITH GRAVE)


- 0x00C1 (LATIN CAPITAL LETTER A WITH ACUTE)


- 0x00C2 (LATIN CAPITAL LETTER A WITH CIRCUMFLEX)


- 0x00C3 (LATIN CAPITAL LETTER A WITH TILDE)


- 0x00C4 (LATIN CAPITAL LETTER A WITH DIAERESIS)


- 0x00C6 (LATIN CAPITAL LETTER AE)


- 0x00C8 (LATIN CAPITAL LETTER E WITH GRAVE)


- 0x00C9 (LATIN CAPITAL LETTER E WITH ACUTE)


- 0x00CA (LATIN CAPITAL LETTER E WITH CIRCUMFLEX)


- 0x00CB (LATIN CAPITAL LETTER E WITH DIAERESIS)


- 0x00CC (LATIN CAPITAL LETTER I WITH GRAVE)


- 0x00CD (LATIN CAPITAL LETTER I WITH ACUTE)


- 0x00CE (LATIN CAPITAL LETTER I WITH CIRCUMFLEX)


- 0x00CF (LATIN CAPITAL LETTER I WITH DIAERESIS)


- 0x00D1 (LATIN CAPITAL LETTER N WITH TILDE)


- 0x00D2 (LATIN CAPITAL LETTER O WITH GRAVE)


- 0x00D3 (LATIN CAPITAL LETTER O WITH ACUTE)


- 0x00D4 (LATIN CAPITAL LETTER O WITH CIRCUMFLEX)


- 0x00D5 (LATIN CAPITAL LETTER O WITH TILDE)


- 0x00D6 (LATIN CAPITAL LETTER O WITH DIAERESIS)


- 0x00D8 (LATIN CAPITAL LETTER O WITH STROKE)


- 0x00D9 (LATIN CAPITAL LETTER U WITH GRAVE)


- 0x00DA (LATIN CAPITAL LETTER U WITH ACUTE)


- 0x00DB (LATIN CAPITAL LETTER U WITH CIRCUMFLEX)


- 0x00DC (LATIN CAPITAL LETTER U WITH DIAERESIS)


- 0x00DD (LATIN CAPITAL LETTER Y WITH ACUTE)


- 0x00DF (LATIN SMALL LETTER SHARP S)


- 0x00E0 (LATIN SMALL LETTER A WITH GRAVE)


- 0x00E1 (LATIN SMALL LETTER A WITH ACUTE)


- 0x00E2 (LATIN SMALL LETTER A WITH CIRCUMFLEX)


- 0x00E3 (LATIN SMALL LETTER A WITH TILDE)


- 0x00E4 (LATIN SMALL LETTER A WITH DIAERESIS)


- 0x00E5 (LATIN SMALL LETTER A WITH RING ABOVE)


- 0x00E6 (LATIN SMALL LETTER AE)


- 0x00E8 (LATIN SMALL LETTER E WITH GRAVE)


- 0x00E9 (LATIN SMALL LETTER E WITH ACUTE)


- 0x00EA (LATIN SMALL LETTER E WITH CIRCUMFLEX)


- 0x00EB (LATIN SMALL LETTER E WITH DIAERESIS)


- 0x00EC (LATIN SMALL LETTER I WITH GRAVE)


- 0x00ED (LATIN SMALL LETTER I WITH ACUTE)


- 0x00EE (LATIN SMALL LETTER I WITH CIRCUMFLEX)


- 0x00EF (LATIN SMALL LETTER I WITH DIAERESIS)


- 0x00F1 (LATIN SMALL LETTER N WITH TILDE)


- 0x00F2 (LATIN SMALL LETTER O WITH GRAVE)


- 0x00F3 (LATIN SMALL LETTER O WITH ACUTE)


- 0x00F4 (LATIN SMALL LETTER O WITH CIRCUMFLEX)


- 0x00F5 (LATIN SMALL LETTER O WITH TILDE)


- 0x00F6 (LATIN SMALL LETTER O WITH DIAERESIS)


- 0x00F8 (LATIN SMALL LETTER O WITH STROKE)


- 0x00F9 (LATIN SMALL LETTER U WITH GRAVE)


- 0x00FA (LATIN SMALL LETTER U WITH ACUTE)


- 0x00FB (LATIN SMALL LETTER U WITH CIRCUMFLEX)


- 0x00FC (LATIN SMALL LETTER U WITH DIAERESIS)


- 0x00FD (LATIN SMALL LETTER Y WITH ACUTE)


- 0x00FF (LATIN SMALL LETTER Y WITH DIAERESIS)


- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


- 0x0101 (LATIN SMALL LETTER A WITH MACRON)


- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


- 0x0103 (LATIN SMALL LETTER A WITH BREVE)


- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


- 0x0105 (LATIN SMALL LETTER A WITH OGONEK)


- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)


- 0x0107 (LATIN SMALL LETTER C WITH ACUTE)


- 0x010A (LATIN CAPITAL LETTER C WITH DOT ABOVE)


- 0x010B (LATIN SMALL LETTER C WITH DOT ABOVE)


- 0x010C (LATIN CAPITAL LETTER C WITH CARON)


- 0x010D (LATIN SMALL LETTER C WITH CARON)


- 0x010E (LATIN CAPITAL LETTER D WITH CARON)


- 0x010F (LATIN SMALL LETTER D WITH CARON)


- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


- 0x0111 (LATIN SMALL LETTER D WITH STROKE)


- 0x0112 (LATIN CAPITAL LETTER E WITH MACRON)


- 0x0113 (LATIN SMALL LETTER E WITH MACRON)


- 0x0116 (LATIN CAPITAL LETTER E WITH DOT ABOVE)


- 0x0117 (LATIN SMALL LETTER E WITH DOT ABOVE)


- 0x0118 (LATIN CAPITAL LETTER E WITH OGONEK)


- 0x0119 (LATIN SMALL LETTER E WITH OGONEK)


- 0x011A (LATIN CAPITAL LETTER E WITH CARON)


- 0x011B (LATIN SMALL LETTER E WITH CARON)


- 0x011E (LATIN CAPITAL LETTER G WITH BREVE)


- 0x011F (LATIN SMALL LETTER G WITH BREVE)


- 0x0120 (LATIN CAPITAL LETTER G WITH DOT ABOVE)


- 0x0121 (LATIN SMALL LETTER G WITH DOT ABOVE)


- 0x0122 (LATIN CAPITAL LETTER G WITH CEDILLA)


- 0x0123 (LATIN SMALL LETTER G WITH CEDILLA)


- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


- 0x0127 (LATIN SMALL LETTER H WITH STROKE)


- 0x012A (LATIN CAPITAL LETTER I WITH MACRON)


- 0x012B (LATIN SMALL LETTER I WITH MACRON)


- 0x012E (LATIN CAPITAL LETTER I WITH OGONEK)


- 0x012F (LATIN SMALL LETTER I WITH OGONEK)


- 0x0130 (LATIN CAPITAL LETTER I WITH DOT ABOVE)


- 0x0136 (LATIN CAPITAL LETTER K WITH CEDILLA)


- 0x0137 (LATIN SMALL LETTER K WITH CEDILLA)


- 0x0139 (LATIN CAPITAL LETTER L WITH ACUTE)


- 0x013A (LATIN SMALL LETTER L WITH ACUTE)


- 0x013B (LATIN CAPITAL LETTER L WITH CEDILLA)


- 0x013C (LATIN SMALL LETTER L WITH CEDILLA)


- 0x013D (LATIN CAPITAL LETTER L WITH CARON)


- 0x013E (LATIN SMALL LETTER L WITH CARON)


- 0x0141 (LATIN CAPITAL LETTER L WITH STROKE)


- 0x0142 (LATIN SMALL LETTER L WITH STROKE)


- 0x0143 (LATIN CAPITAL LETTER N WITH ACUTE)


- 0x0144 (LATIN SMALL LETTER N WITH ACUTE)


- 0x0145 (LATIN CAPITAL LETTER N WITH CEDILLA)


- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)


- 0x0147 (LATIN CAPITAL LETTER N WITH CARON)


- 0x0148 (LATIN SMALL LETTER N WITH CARON)


- 0x0150 (LATIN CAPITAL LETTER O WITH DOUBLE ACUTE)


- 0x0151 (LATIN SMALL LETTER O WITH DOUBLE ACUTE)


- 0x0152 (LATIN CAPITAL LIGATURE OE)


- 0x0153 (LATIN SMALL LIGATURE OE)


- 0x0154 (LATIN CAPITAL LETTER R WITH ACUTE)


- 0x0155 (LATIN SMALL LETTER R WITH ACUTE)


- 0x0158 (LATIN CAPITAL LETTER R WITH CARON)


- 0x0159 (LATIN SMALL LETTER R WITH CARON)


- 0x015A (LATIN CAPITAL LETTER S WITH ACUTE)


- 0x015B (LATIN SMALL LETTER S WITH ACUTE)


- 0x015E (LATIN CAPITAL LETTER S WITH CEDILLA)


- 0x015F (LATIN SMALL LETTER S WITH CEDILLA)


- 0x0160 (LATIN CAPITAL LETTER S WITH CARON)


- 0x0161 (LATIN SMALL LETTER S WITH CARON)


- 0x0164 (LATIN CAPITAL LETTER T WITH CARON)


- 0x0165 (LATIN SMALL LETTER T WITH CARON)


- 0x016A (LATIN CAPITAL LETTER U WITH MACRON)


- 0x016B (LATIN SMALL LETTER U WITH MACRON)


- 0x016E (LATIN CAPITAL LETTER U WITH RING ABOVE)


- 0x016F (LATIN SMALL LETTER U WITH RING ABOVE)


- 0x0170 (LATIN CAPITAL LETTER U WITH DOUBLE ACUTE)


- 0x0171 (LATIN SMALL LETTER U WITH DOUBLE ACUTE)


- 0x0172 (LATIN CAPITAL LETTER U WITH OGONEK)


- 0x0173 (LATIN SMALL LETTER U WITH OGONEK)


- 0x0174 (LATIN CAPITAL LETTER W WITH CIRCUMFLEX)


- 0x0175 (LATIN SMALL LETTER W WITH CIRCUMFLEX)


- 0x0176 (LATIN CAPITAL LETTER Y WITH CIRCUMFLEX)


- 0x0177 (LATIN SMALL LETTER Y WITH CIRCUMFLEX)


- 0x0178 (LATIN CAPITAL LETTER Y WITH DIAERESIS)


- 0x0179 (LATIN CAPITAL LETTER Z WITH ACUTE)


- 0x017A (LATIN SMALL LETTER Z WITH ACUTE)


- 0x017B (LATIN CAPITAL LETTER Z WITH DOT ABOVE)


- 0x017C (LATIN SMALL LETTER Z WITH DOT ABOVE)


- 0x017D (LATIN CAPITAL LETTER Z WITH CARON)


- 0x017E (LATIN SMALL LETTER Z WITH CARON)


- 0x0218 (LATIN CAPITAL LETTER S WITH COMMA BELOW)


- 0x0219 (LATIN SMALL LETTER S WITH COMMA BELOW)


- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)


- 0x021B (LATIN SMALL LETTER T WITH COMMA BELOW)


- 0x02C7 (CARON)


- 0x02D8 (BREVE)


- 0x02D9 (DOT ABOVE)


- 0x02DB (OGONEK)


- 0x02DC (SMALL TILDE)


- 0x02DD (DOUBLE ACUTE ACCENT)


- 0x0328 (COMBINING OGONEK)


- 0x1E80 (LATIN CAPITAL LETTER W WITH GRAVE)


- 0x1E81 (LATIN SMALL LETTER W WITH GRAVE)


- 0x1E82 (LATIN CAPITAL LETTER W WITH ACUTE)


- 0x1E83 (LATIN SMALL LETTER W WITH ACUTE)


- 0x1E84 (LATIN CAPITAL LETTER W WITH DIAERESIS)


- 0x1E85 (LATIN SMALL LETTER W WITH DIAERESIS)


- 0x1E9E (LATIN CAPITAL LETTER SHARP S)


- 0x1EF2 (LATIN CAPITAL LETTER Y WITH GRAVE)


- 0x1EF3 (LATIN SMALL LETTER Y WITH GRAVE)


- 0x2013 (EN DASH)


- 0x201A (SINGLE LOW-9 QUOTATION MARK)


- 0x201E (DOUBLE LOW-9 QUOTATION MARK)


- 0x2039 (SINGLE LEFT-POINTING ANGLE QUOTATION MARK)


- 0x203A (SINGLE RIGHT-POINTING ANGLE QUOTATION MARK)


- 0x2122 (TRADE MARK SIGN)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni031A (U+031A), uni20DD (U+20DD), uni20DE (U+20DE), uni20DF (U+20DF) and uni20E4 (U+20E4)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: uni210A	Contours detected: 3	Expected: 2

- Glyph name: uni210D	Contours detected: 3	Expected: 2

- Glyph name: uni2119	Contours detected: 4	Expected: 2

- Glyph name: uni211A	Contours detected: 5	Expected: 3

- Glyph name: uni211D	Contours detected: 5	Expected: 3

- Glyph name: uni21A4	Contours detected: 2	Expected: 1

- Glyph name: uni21B9	Contours detected: 2	Expected: 4

- Glyph name: uni21C9	Contours detected: 2	Expected: 1

- Glyph name: uni21E0	Contours detected: 4	Expected: 3

- Glyph name: uni21E1	Contours detected: 4	Expected: 3

- Glyph name: uni21E2	Contours detected: 4	Expected: 3

- Glyph name: uni21E3	Contours detected: 4	Expected: 3

- Glyph name: uni21E4	Contours detected: 1	Expected: 2

- Glyph name: uni21E5	Contours detected: 1	Expected: 2

- Glyph name: uni2213	Contours detected: 1	Expected: 2

- Glyph name: uni2270	Contours detected: 3	Expected: 2

- Glyph name: uni2271	Contours detected: 3	Expected: 2

- Glyph name: circleplus	Contours detected: 5	Expected: 3

- Glyph name: ltshade	Contours detected: 156	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: dkshade	Contours detected: 145	Expected: 73

- Glyph name: circleplus	Contours detected: 5	Expected: 3

- Glyph name: dkshade	Contours detected: 145	Expected: 73

- Glyph name: ltshade	Contours detected: 156	Expected: 46

- Glyph name: shade	Contours detected: 78	Expected: 85

- Glyph name: uni210A	Contours detected: 3	Expected: 2

- Glyph name: uni210D	Contours detected: 3	Expected: 2

- Glyph name: uni2119	Contours detected: 4	Expected: 2

- Glyph name: uni211A	Contours detected: 5	Expected: 3

- Glyph name: uni211D	Contours detected: 5	Expected: 3

- Glyph name: uni21A4	Contours detected: 2	Expected: 1

- Glyph name: uni21B9	Contours detected: 2	Expected: 4

- Glyph name: uni21C9	Contours detected: 2	Expected: 1

- Glyph name: uni21E0	Contours detected: 4	Expected: 3

- Glyph name: uni21E1	Contours detected: 4	Expected: 3

- Glyph name: uni21E2	Contours detected: 4	Expected: 3

- Glyph name: uni21E3	Contours detected: 4	Expected: 3

- Glyph name: uni21E4	Contours detected: 1	Expected: 2

- Glyph name: uni21E5	Contours detected: 1	Expected: 2

- Glyph name: uni2213	Contours detected: 1	Expected: 2

- Glyph name: uni2270	Contours detected: 3	Expected: 2

- Glyph name: uni2271	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 572 among a set of 169 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 699:
uni22F3, suchthat, uni2289, uni22F6, uni228B, uni2ABD, uni22F8, uni22FD, uni22D0, uni22F9, propersubset, uni297E, uni22F5, uni2ABE, uni22D1, uni27C4, uni2288, uni2285, reflexsuperset, uni220C, uni2AC7, element, uni228A, uni27C3, uni22FB, reflexsubset, uni2AC8, notelement, uni297F, notsubset, propersuperset</p>
<p>Width = 540:
proportional</p>
<p>Width = 652:
orthogonal, uni2221, uni299D, uni29A3, uni29AB, uni29A8, uni27D4, uni29AA, uni22BE, uni299F, uni299B, angle, uni299C, uni299E, uni27C0, uni29A2, uni29A5, uni29A4, uni29A9, uni27D3</p>
<p>Width = 617:
uni2239, uni2A27</p>
<p>Width = 696:
uni223E</p>
<p>Width = 667:
uni2A33, uni223F</p>
<p>Width = 573:
uni2A88, uni2A7B, uni2AF3, lessequal, greaterequal, uni2A7C, approxequal, uni2270, uni2271</p>
<p>Width = 542:
uni2280, uni227B, uni227C, uni227D, uni2281, uni22E1, uni22DF, uni22DE, uni22E0, uni227A</p>
<p>Width = 756:
uni2AE9, uni2ADF, uni2AEB, uni22A2, uni2AE0, uni2AE4, uni22A5, uni2AEA, uni22A4, uni3012, uni2AE8, uni2AE7, uni22A3, uni22A8, uni2AE2</p>
<p>Width = 567:
uni22B0, uni22B1</p>
<p>Width = 532:
uni22D7, uni22D6</p>
<p>Width = 775:
uni297B, uni2979</p>
<p>Width = 579:
uni2994, uni2993</p>
<p>Width = 631:
uni2995, uni2996</p>
<p>Width = 624:
uni29A1</p>
<p>Width = 689:
uni29E3, uni29E4</p>
<p>Width = 744:
uni29FA</p>
<p>Width = 916:
uni29FB</p>
<p>Width = 745:
uni2A69, uni2A68</p>
<p>Width = 669:
uni2A7A, uni2A79</p>
<p>Width = 798:
uni2AA2, uni2AA1</p>
<p>Width = 760:
uni2AA9, uni2AA7, uni2AA8, uni2AA6</p>
<p>Width = 681:
uni2AAB, smallerthan, uni2AAD, uni2AAC</p>
<p>Width = 679:
uni2AD2, uni2AD6, uni2ACA, uni2AD1, uni2AD5, uni2ACB, uni2AC0, uni2AC9, uni2AD4, uni2AC4, uni2AC1, uni2AD3, uni2AC2, uni2AC5, uni2ACF, uni2AC3, uni2AD0, uni2AC6, uni2ACC, uni2ABF</p>
<p>Width = 754:
uni2AE1</p>
<p>Width = 836:
uni2AE6</p>
<p>Width = 547:
uni2AF4</p>
<p>Width = 735:
uni2AF5</p>
<p>Width = 222:
uni2AF6</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* u1D49C.uv001: L&lt;&lt;600.0,47.0&gt;--&lt;600.0,109.0&gt;&gt; -&gt; L&lt;&lt;600.0,109.0&gt;--&lt;602.0,246.0&gt;&gt;

* u1D604 (U+1D604): L&lt;&lt;425.0,432.0&gt;--&lt;369.0,189.0&gt;&gt; -&gt; L&lt;&lt;369.0,189.0&gt;--&lt;325.0,0.0&gt;&gt;

* u1D612 (U+1D612): L&lt;&lt;207.0,367.0&gt;--&lt;269.0,433.0&gt;&gt; -&gt; L&lt;&lt;269.0,433.0&gt;--&lt;543.0,714.0&gt;&gt;

* u1D612.ssty1: L&lt;&lt;264.0,368.0&gt;--&lt;336.0,459.0&gt;&gt; -&gt; L&lt;&lt;336.0,459.0&gt;--&lt;560.0,714.0&gt;&gt;

* u1D612.ssty2: L&lt;&lt;249.0,369.0&gt;--&lt;325.0,469.0&gt;&gt; -&gt; L&lt;&lt;325.0,469.0&gt;--&lt;530.0,714.0&gt;&gt;

* u1D646 (U+1D646): L&lt;&lt;251.0,369.0&gt;--&lt;327.0,471.0&gt;&gt; -&gt; L&lt;&lt;327.0,471.0&gt;--&lt;529.0,714.0&gt;&gt;

* u1D6EB (U+1D6EB): L&lt;&lt;207.0,367.0&gt;--&lt;269.0,433.0&gt;&gt; -&gt; L&lt;&lt;269.0,433.0&gt;--&lt;543.0,714.0&gt;&gt;

* u1D6EB.ssty1: L&lt;&lt;264.0,368.0&gt;--&lt;336.0,459.0&gt;&gt; -&gt; L&lt;&lt;336.0,459.0&gt;--&lt;560.0,714.0&gt;&gt;

* u1D6EB.ssty2: L&lt;&lt;249.0,369.0&gt;--&lt;325.0,469.0&gt;&gt; -&gt; L&lt;&lt;325.0,469.0&gt;--&lt;530.0,714.0&gt;&gt;

* uni2983 (U+2983): L&lt;&lt;347.0,784.0&gt;--&lt;347.0,784.0&gt;&gt; -&gt; L&lt;&lt;347.0,784.0&gt;--&lt;490.0,784.0&gt;&gt;

* uni2983.s01: L&lt;&lt;351.0,899.0&gt;--&lt;351.0,899.0&gt;&gt; -&gt; L&lt;&lt;351.0,899.0&gt;--&lt;498.0,899.0&gt;&gt;

* uni2983.s02: L&lt;&lt;355.0,1014.0&gt;--&lt;355.0,1014.0&gt;&gt; -&gt; L&lt;&lt;355.0,1014.0&gt;--&lt;505.0,1014.0&gt;&gt;

* uni2983.s03: L&lt;&lt;513.0,-520.0&gt;--&lt;360.0,-520.0&gt;&gt; -&gt; L&lt;&lt;360.0,-520.0&gt;--&lt;359.0,-520.0&gt;&gt;

* uni2983.s04: L&lt;&lt;364.0,1243.0&gt;--&lt;364.0,1243.0&gt;&gt; -&gt; L&lt;&lt;364.0,1243.0&gt;--&lt;520.0,1243.0&gt;&gt;

* uni2983.s05: L&lt;&lt;368.0,1358.0&gt;--&lt;368.0,1358.0&gt;&gt; -&gt; L&lt;&lt;368.0,1358.0&gt;--&lt;528.0,1358.0&gt;&gt;

* uni2983.s06: L&lt;&lt;372.0,1473.0&gt;--&lt;372.0,1473.0&gt;&gt; -&gt; L&lt;&lt;372.0,1473.0&gt;--&lt;535.0,1473.0&gt;&gt;

* uni2983.s07: L&lt;&lt;376.0,1588.0&gt;--&lt;376.0,1588.0&gt;&gt; -&gt; L&lt;&lt;376.0,1588.0&gt;--&lt;543.0,1588.0&gt;&gt;

* uni2983.s08: L&lt;&lt;380.0,1703.0&gt;--&lt;380.0,1703.0&gt;&gt; -&gt; L&lt;&lt;380.0,1703.0&gt;--&lt;550.0,1703.0&gt;&gt;

* uni2983.s09: L&lt;&lt;558.0,-1244.0&gt;--&lt;385.0,-1244.0&gt;&gt; -&gt; L&lt;&lt;385.0,-1244.0&gt;--&lt;384.0,-1244.0&gt;&gt;

* uni2983.s10: L&lt;&lt;389.0,1932.0&gt;--&lt;389.0,1932.0&gt;&gt; -&gt; L&lt;&lt;389.0,1932.0&gt;--&lt;565.0,1932.0&gt;&gt;

* uni2983.s11: L&lt;&lt;393.0,2047.0&gt;--&lt;393.0,2047.0&gt;&gt; -&gt; L&lt;&lt;393.0,2047.0&gt;--&lt;573.0,2047.0&gt;&gt;

* uni2983.s12: L&lt;&lt;397.0,2162.0&gt;--&lt;397.0,2162.0&gt;&gt; -&gt; L&lt;&lt;397.0,2162.0&gt;--&lt;580.0,2162.0&gt;&gt;

* uni2983.t: L&lt;&lt;397.0,1069.0&gt;--&lt;397.0,1069.0&gt;&gt; -&gt; L&lt;&lt;397.0,1069.0&gt;--&lt;580.0,1069.0&gt;&gt;

* uni2984 (U+2984): L&lt;&lt;32.0,784.0&gt;--&lt;175.0,784.0&gt;&gt; -&gt; L&lt;&lt;175.0,784.0&gt;--&lt;175.0,784.0&gt;&gt;

* uni2984.s01: L&lt;&lt;32.0,899.0&gt;--&lt;178.0,899.0&gt;&gt; -&gt; L&lt;&lt;178.0,899.0&gt;--&lt;178.0,899.0&gt;&gt;

* uni2984.s02: L&lt;&lt;32.0,1014.0&gt;--&lt;182.0,1014.0&gt;&gt; -&gt; L&lt;&lt;182.0,1014.0&gt;--&lt;182.0,1014.0&gt;&gt;

* uni2984.s04: L&lt;&lt;32.0,1243.0&gt;--&lt;188.0,1243.0&gt;&gt; -&gt; L&lt;&lt;188.0,1243.0&gt;--&lt;188.0,1243.0&gt;&gt;

* uni2984.s05: L&lt;&lt;32.0,1358.0&gt;--&lt;192.0,1358.0&gt;&gt; -&gt; L&lt;&lt;192.0,1358.0&gt;--&lt;192.0,1358.0&gt;&gt;

* uni2984.s06: L&lt;&lt;32.0,1473.0&gt;--&lt;195.0,1473.0&gt;&gt; -&gt; L&lt;&lt;195.0,1473.0&gt;--&lt;195.0,1473.0&gt;&gt;

* uni2984.s07: L&lt;&lt;32.0,1588.0&gt;--&lt;198.0,1588.0&gt;&gt; -&gt; L&lt;&lt;198.0,1588.0&gt;--&lt;198.0,1588.0&gt;&gt;

* uni2984.s08: L&lt;&lt;32.0,1703.0&gt;--&lt;202.0,1703.0&gt;&gt; -&gt; L&lt;&lt;202.0,1703.0&gt;--&lt;202.0,1703.0&gt;&gt;

* uni2984.s10: L&lt;&lt;32.0,1932.0&gt;--&lt;208.0,1932.0&gt;&gt; -&gt; L&lt;&lt;208.0,1932.0&gt;--&lt;208.0,1932.0&gt;&gt;

* uni2984.s11: L&lt;&lt;32.0,2047.0&gt;--&lt;212.0,2047.0&gt;&gt; -&gt; L&lt;&lt;212.0,2047.0&gt;--&lt;212.0,2047.0&gt;&gt;

* uni2984.s12: L&lt;&lt;32.0,2162.0&gt;--&lt;215.0,2162.0&gt;&gt; -&gt; L&lt;&lt;215.0,2162.0&gt;--&lt;215.0,2162.0&gt;&gt;

* uni2984.t: L&lt;&lt;51.0,1069.0&gt;--&lt;234.0,1069.0&gt;&gt; -&gt; L&lt;&lt;234.0,1069.0&gt;--&lt;234.0,1069.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* W.ssty1: B&lt;&lt;502.5,519.5&gt;-&lt;497.0,547.0&gt;-&lt;495.0,567.0&gt;&gt;/B&lt;&lt;495.0,567.0&gt;-&lt;492.0,547.0&gt;-&lt;486.5,519.0&gt;&gt; = 14.241358747447757

* W.ssty2: B&lt;&lt;531.5,500.5&gt;-&lt;525.0,532.0&gt;-&lt;523.0,548.0&gt;&gt;/B&lt;&lt;523.0,548.0&gt;-&lt;521.0,530.0&gt;-&lt;514.5,498.5&gt;&gt; = 13.465208094811695

* u1D4A9 (U+1D4A9): B&lt;&lt;638.0,510.5&gt;-&lt;658.0,602.0&gt;-&lt;695.0,666.0&gt;&gt;/B&lt;&lt;695.0,666.0&gt;-&lt;653.0,623.0&gt;-&lt;607.0,551.5&gt;&gt; = 14.292682666020351

* u1D4B6 (U+1D4B6): B&lt;&lt;266.0,51.0&gt;-&lt;266.0,82.0&gt;-&lt;279.0,108.0&gt;&gt;/B&lt;&lt;279.0,108.0&gt;-&lt;200.0,-6.0&gt;-&lt;125.0,-6.0&gt;&gt; = 8.156229018789725

* u1D4B7 (U+1D4B7): B&lt;&lt;113.0,187.0&gt;-&lt;126.0,210.0&gt;-&lt;139.0,236.0&gt;&gt;/B&lt;&lt;139.0,236.0&gt;-&lt;118.0,211.0&gt;-&lt;103.5,197.5&gt;&gt; = 13.465208094811695

* u1D4B7.ssty1: B&lt;&lt;76.5,126.5&gt;-&lt;92.0,161.0&gt;-&lt;130.0,227.0&gt;&gt;/B&lt;&lt;130.0,227.0&gt;-&lt;112.0,207.0&gt;-&lt;98.5,194.0&gt;&gt; = 12.055700655308824

* u1D4B7.ssty2: B&lt;&lt;70.5,125.0&gt;-&lt;86.0,162.0&gt;-&lt;120.0,217.0&gt;&gt;/B&lt;&lt;120.0,217.0&gt;-&lt;106.0,202.0&gt;-&lt;92.5,190.5&gt;&gt; = 11.30146303143393

* u1D4B9 (U+1D4B9): B&lt;&lt;261.0,51.0&gt;-&lt;261.0,82.0&gt;-&lt;274.0,108.0&gt;&gt;/B&lt;&lt;274.0,108.0&gt;-&lt;229.0,50.0&gt;-&lt;192.5,22.0&gt;&gt; = 11.241478767626447

* u1D4BB (U+1D4BB): L&lt;&lt;78.0,105.0&gt;--&lt;153.0,236.0&gt;&gt;/B&lt;&lt;153.0,236.0&gt;-&lt;132.0,214.0&gt;-&lt;116.0,198.5&gt;&gt; = 13.875819336765673

* u1D4BB.ssty1: L&lt;&lt;84.0,109.0&gt;--&lt;160.0,237.0&gt;&gt;/B&lt;&lt;160.0,237.0&gt;-&lt;122.0,196.0&gt;-&lt;88.0,169.0&gt;&gt; = 12.125533334575563

* u1D4BB.ssty2: L&lt;&lt;90.0,113.0&gt;--&lt;167.0,237.0&gt;&gt;/B&lt;&lt;167.0,237.0&gt;-&lt;150.0,219.0&gt;-&lt;131.0,201.5&gt;&gt; = 11.52447582395351

* u1D4BD (U+1D4BD): L&lt;&lt;414.0,586.0&gt;--&lt;166.0,112.0&gt;&gt;/B&lt;&lt;166.0,112.0&gt;-&lt;256.0,213.0&gt;-&lt;309.0,261.0&gt;&gt; = 14.0850159536873

* u1D4BD (U+1D4BD): L&lt;&lt;9.0,-6.0&gt;--&lt;139.0,236.0&gt;&gt;/B&lt;&lt;139.0,236.0&gt;-&lt;125.0,220.0&gt;-&lt;106.0,201.5&gt;&gt; = 12.94167409490862

* u1D4BD.ssty1: L&lt;&lt;15.0,-6.0&gt;--&lt;145.0,237.0&gt;&gt;/B&lt;&lt;145.0,237.0&gt;-&lt;130.0,220.0&gt;-&lt;111.5,201.5&gt;&gt; = 13.277800996699018

* u1D4BD.ssty1: L&lt;&lt;432.0,586.0&gt;--&lt;205.0,154.0&gt;&gt;/B&lt;&lt;205.0,154.0&gt;-&lt;276.0,234.0&gt;-&lt;324.0,271.0&gt;&gt; = 13.868791824470303

* u1D4BD.ssty2: L&lt;&lt;21.0,-7.0&gt;--&lt;151.0,238.0&gt;&gt;/B&lt;&lt;151.0,238.0&gt;-&lt;135.0,219.0&gt;-&lt;117.0,201.0&gt;&gt; = 12.149938518322031

* u1D4BE (U+1D4BE): B&lt;&lt;111.5,190.5&gt;-&lt;123.0,210.0&gt;-&lt;135.0,229.0&gt;&gt;/B&lt;&lt;135.0,229.0&gt;-&lt;123.0,216.0&gt;-&lt;107.5,201.0&gt;&gt; = 10.433745642783816

* u1D4BE.dtls.ssty1: B&lt;&lt;94.5,163.5&gt;-&lt;112.0,195.0&gt;-&lt;130.0,225.0&gt;&gt;/B&lt;&lt;130.0,225.0&gt;-&lt;120.0,213.0&gt;-&lt;105.0,198.0&gt;&gt; = 8.84181456019163

* u1D4BE.dtls.ssty2: B&lt;&lt;70.0,118.0&gt;-&lt;88.0,157.0&gt;-&lt;125.0,220.0&gt;&gt;/B&lt;&lt;125.0,220.0&gt;-&lt;115.0,209.0&gt;-&lt;101.0,195.0&gt;&gt; = 11.847905204132427

* u1D4BE.dtls: B&lt;&lt;111.5,190.5&gt;-&lt;123.0,210.0&gt;-&lt;135.0,229.0&gt;&gt;/B&lt;&lt;135.0,229.0&gt;-&lt;123.0,216.0&gt;-&lt;107.5,201.0&gt;&gt; = 10.433745642783816

* u1D4BE.ssty1: B&lt;&lt;94.5,163.5&gt;-&lt;112.0,195.0&gt;-&lt;130.0,225.0&gt;&gt;/B&lt;&lt;130.0,225.0&gt;-&lt;120.0,213.0&gt;-&lt;105.0,198.0&gt;&gt; = 8.84181456019163

* u1D4BE.ssty2: B&lt;&lt;70.0,118.0&gt;-&lt;88.0,157.0&gt;-&lt;125.0,220.0&gt;&gt;/B&lt;&lt;125.0,220.0&gt;-&lt;115.0,209.0&gt;-&lt;101.0,195.0&gt;&gt; = 11.847905204132427

* u1D4BF (U+1D4BF): L&lt;&lt;-1.0,-5.0&gt;--&lt;135.0,229.0&gt;&gt;/B&lt;&lt;135.0,229.0&gt;-&lt;124.0,216.0&gt;-&lt;108.5,201.0&gt;&gt; = 10.071350503532525

* u1D4BF.dtls.ssty1: L&lt;&lt;4.0,-1.0&gt;--&lt;132.0,221.0&gt;&gt;/B&lt;&lt;132.0,221.0&gt;-&lt;123.0,211.0&gt;-&lt;109.0,197.0&gt;&gt; = 12.020470625204926

* u1D4BF.dtls: L&lt;&lt;-1.0,-5.0&gt;--&lt;135.0,229.0&gt;&gt;/B&lt;&lt;135.0,229.0&gt;-&lt;124.0,216.0&gt;-&lt;108.5,201.0&gt;&gt; = 10.071350503532525

* u1D4BF.ssty1: L&lt;&lt;4.0,-1.0&gt;--&lt;132.0,221.0&gt;&gt;/B&lt;&lt;132.0,221.0&gt;-&lt;123.0,211.0&gt;-&lt;109.0,197.0&gt;&gt; = 12.020470625204926

* u1D4C0 (U+1D4C0): L&lt;&lt;7.0,-7.0&gt;--&lt;139.0,236.0&gt;&gt;/B&lt;&lt;139.0,236.0&gt;-&lt;123.0,218.0&gt;-&lt;107.0,202.0&gt;&gt; = 13.122293042461466

* u1D4C0.ssty1: L&lt;&lt;14.0,-7.0&gt;--&lt;147.0,241.0&gt;&gt;/B&lt;&lt;147.0,241.0&gt;-&lt;130.0,222.0&gt;-&lt;112.5,204.0&gt;&gt; = 13.615941208508001

* u1D4C0.ssty2: L&lt;&lt;20.0,-7.0&gt;--&lt;155.0,245.0&gt;&gt;/B&lt;&lt;155.0,245.0&gt;-&lt;137.0,224.0&gt;-&lt;118.0,204.0&gt;&gt; = 12.422704535045296

* u1D4C5 (U+1D4C5): L&lt;&lt;-142.0,-283.0&gt;--&lt;139.0,236.0&gt;&gt;/B&lt;&lt;139.0,236.0&gt;-&lt;122.0,215.0&gt;-&lt;105.5,198.5&gt;&gt; = 10.558735685480405

* u1D4C5.ssty1: L&lt;&lt;-145.0,-283.0&gt;--&lt;127.0,222.0&gt;&gt;/B&lt;&lt;127.0,222.0&gt;-&lt;100.0,190.0&gt;-&lt;74.0,169.0&gt;&gt; = 11.848478505359145

* u1D4C8 (U+1D4C8): B&lt;&lt;239.5,95.0&gt;-&lt;228.0,73.0&gt;-&lt;199.0,44.0&gt;&gt;/B&lt;&lt;199.0,44.0&gt;-&lt;237.0,69.0&gt;-&lt;273.0,105.0&gt;&gt; = 11.659292653522963

* u1D4C8.ssty1: B&lt;&lt;257.0,145.0&gt;-&lt;257.0,101.0&gt;-&lt;219.0,63.0&gt;&gt;/B&lt;&lt;219.0,63.0&gt;-&lt;250.0,84.0&gt;-&lt;281.0,115.0&gt;&gt; = 10.88552705465871

* u1D4C8.ssty2: B&lt;&lt;262.0,146.0&gt;-&lt;262.0,104.0&gt;-&lt;239.0,82.0&gt;&gt;/B&lt;&lt;239.0,82.0&gt;-&lt;265.0,102.0&gt;-&lt;288.0,125.0&gt;&gt; = 6.1583779511158045

* u1D4C9.ssty1: B&lt;&lt;100.0,166.0&gt;-&lt;113.0,192.0&gt;-&lt;132.0,228.0&gt;&gt;/B&lt;&lt;132.0,228.0&gt;-&lt;115.0,209.0&gt;-&lt;99.5,194.5&gt;&gt; = 13.996073495882507

* u1D4CA (U+1D4CA): B&lt;&lt;281.0,111.5&gt;-&lt;294.0,141.0&gt;-&lt;314.0,181.0&gt;&gt;/B&lt;&lt;314.0,181.0&gt;-&lt;230.0,64.0&gt;-&lt;192.0,30.0&gt;&gt; = 9.11135704478395

* u1D4CA (U+1D4CA): B&lt;&lt;77.5,130.5&gt;-&lt;99.0,172.0&gt;-&lt;138.0,233.0&gt;&gt;/B&lt;&lt;138.0,233.0&gt;-&lt;121.0,215.0&gt;-&lt;103.0,197.5&gt;&gt; = 10.77084148578403

* u1D4CA.ssty1: B&lt;&lt;286.0,95.0&gt;-&lt;293.0,113.0&gt;-&lt;304.0,137.0&gt;&gt;/B&lt;&lt;304.0,137.0&gt;-&lt;256.0,73.0&gt;-&lt;212.0,34.0&gt;&gt; = 12.246332859680393

* u1D4CA.ssty1: B&lt;&lt;74.5,124.5&gt;-&lt;93.0,164.0&gt;-&lt;130.0,224.0&gt;&gt;/B&lt;&lt;130.0,224.0&gt;-&lt;114.0,208.0&gt;-&lt;98.5,193.5&gt;&gt; = 13.339248903363371

* u1D4CC (U+1D4CC): B&lt;&lt;296.0,80.0&gt;-&lt;296.0,111.0&gt;-&lt;323.0,168.0&gt;&gt;/B&lt;&lt;323.0,168.0&gt;-&lt;260.0,79.0&gt;-&lt;210.5,35.5&gt;&gt; = 9.947171648713546

* u1D4CC (U+1D4CC): B&lt;&lt;76.0,130.5&gt;-&lt;97.0,171.0&gt;-&lt;137.0,232.0&gt;&gt;/B&lt;&lt;137.0,232.0&gt;-&lt;98.0,192.0&gt;-&lt;71.0,169.0&gt;&gt; = 11.02040912622867

* u1D4CC.ssty1: B&lt;&lt;308.0,82.0&gt;-&lt;308.0,102.0&gt;-&lt;323.0,136.0&gt;&gt;/B&lt;&lt;323.0,136.0&gt;-&lt;271.0,67.0&gt;-&lt;228.5,30.0&gt;&gt; = 13.196583009738436

* u1D4CC.ssty1: B&lt;&lt;81.0,139.0&gt;-&lt;105.0,179.0&gt;-&lt;148.0,239.0&gt;&gt;/B&lt;&lt;148.0,239.0&gt;-&lt;134.0,224.0&gt;-&lt;114.0,208.0&gt;&gt; = 7.39715869769701

* u1D4CD (U+1D4CD): B&lt;&lt;252.0,218.0&gt;-&lt;252.0,200.0&gt;-&lt;249.0,183.0&gt;&gt;/B&lt;&lt;249.0,183.0&gt;-&lt;275.0,247.0&gt;-&lt;297.0,277.5&gt;&gt; = 12.101468542310323

* u1D4CD.ssty1: B&lt;&lt;251.5,194.0&gt;-&lt;251.0,186.0&gt;-&lt;250.0,178.0&gt;&gt;/B&lt;&lt;250.0,178.0&gt;-&lt;271.0,241.0&gt;-&lt;295.5,274.5&gt;&gt; = 11.309932474020162

* u1D4CE (U+1D4CE): L&lt;&lt;241.0,-11.0&gt;--&lt;318.0,131.0&gt;&gt;/B&lt;&lt;318.0,131.0&gt;-&lt;215.0,-7.0&gt;-&lt;154.0,-7.0&gt;&gt; = 8.267887647015705

* u1D4CE.ssty1: L&lt;&lt;243.0,-7.0&gt;--&lt;305.0,107.0&gt;&gt;/B&lt;&lt;305.0,107.0&gt;-&lt;215.0,-7.0&gt;-&lt;159.0,-7.0&gt;&gt; = 9.750178004283045

* u1D4CE.ssty2: L&lt;&lt;244.0,-4.0&gt;--&lt;291.0,82.0&gt;&gt;/B&lt;&lt;291.0,82.0&gt;-&lt;216.0,-7.0&gt;-&lt;164.0,-7.0&gt;&gt; = 11.463608760435159

* u1D4D7 (U+1D4D7): B&lt;&lt;494.5,448.0&gt;-&lt;519.0,488.0&gt;-&lt;554.0,534.0&gt;&gt;/B&lt;&lt;554.0,534.0&gt;-&lt;523.0,509.0&gt;-&lt;492.0,486.5&gt;&gt; = 13.849101665308249

* u1D4EB (U+1D4EB): B&lt;&lt;70.5,125.0&gt;-&lt;86.0,162.0&gt;-&lt;120.0,217.0&gt;&gt;/B&lt;&lt;120.0,217.0&gt;-&lt;106.0,202.0&gt;-&lt;92.5,190.5&gt;&gt; = 11.30146303143393

* u1D4EF (U+1D4EF): L&lt;&lt;90.0,113.0&gt;--&lt;167.0,237.0&gt;&gt;/B&lt;&lt;167.0,237.0&gt;-&lt;150.0,219.0&gt;-&lt;131.0,201.5&gt;&gt; = 11.52447582395351

* u1D4F1 (U+1D4F1): L&lt;&lt;21.0,-7.0&gt;--&lt;151.0,238.0&gt;&gt;/B&lt;&lt;151.0,238.0&gt;-&lt;135.0,219.0&gt;-&lt;117.0,201.0&gt;&gt; = 12.149938518322031

* u1D4F2 (U+1D4F2): B&lt;&lt;70.0,118.0&gt;-&lt;88.0,157.0&gt;-&lt;125.0,220.0&gt;&gt;/B&lt;&lt;125.0,220.0&gt;-&lt;115.0,209.0&gt;-&lt;101.0,195.0&gt;&gt; = 11.847905204132427

* u1D4F4 (U+1D4F4): L&lt;&lt;20.0,-7.0&gt;--&lt;155.0,245.0&gt;&gt;/B&lt;&lt;155.0,245.0&gt;-&lt;137.0,224.0&gt;-&lt;118.0,204.0&gt;&gt; = 12.422704535045296

* u1D4FC (U+1D4FC): B&lt;&lt;262.0,146.0&gt;-&lt;262.0,104.0&gt;-&lt;239.0,82.0&gt;&gt;/B&lt;&lt;239.0,82.0&gt;-&lt;265.0,102.0&gt;-&lt;288.0,125.0&gt;&gt; = 6.1583779511158045

* u1D502 (U+1D502): L&lt;&lt;244.0,-4.0&gt;--&lt;291.0,82.0&gt;&gt;/B&lt;&lt;291.0,82.0&gt;-&lt;216.0,-7.0&gt;-&lt;164.0,-7.0&gt;&gt; = 11.463608760435159

* u1D50A.ssty2: B&lt;&lt;481.5,442.5&gt;-&lt;471.0,419.0&gt;-&lt;455.0,395.0&gt;&gt;/B&lt;&lt;455.0,395.0&gt;-&lt;475.0,413.0&gt;-&lt;507.0,425.0&gt;&gt; = 14.322719978203523

* u1D572 (U+1D572): B&lt;&lt;456.0,449.5&gt;-&lt;445.0,426.0&gt;-&lt;430.0,407.0&gt;&gt;/B&lt;&lt;430.0,407.0&gt;-&lt;440.0,415.0&gt;-&lt;451.5,422.0&gt;&gt; = 13.050028553666817

* u1D5EA (U+1D5EA): B&lt;&lt;266.0,196.0&gt;-&lt;272.0,161.0&gt;-&lt;275.0,137.0&gt;&gt;/B&lt;&lt;275.0,137.0&gt;-&lt;278.0,162.0&gt;-&lt;284.0,196.5&gt;&gt; = 13.967789761532726

* u1D5EA (U+1D5EA): B&lt;&lt;489.0,505.5&gt;-&lt;485.0,529.0&gt;-&lt;483.0,542.0&gt;&gt;/B&lt;&lt;483.0,542.0&gt;-&lt;482.0,529.0&gt;-&lt;477.5,505.5&gt;&gt; = 13.144867617550734

* u1D5EA (U+1D5EA): B&lt;&lt;683.0,196.0&gt;-&lt;689.0,161.0&gt;-&lt;692.0,137.0&gt;&gt;/B&lt;&lt;692.0,137.0&gt;-&lt;695.0,162.0&gt;-&lt;701.0,196.5&gt;&gt; = 13.967789761532726

* u1D709 (U+1D709): B&lt;&lt;235.5,675.0&gt;-&lt;265.0,691.0&gt;-&lt;291.0,699.0&gt;&gt;/B&lt;&lt;291.0,699.0&gt;-&lt;280.0,697.0&gt;-&lt;261.5,695.0&gt;&gt; = 6.79788250028636

* u1D709.ssty1: B&lt;&lt;187.5,615.5&gt;-&lt;221.0,650.0&gt;-&lt;290.0,668.0&gt;&gt;/B&lt;&lt;290.0,668.0&gt;-&lt;262.0,666.0&gt;-&lt;243.0,664.0&gt;&gt; = 10.535257208656729

* u1D709.ssty2: B&lt;&lt;205.5,600.0&gt;-&lt;235.0,636.0&gt;-&lt;315.0,656.0&gt;&gt;/B&lt;&lt;315.0,656.0&gt;-&lt;281.0,654.0&gt;-&lt;261.5,652.0&gt;&gt; = 10.669782804496695

* u1D761 (U+1D761): L&lt;&lt;361.0,0.0&gt;--&lt;213.0,580.0&gt;&gt;/L&lt;&lt;213.0,580.0&gt;--&lt;213.0,0.0&gt;&gt; = 14.314826910404852

* u1D761 (U+1D761): L&lt;&lt;658.0,0.0&gt;--&lt;658.0,580.0&gt;&gt;/L&lt;&lt;658.0,580.0&gt;--&lt;512.0,0.0&gt;&gt; = 14.129180579464611

* u1D79B (U+1D79B): L&lt;&lt;594.0,0.0&gt;--&lt;706.0,584.0&gt;&gt;/L&lt;&lt;706.0,584.0&gt;--&lt;444.0,0.0&gt;&gt; = 13.306028360029698

* u1F7BF (U+1F7BF): L&lt;&lt;209.0,640.0&gt;--&lt;343.0,374.0&gt;&gt;/L&lt;&lt;343.0,374.0&gt;--&lt;250.0,657.0&gt;&gt; = 8.545453953148678

* u1F7BF (U+1F7BF): L&lt;&lt;250.0,57.0&gt;--&lt;343.0,340.0&gt;&gt;/L&lt;&lt;343.0,340.0&gt;--&lt;209.0,74.0&gt;&gt; = 8.545453953148678

* u1F7BF (U+1F7BF): L&lt;&lt;450.0,657.0&gt;--&lt;357.0,374.0&gt;&gt;/L&lt;&lt;357.0,374.0&gt;--&lt;491.0,640.0&gt;&gt; = 8.545453953148678

* u1F7BF (U+1F7BF): L&lt;&lt;491.0,74.0&gt;--&lt;357.0,340.0&gt;&gt;/L&lt;&lt;357.0,340.0&gt;--&lt;450.0,57.0&gt;&gt; = 8.545453953148678

* u1F7BF (U+1F7BF): L&lt;&lt;50.0,457.0&gt;--&lt;333.0,364.0&gt;&gt;/L&lt;&lt;333.0,364.0&gt;--&lt;67.0,498.0&gt;&gt; = 8.545453953148636

* u1F7BF (U+1F7BF): L&lt;&lt;633.0,498.0&gt;--&lt;367.0,364.0&gt;&gt;/L&lt;&lt;367.0,364.0&gt;--&lt;650.0,457.0&gt;&gt; = 8.545453953148636

* u1F7BF (U+1F7BF): L&lt;&lt;650.0,257.0&gt;--&lt;367.0,350.0&gt;&gt;/L&lt;&lt;367.0,350.0&gt;--&lt;633.0,216.0&gt;&gt; = 8.545453953148636

* u1F7BF (U+1F7BF): L&lt;&lt;67.0,216.0&gt;--&lt;333.0,350.0&gt;&gt;/L&lt;&lt;333.0,350.0&gt;--&lt;50.0,257.0&gt;&gt; = 8.545453953148636

* uni210B (U+210B): B&lt;&lt;491.0,431.5&gt;-&lt;529.0,502.0&gt;-&lt;593.0,581.0&gt;&gt;/B&lt;&lt;593.0,581.0&gt;-&lt;569.0,559.0&gt;-&lt;539.5,535.0&gt;&gt; = 8.477701297774663

* uni210B.ssty1: B&lt;&lt;481.5,420.5&gt;-&lt;516.0,484.0&gt;-&lt;574.0,558.0&gt;&gt;/B&lt;&lt;574.0,558.0&gt;-&lt;543.0,531.0&gt;-&lt;506.5,503.5&gt;&gt; = 10.856413348062235

* uni210B.ssty2: B&lt;&lt;494.5,448.0&gt;-&lt;519.0,488.0&gt;-&lt;554.0,534.0&gt;&gt;/B&lt;&lt;554.0,534.0&gt;-&lt;523.0,509.0&gt;-&lt;492.0,486.5&gt;&gt; = 13.849101665308249

* uni2133 (U+2133): B&lt;&lt;994.5,596.0&gt;-&lt;1045.0,653.0&gt;-&lt;1086.0,696.0&gt;&gt;/B&lt;&lt;1086.0,696.0&gt;-&lt;1069.0,684.0&gt;-&lt;1026.0,649.5&gt;&gt; = 11.14633456341022

* uni2137 (U+2137): L&lt;&lt;254.0,0.0&gt;--&lt;214.0,180.0&gt;&gt;/B&lt;&lt;214.0,180.0&gt;-&lt;214.0,146.0&gt;-&lt;195.5,115.5&gt;&gt; = 12.528807709151492

* uni263D (U+263D): B&lt;&lt;277.0,98.0&gt;-&lt;225.0,53.0&gt;-&lt;155.0,37.0&gt;&gt;/B&lt;&lt;155.0,37.0&gt;-&lt;221.0,37.0&gt;-&lt;278.0,62.0&gt;&gt; = 12.875001559612462

* uni263D (U+263D): B&lt;&lt;278.0,646.5&gt;-&lt;221.0,671.0&gt;-&lt;155.0,671.0&gt;&gt;/B&lt;&lt;155.0,671.0&gt;-&lt;225.0,656.0&gt;-&lt;277.0,610.5&gt;&gt; = 12.094757077012089

* uni263E (U+263E): B&lt;&lt;283.0,61.5&gt;-&lt;340.0,37.0&gt;-&lt;406.0,37.0&gt;&gt;/B&lt;&lt;406.0,37.0&gt;-&lt;337.0,53.0&gt;-&lt;285.0,97.5&gt;&gt; = 13.055247223796592

* uni263E (U+263E): B&lt;&lt;285.0,610.5&gt;-&lt;337.0,656.0&gt;-&lt;406.0,671.0&gt;&gt;/B&lt;&lt;406.0,671.0&gt;-&lt;340.0,671.0&gt;-&lt;283.0,646.0&gt;&gt; = 12.2647737278924

* uni2667 (U+2667): B&lt;&lt;261.0,507.0&gt;-&lt;279.0,501.0&gt;-&lt;293.0,490.0&gt;&gt;/B&lt;&lt;293.0,490.0&gt;-&lt;277.0,506.0&gt;-&lt;266.5,532.5&gt;&gt; = 6.842773412630916

* uni2667 (U+2667): B&lt;&lt;609.5,532.0&gt;-&lt;599.0,505.0&gt;-&lt;583.0,490.0&gt;&gt;/B&lt;&lt;583.0,490.0&gt;-&lt;597.0,501.0&gt;-&lt;615.0,507.0&gt;&gt; = 4.995163146636313

* uni2983.s01: L&lt;&lt;351.0,-279.0&gt;--&lt;351.0,-279.0&gt;&gt;/B&lt;&lt;351.0,-279.0&gt;-&lt;261.0,-278.0&gt;-&lt;205.5,-239.0&gt;&gt; = 0.6365935759634798

* uni2983.s04: L&lt;&lt;364.0,-641.0&gt;--&lt;364.0,-641.0&gt;&gt;/B&lt;&lt;364.0,-641.0&gt;-&lt;264.0,-640.0&gt;-&lt;207.0,-602.0&gt;&gt; = 0.5729386976832647

* uni2989.s03: L&lt;&lt;127.0,295.0&gt;--&lt;292.0,-361.0&gt;&gt;/L&lt;&lt;292.0,-361.0&gt;--&lt;292.0,978.0&gt;&gt; = 14.118417351366187

* uni2989.s04: L&lt;&lt;128.0,295.0&gt;--&lt;314.0,-472.0&gt;&gt;/L&lt;&lt;314.0,-472.0&gt;--&lt;314.0,1083.0&gt;&gt; = 13.631270823875766

* uni2989.s04: L&lt;&lt;314.0,-472.0&gt;--&lt;314.0,1083.0&gt;&gt;/L&lt;&lt;314.0,1083.0&gt;--&lt;128.0,337.0&gt;&gt; = 14.000094715932251

* uni2989.s05: L&lt;&lt;130.0,295.0&gt;--&lt;337.0,-583.0&gt;&gt;/L&lt;&lt;337.0,-583.0&gt;--&lt;337.0,1188.0&gt;&gt; = 13.265978238800068

* uni2989.s05: L&lt;&lt;337.0,-583.0&gt;--&lt;337.0,1188.0&gt;&gt;/L&lt;&lt;337.0,1188.0&gt;--&lt;130.0,341.0&gt;&gt; = 13.733431319117

* uni2989.s06: L&lt;&lt;132.0,295.0&gt;--&lt;360.0,-693.0&gt;&gt;/L&lt;&lt;360.0,-693.0&gt;--&lt;360.0,1294.0&gt;&gt; = 12.994616791916512

* uni2989.s06: L&lt;&lt;360.0,-693.0&gt;--&lt;360.0,1294.0&gt;&gt;/L&lt;&lt;360.0,1294.0&gt;--&lt;132.0,344.0&gt;&gt; = 13.495733280795811

* uni2989.s07: L&lt;&lt;134.0,295.0&gt;--&lt;382.0,-804.0&gt;&gt;/L&lt;&lt;382.0,-804.0&gt;--&lt;382.0,1399.0&gt;&gt; = 12.716354599101924

* uni2989.s07: L&lt;&lt;382.0,-804.0&gt;--&lt;382.0,1399.0&gt;&gt;/L&lt;&lt;382.0,1399.0&gt;--&lt;134.0,348.0&gt;&gt; = 13.276977270368576

* uni2989.s08: L&lt;&lt;136.0,295.0&gt;--&lt;405.0,-915.0&gt;&gt;/L&lt;&lt;405.0,-915.0&gt;--&lt;405.0,1504.0&gt;&gt; = 12.53382134052769

* uni2989.s08: L&lt;&lt;405.0,-915.0&gt;--&lt;405.0,1504.0&gt;&gt;/L&lt;&lt;405.0,1504.0&gt;--&lt;136.0,351.0&gt;&gt; = 13.132451396970199

* uni2989.s09: L&lt;&lt;138.0,295.0&gt;--&lt;427.0,-1026.0&gt;&gt;/L&lt;&lt;427.0,-1026.0&gt;--&lt;427.0,1609.0&gt;&gt; = 12.340380782773712

* uni2989.s09: L&lt;&lt;427.0,-1026.0&gt;--&lt;427.0,1609.0&gt;&gt;/L&lt;&lt;427.0,1609.0&gt;--&lt;138.0,355.0&gt;&gt; = 12.97793096924386

* uni2989.s10: L&lt;&lt;139.0,295.0&gt;--&lt;450.0,-1137.0&gt;&gt;/L&lt;&lt;450.0,-1137.0&gt;--&lt;450.0,1714.0&gt;&gt; = 12.253145463966021

* uni2989.s10: L&lt;&lt;450.0,-1137.0&gt;--&lt;450.0,1714.0&gt;&gt;/L&lt;&lt;450.0,1714.0&gt;--&lt;139.0,358.0&gt;&gt; = 12.917444569427033

* uni2989.s11: L&lt;&lt;141.0,295.0&gt;--&lt;472.0,-1248.0&gt;&gt;/L&lt;&lt;472.0,-1248.0&gt;--&lt;472.0,1819.0&gt;&gt; = 12.107435939277618

* uni2989.s11: L&lt;&lt;472.0,-1248.0&gt;--&lt;472.0,1819.0&gt;&gt;/L&lt;&lt;472.0,1819.0&gt;--&lt;141.0,362.0&gt;&gt; = 12.799166912595032

* uni2989.s12: L&lt;&lt;143.0,295.0&gt;--&lt;495.0,-1359.0&gt;&gt;/L&lt;&lt;495.0,-1359.0&gt;--&lt;495.0,1924.0&gt;&gt; = 12.01429882395764

* uni2989.s12: L&lt;&lt;495.0,-1359.0&gt;--&lt;495.0,1924.0&gt;&gt;/L&lt;&lt;495.0,1924.0&gt;--&lt;143.0,365.0&gt;&gt; = 12.723227660310524

* uni298A.s03: L&lt;&lt;123.0,978.0&gt;--&lt;123.0,-361.0&gt;&gt;/L&lt;&lt;123.0,-361.0&gt;--&lt;288.0,295.0&gt;&gt; = 14.118417351366187

* uni298A.s04: L&lt;&lt;125.0,1083.0&gt;--&lt;125.0,-472.0&gt;&gt;/L&lt;&lt;125.0,-472.0&gt;--&lt;311.0,295.0&gt;&gt; = 13.631270823875766

* uni298A.s04: L&lt;&lt;311.0,337.0&gt;--&lt;125.0,1083.0&gt;&gt;/L&lt;&lt;125.0,1083.0&gt;--&lt;125.0,-472.0&gt;&gt; = 14.000094715932251

* uni298A.s05: L&lt;&lt;127.0,1188.0&gt;--&lt;127.0,-583.0&gt;&gt;/L&lt;&lt;127.0,-583.0&gt;--&lt;334.0,295.0&gt;&gt; = 13.265978238800068

* uni298A.s05: L&lt;&lt;334.0,341.0&gt;--&lt;127.0,1188.0&gt;&gt;/L&lt;&lt;127.0,1188.0&gt;--&lt;127.0,-583.0&gt;&gt; = 13.733431319117

* uni298A.s06: L&lt;&lt;130.0,1294.0&gt;--&lt;130.0,-693.0&gt;&gt;/L&lt;&lt;130.0,-693.0&gt;--&lt;357.0,295.0&gt;&gt; = 12.939545079954247

* uni298A.s06: L&lt;&lt;357.0,344.0&gt;--&lt;130.0,1294.0&gt;&gt;/L&lt;&lt;130.0,1294.0&gt;--&lt;130.0,-693.0&gt;&gt; = 13.438693060398712

* uni298A.s07: L&lt;&lt;132.0,1399.0&gt;--&lt;132.0,-804.0&gt;&gt;/L&lt;&lt;132.0,-804.0&gt;--&lt;380.0,295.0&gt;&gt; = 12.716354599101924

* uni298A.s07: L&lt;&lt;380.0,348.0&gt;--&lt;132.0,1399.0&gt;&gt;/L&lt;&lt;132.0,1399.0&gt;--&lt;132.0,-804.0&gt;&gt; = 13.276977270368576

* uni298A.s08: L&lt;&lt;134.0,1504.0&gt;--&lt;134.0,-915.0&gt;&gt;/L&lt;&lt;134.0,-915.0&gt;--&lt;403.0,295.0&gt;&gt; = 12.53382134052769

* uni298A.s08: L&lt;&lt;403.0,351.0&gt;--&lt;134.0,1504.0&gt;&gt;/L&lt;&lt;134.0,1504.0&gt;--&lt;134.0,-915.0&gt;&gt; = 13.132451396970199

* uni298A.s09: L&lt;&lt;136.0,1609.0&gt;--&lt;136.0,-1026.0&gt;&gt;/L&lt;&lt;136.0,-1026.0&gt;--&lt;426.0,295.0&gt;&gt; = 12.381766172602543

* uni298A.s09: L&lt;&lt;426.0,355.0&gt;--&lt;136.0,1609.0&gt;&gt;/L&lt;&lt;136.0,1609.0&gt;--&lt;136.0,-1026.0&gt;&gt; = 13.021309442914834

* uni298A.s10: L&lt;&lt;139.0,1714.0&gt;--&lt;139.0,-1137.0&gt;&gt;/L&lt;&lt;139.0,-1137.0&gt;--&lt;449.0,295.0&gt;&gt; = 12.21493109749736

* uni298A.s10: L&lt;&lt;449.0,358.0&gt;--&lt;139.0,1714.0&gt;&gt;/L&lt;&lt;139.0,1714.0&gt;--&lt;139.0,-1137.0&gt;&gt; = 12.877296144293375

* uni298A.s11: L&lt;&lt;141.0,1819.0&gt;--&lt;141.0,-1248.0&gt;&gt;/L&lt;&lt;141.0,-1248.0&gt;--&lt;472.0,295.0&gt;&gt; = 12.107435939277618

* uni298A.s11: L&lt;&lt;472.0,362.0&gt;--&lt;141.0,1819.0&gt;&gt;/L&lt;&lt;141.0,1819.0&gt;--&lt;141.0,-1248.0&gt;&gt; = 12.799166912595032

* uni298A.s12: L&lt;&lt;143.0,1924.0&gt;--&lt;143.0,-1359.0&gt;&gt;/L&lt;&lt;143.0,-1359.0&gt;--&lt;495.0,295.0&gt;&gt; = 12.01429882395764

* uni298A.s12: L&lt;&lt;495.0,365.0&gt;--&lt;143.0,1924.0&gt;&gt;/L&lt;&lt;143.0,1924.0&gt;--&lt;143.0,-1359.0&gt;&gt; = 12.723227660310524

* uni2A17.rtlm.s01: B&lt;&lt;588.0,200.5&gt;-&lt;593.0,140.0&gt;-&lt;599.0,81.0&gt;&gt;/L&lt;&lt;599.0,81.0&gt;--&lt;599.0,140.0&gt;&gt; = 5.806726905531528

* xi (U+03BE): B&lt;&lt;162.5,663.5&gt;-&lt;196.0,682.0&gt;-&lt;236.0,693.0&gt;&gt;/B&lt;&lt;236.0,693.0&gt;-&lt;217.0,691.0&gt;-&lt;183.0,689.0&gt;&gt; = 9.367245291331619

* xi.ssty1: B&lt;&lt;145.0,620.0&gt;-&lt;182.0,651.0&gt;-&lt;251.0,668.0&gt;&gt;/B&lt;&lt;251.0,668.0&gt;-&lt;231.0,667.0&gt;-&lt;206.5,665.5&gt;&gt; = 10.978290265543803

* xi.ssty2: B&lt;&lt;186.5,610.0&gt;-&lt;221.0,641.0&gt;-&lt;291.0,657.0&gt;&gt;/B&lt;&lt;291.0,657.0&gt;-&lt;262.0,655.0&gt;-&lt;231.0,653.0&gt;&gt; = 8.929815330574892
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* male (U+2642): L&lt;&lt;565.0,534.0&gt;--&lt;566.0,365.0&gt;&gt;

* u1D61E.ssty2: L&lt;&lt;229.0,714.0&gt;--&lt;232.0,322.0&gt;&gt;

* u1D638.ssty2: L&lt;&lt;215.0,546.0&gt;--&lt;217.0,302.0&gt;&gt;

* u1D638.ssty2: L&lt;&lt;540.0,546.0&gt;--&lt;541.0,283.0&gt;&gt;

* u1D652 (U+1D652): L&lt;&lt;230.0,714.0&gt;--&lt;233.0,324.0&gt;&gt;

* u1D66C (U+1D66C): L&lt;&lt;198.0,546.0&gt;--&lt;200.0,304.0&gt;&gt;

* u1EEA8 (U+1EEA8): L&lt;&lt;303.0,80.0&gt;--&lt;418.0,79.0&gt;&gt;

* u1EEA8 (U+1EEA8): L&lt;&lt;418.0,59.0&gt;--&lt;265.0,60.0&gt;&gt;

* u1EEBA (U+1EEBA): L&lt;&lt;303.0,80.0&gt;--&lt;418.0,79.0&gt;&gt;

* u1EEBA (U+1EEBA): L&lt;&lt;418.0,59.0&gt;--&lt;285.0,60.0&gt;&gt;

* uni0411 (U+0411): L&lt;&lt;98.0,0.0&gt;--&lt;97.0,714.0&gt;&gt;

* uni042B (U+042B): L&lt;&lt;187.0,714.0&gt;--&lt;186.0,436.0&gt;&gt;

* uni2296 (U+2296): L&lt;&lt;125.0,310.0&gt;--&lt;711.0,311.0&gt;&gt;

* uni2296 (U+2296): L&lt;&lt;711.0,247.0&gt;--&lt;125.0,246.0&gt;&gt;

* uni26A5 (U+26A5): L&lt;&lt;565.0,776.0&gt;--&lt;566.0,607.0&gt;&gt;

* uni2997 (U+2997): L&lt;&lt;81.0,179.0&gt;--&lt;80.0,447.0&gt;&gt;

* uni2997.s01: L&lt;&lt;81.0,69.0&gt;--&lt;80.0,551.0&gt;&gt;

* uni2997.s02: L&lt;&lt;81.0,-40.0&gt;--&lt;80.0,654.0&gt;&gt;

* uni2997.s03: L&lt;&lt;81.0,-149.0&gt;--&lt;80.0,758.0&gt;&gt;

* uni2997.s04: L&lt;&lt;81.0,-259.0&gt;--&lt;80.0,862.0&gt;&gt;

* uni2997.s05: L&lt;&lt;81.0,-368.0&gt;--&lt;80.0,965.0&gt;&gt;

* uni2997.s06: L&lt;&lt;81.0,-478.0&gt;--&lt;80.0,1069.0&gt;&gt;

* uni2998 (U+2998): L&lt;&lt;259.0,447.0&gt;--&lt;258.0,179.0&gt;&gt;

* uni2998.s01: L&lt;&lt;267.0,551.0&gt;--&lt;266.0,69.0&gt;&gt;

* uni2998.s02: L&lt;&lt;275.0,654.0&gt;--&lt;274.0,-40.0&gt;&gt;

* uni2998.s04: L&lt;&lt;290.0,862.0&gt;--&lt;289.0,-259.0&gt;&gt;

* uni2998.s05: L&lt;&lt;298.0,965.0&gt;--&lt;297.0,-368.0&gt;&gt;

* uni2998.s06: L&lt;&lt;306.0,1069.0&gt;--&lt;305.0,-478.0&gt;&gt;

* uni2998.s10: L&lt;&lt;337.0,1484.0&gt;--&lt;336.0,-916.0&gt;&gt;

* uni2A19.rtlm.s01: L&lt;&lt;225.0,21.0&gt;--&lt;224.0,334.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃐ i⃑ i⃔ i⃕ i⃖ i⃗ i⃛ i⃜ i⃡ i⃧ i⃩ ị⃐ ị⃑ ị⃔ ị⃕ ị⃖ ị⃗ ị⃛ ị⃜ ị⃡</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Ijo, Southeast (Latn, 2,471,000 speakers), Dutch (Latn, 31,709,104 speakers), Ebira (Latn, 2,200,000 speakers), Igbo (Latn, 27,823,640 speakers), Ekpeye (Latn, 226,000 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Ma’di (Latn, 584,000 speakers), Bafut (Latn, 158,146 speakers), Yala (Latn, 200,000 speakers), Vute (Latn, 21,000 speakers), Avokaya (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), South Central Banda (Latn, 244,000 speakers), Koonzime (Latn, 40,000 speakers), Gulay (Latn, 250,478 speakers), Mango (Latn, 77,000 speakers), Navajo (Latn, 166,319 speakers), Zapotec (Latn, 490,000 speakers), Nateni (Latn, 100,000 speakers), Lithuanian (Latn, 2,357,094 speakers), Fur (Latn, 1,230,163 speakers), Mundani (Latn, 34,000 speakers), Aghem (Latn, 38,843 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Bete-Bendi (Latn, 100,000 speakers), Sar (Latn, 500,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Dan (Latn, 1,099,244 speakers), Mfumte (Latn, 79,000 speakers), Nzakara (Latn, 50,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Makaa (Latn, 221,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Southern Kisi (Latn, 360,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D4 MODIFIER LETTER UP TACK: not included in any glyphset definition</li>
<li>U+02D5 MODIFIER LETTER DOWN TACK: not included in any glyphset definition</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0310 COMBINING CANDRABINDU: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: not included in any glyphset definition</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: not included in any glyphset definition</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding syriac</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, caucasian-albanian, gothic, cherokee, syriac</li>
<li>U+0332 COMBINING LOW LINE: not included in any glyphset definition</li>
<li>U+0333 COMBINING DOUBLE LOW LINE: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+033A COMBINING INVERTED BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+033F COMBINING DOUBLE OVERLINE: try adding coptic</li>
<li>U+0346 COMBINING BRIDGE ABOVE: not included in any glyphset definition</li>
<li>U+034D COMBINING LEFT RIGHT ARROW BELOW: not included in any glyphset definition</li>
<li>U+03DC GREEK LETTER DIGAMMA: try adding one of: greek, elbasan</li>
<li>U+03DD GREEK SMALL LETTER DIGAMMA: try adding greek</li>
<li>U+03F6 GREEK REVERSED LUNATE EPSILON SYMBOL: try adding greek</li>
<li>U+0606 ARABIC-INDIC CUBE ROOT: try adding arabic</li>
<li>U+0607 ARABIC-INDIC FOURTH ROOT: try adding arabic</li>
<li>U+0608 ARABIC RAY: try adding arabic</li>
<li>U+0609 ARABIC-INDIC PER MILLE SIGN: try adding arabic</li>
<li>U+060A ARABIC-INDIC PER TEN THOUSAND SIGN: try adding arabic</li>
<li>U+060C ARABIC COMMA: try adding one of: hanifi-rohingya, thaana, yezidi, syriac, nko, arabic</li>
<li>U+0627 ARABIC LETTER ALEF: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+0628 ARABIC LETTER BEH: try adding arabic</li>
<li>U+062A ARABIC LETTER TEH: try adding arabic</li>
<li>U+062B ARABIC LETTER THEH: try adding arabic</li>
<li>U+062C ARABIC LETTER JEEM: try adding arabic</li>
<li>U+062D ARABIC LETTER HAH: try adding arabic</li>
<li>U+062E ARABIC LETTER KHAH: try adding arabic</li>
<li>U+062F ARABIC LETTER DAL: try adding arabic</li>
<li>U+0630 ARABIC LETTER THAL: try adding arabic</li>
<li>U+0631 ARABIC LETTER REH: try adding arabic</li>
<li>U+0632 ARABIC LETTER ZAIN: try adding arabic</li>
<li>U+0633 ARABIC LETTER SEEN: try adding arabic</li>
<li>U+0634 ARABIC LETTER SHEEN: try adding arabic</li>
<li>U+0635 ARABIC LETTER SAD: try adding arabic</li>
<li>U+0636 ARABIC LETTER DAD: try adding arabic</li>
<li>U+0637 ARABIC LETTER TAH: try adding arabic</li>
<li>U+0638 ARABIC LETTER ZAH: try adding arabic</li>
<li>U+0639 ARABIC LETTER AIN: try adding arabic</li>
<li>U+063A ARABIC LETTER GHAIN: try adding arabic</li>
<li>U+0641 ARABIC LETTER FEH: try adding arabic</li>
<li>U+0642 ARABIC LETTER QAF: try adding arabic</li>
<li>U+0643 ARABIC LETTER KAF: try adding arabic</li>
<li>U+0644 ARABIC LETTER LAM: try adding arabic</li>
<li>U+0645 ARABIC LETTER MEEM: try adding arabic</li>
<li>U+0646 ARABIC LETTER NOON: try adding arabic</li>
<li>U+0647 ARABIC LETTER HEH: try adding arabic</li>
<li>U+0648 ARABIC LETTER WAW: try adding arabic</li>
<li>U+0649 ARABIC LETTER ALEF MAKSURA: try adding arabic</li>
<li>U+064A ARABIC LETTER YEH: try adding arabic</li>
<li>U+0660 ARABIC-INDIC DIGIT ZERO: try adding one of: hanifi-rohingya, thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0661 ARABIC-INDIC DIGIT ONE: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0662 ARABIC-INDIC DIGIT TWO: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0663 ARABIC-INDIC DIGIT THREE: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0664 ARABIC-INDIC DIGIT FOUR: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0665 ARABIC-INDIC DIGIT FIVE: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0666 ARABIC-INDIC DIGIT SIX: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0667 ARABIC-INDIC DIGIT SEVEN: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0668 ARABIC-INDIC DIGIT EIGHT: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+0669 ARABIC-INDIC DIGIT NINE: try adding one of: thaana, yezidi, syriac, indic-siyaq-numbers, arabic</li>
<li>U+066A ARABIC PERCENT SIGN: try adding one of: nko, thaana, syriac, arabic</li>
<li>U+066B ARABIC DECIMAL SEPARATOR: try adding one of: thaana, syriac, arabic</li>
<li>U+066C ARABIC THOUSANDS SEPARATOR: try adding one of: thaana, syriac, arabic</li>
<li>U+066E ARABIC LETTER DOTLESS BEH: try adding arabic</li>
<li>U+066F ARABIC LETTER DOTLESS QAF: try adding arabic</li>
<li>U+06A1 ARABIC LETTER DOTLESS FEH: try adding arabic</li>
<li>U+06BA ARABIC LETTER NOON GHUNNA: try adding arabic</li>
<li>U+06F0 EXTENDED ARABIC-INDIC DIGIT ZERO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F1 EXTENDED ARABIC-INDIC DIGIT ONE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F2 EXTENDED ARABIC-INDIC DIGIT TWO: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F3 EXTENDED ARABIC-INDIC DIGIT THREE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F4 EXTENDED ARABIC-INDIC DIGIT FOUR: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F5 EXTENDED ARABIC-INDIC DIGIT FIVE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F6 EXTENDED ARABIC-INDIC DIGIT SIX: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F7 EXTENDED ARABIC-INDIC DIGIT SEVEN: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F8 EXTENDED ARABIC-INDIC DIGIT EIGHT: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+06F9 EXTENDED ARABIC-INDIC DIGIT NINE: try adding one of: indic-siyaq-numbers, arabic</li>
<li>U+1D46 MODIFIER LETTER SMALL TURNED AE: not included in any glyphset definition</li>
<li>U+2000 EN QUAD: not included in any glyphset definition</li>
<li>U+2001 EM QUAD: not included in any glyphset definition</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2004 THREE-PER-EM SPACE: not included in any glyphset definition</li>
<li>U+2005 FOUR-PER-EM SPACE: not included in any glyphset definition</li>
<li>U+2006 SIX-PER-EM SPACE: not included in any glyphset definition</li>
<li>U+2007 FIGURE SPACE: not included in any glyphset definition</li>
<li>U+2008 PUNCTUATION SPACE: not included in any glyphset definition</li>
<li>U+200A HAIR SPACE: not included in any glyphset definition</li>
<li>U+2010 HYPHEN: try adding one of: cham, armenian, coptic, kayah-li, sora-sompeng, yi, hebrew, lisu, sundanese, kaithi, syloti-nagri, kharoshthi, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: not included in any glyphset definition</li>
<li>U+2017 DOUBLE LOW LINE: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+202F NARROW NO-BREAK SPACE: try adding one of: yi, mongolian</li>
<li>U+2038 CARET: not included in any glyphset definition</li>
<li>U+203C DOUBLE EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+2040 CHARACTER TIE: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: not included in any glyphset definition</li>
<li>U+2047 DOUBLE QUESTION MARK: not included in any glyphset definition</li>
<li>U+2050 CLOSE UP: not included in any glyphset definition</li>
<li>U+205F MEDIUM MATHEMATICAL SPACE: not included in any glyphset definition</li>
<li>U+20DD COMBINING ENCLOSING CIRCLE: try adding symbols</li>
<li>U+20DE COMBINING ENCLOSING SQUARE: try adding symbols</li>
<li>U+20DF COMBINING ENCLOSING DIAMOND: try adding symbols</li>
<li>U+20E4 COMBINING ENCLOSING UPWARD POINTING TRIANGLE: try adding symbols</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2107 EULER CONSTANT: not included in any glyphset definition</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: not included in any glyphset definition</li>
<li>U+2118 SCRIPT CAPITAL P: not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: not included in any glyphset definition</li>
<li>U+2127 INVERTED OHM SIGN: not included in any glyphset definition</li>
<li>U+2129 TURNED GREEK SMALL LETTER IOTA: not included in any glyphset definition</li>
<li>U+212B ANGSTROM SIGN: not included in any glyphset definition</li>
<li>U+2132 TURNED CAPITAL F: not included in any glyphset definition</li>
<li>U+2141 TURNED SANS-SERIF CAPITAL G: not included in any glyphset definition</li>
<li>U+2142 TURNED SANS-SERIF CAPITAL L: not included in any glyphset definition</li>
<li>U+2143 REVERSED SANS-SERIF CAPITAL L: not included in any glyphset definition</li>
<li>U+2144 TURNED SANS-SERIF CAPITAL Y: not included in any glyphset definition</li>
<li>U+214A PROPERTY LINE: not included in any glyphset definition</li>
<li>U+214B TURNED AMPERSAND: not included in any glyphset definition</li>
<li>U+21AF DOWNWARDS ZIGZAG ARROW: try adding symbols</li>
<li>U+21E6 LEFTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E8 RIGHTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E9 DOWNWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+21EB UPWARDS WHITE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21EC UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR: try adding symbols</li>
<li>U+21ED UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR: try adding symbols</li>
<li>U+21EE UPWARDS WHITE DOUBLE ARROW: try adding symbols</li>
<li>U+21EF UPWARDS WHITE DOUBLE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21F0 RIGHTWARDS WHITE ARROW FROM WALL: try adding symbols</li>
<li>U+21F3 UP DOWN WHITE ARROW: try adding symbols</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2302 HOUSE: try adding symbols</li>
<li>U+2305 PROJECTIVE: try adding symbols</li>
<li>U+2306 PERSPECTIVE: try adding symbols</li>
<li>U+2311 SQUARE LOZENGE: try adding symbols</li>
<li>U+2312 ARC: try adding symbols</li>
<li>U+2313 SEGMENT: try adding symbols</li>
<li>U+2317 VIEWDATA SQUARE: try adding symbols</li>
<li>U+2322 FROWN: try adding symbols</li>
<li>U+2323 SMILE: try adding symbols</li>
<li>U+232C BENZENE RING: try adding symbols</li>
<li>U+2332 CONICAL TAPER: try adding symbols</li>
<li>U+2394 SOFTWARE-FUNCTION SYMBOL: try adding symbols</li>
<li>U+23B7 RADICAL SYMBOL BOTTOM: not included in any glyphset definition</li>
<li>U+23B8 LEFT VERTICAL BOX LINE: not included in any glyphset definition</li>
<li>U+23B9 RIGHT VERTICAL BOX LINE: not included in any glyphset definition</li>
<li>U+23CE RETURN SYMBOL: try adding symbols</li>
<li>U+23E2 WHITE TRAPEZIUM: try adding symbols</li>
<li>U+23E3 BENZENE RING WITH CIRCLE: try adding symbols</li>
<li>U+23E4 STRAIGHTNESS: try adding symbols</li>
<li>U+23E5 FLATNESS: try adding symbols</li>
<li>U+23E6 AC CURRENT: try adding symbols</li>
<li>U+23E7 ELECTRICAL INTERSECTION: try adding symbols</li>
<li>U+2422 BLANK SYMBOL: try adding symbols</li>
<li>U+2423 OPEN BOX: try adding symbols</li>
<li>U+2500 BOX DRAWINGS LIGHT HORIZONTAL: not included in any glyphset definition</li>
<li>U+2506 BOX DRAWINGS LIGHT TRIPLE DASH VERTICAL: not included in any glyphset definition</li>
<li>U+250C BOX DRAWINGS LIGHT DOWN AND RIGHT: not included in any glyphset definition</li>
<li>U+2510 BOX DRAWINGS LIGHT DOWN AND LEFT: not included in any glyphset definition</li>
<li>U+2514 BOX DRAWINGS LIGHT UP AND RIGHT: not included in any glyphset definition</li>
<li>U+2518 BOX DRAWINGS LIGHT UP AND LEFT: not included in any glyphset definition</li>
<li>U+2550 BOX DRAWINGS DOUBLE HORIZONTAL: not included in any glyphset definition</li>
<li>U+2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT: not included in any glyphset definition</li>
<li>U+2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT: not included in any glyphset definition</li>
<li>U+2577 BOX DRAWINGS LIGHT DOWN: not included in any glyphset definition</li>
<li>U+2580 UPPER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2584 LOWER HALF BLOCK: not included in any glyphset definition</li>
<li>U+2588 FULL BLOCK: not included in any glyphset definition</li>
<li>U+258C LEFT HALF BLOCK: not included in any glyphset definition</li>
<li>U+2590 RIGHT HALF BLOCK: not included in any glyphset definition</li>
<li>U+2591 LIGHT SHADE: not included in any glyphset definition</li>
<li>U+2592 MEDIUM SHADE: not included in any glyphset definition</li>
<li>U+2593 DARK SHADE: not included in any glyphset definition</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25A2 WHITE SQUARE WITH ROUNDED CORNERS: try adding symbols</li>
<li>U+25A3 WHITE SQUARE CONTAINING BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25A4 SQUARE WITH HORIZONTAL FILL: try adding symbols</li>
<li>U+25A5 SQUARE WITH VERTICAL FILL: try adding symbols</li>
<li>U+25A6 SQUARE WITH ORTHOGONAL CROSSHATCH FILL: try adding symbols</li>
<li>U+25A7 SQUARE WITH UPPER LEFT TO LOWER RIGHT FILL: try adding symbols</li>
<li>U+25A8 SQUARE WITH UPPER RIGHT TO LOWER LEFT FILL: try adding symbols</li>
<li>U+25A9 SQUARE WITH DIAGONAL CROSSHATCH FILL: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25AC BLACK RECTANGLE: try adding symbols</li>
<li>U+25AD WHITE RECTANGLE: try adding symbols</li>
<li>U+25AE BLACK VERTICAL RECTANGLE: try adding symbols</li>
<li>U+25B0 BLACK PARALLELOGRAM: try adding symbols</li>
<li>U+25B1 WHITE PARALLELOGRAM: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BB WHITE RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C5 WHITE LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25C8 WHITE DIAMOND CONTAINING BLACK SMALL DIAMOND: try adding symbols</li>
<li>U+25C9 FISHEYE: try adding symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CD CIRCLE WITH VERTICAL FILL: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25D4 CIRCLE WITH UPPER RIGHT QUADRANT BLACK: try adding symbols</li>
<li>U+25D5 CIRCLE WITH ALL BUT UPPER LEFT QUADRANT BLACK: try adding symbols</li>
<li>U+25D6 LEFT HALF BLACK CIRCLE: try adding symbols</li>
<li>U+25D7 RIGHT HALF BLACK CIRCLE: try adding symbols</li>
<li>U+25D8 INVERSE BULLET: try adding symbols</li>
<li>U+25D9 INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25DA UPPER HALF INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25DB LOWER HALF INVERSE WHITE CIRCLE: try adding symbols</li>
<li>U+25DC UPPER LEFT QUADRANT CIRCULAR ARC: try adding symbols</li>
<li>U+25DD UPPER RIGHT QUADRANT CIRCULAR ARC: try adding symbols</li>
<li>U+25DE LOWER RIGHT QUADRANT CIRCULAR ARC: try adding symbols</li>
<li>U+25DF LOWER LEFT QUADRANT CIRCULAR ARC: try adding symbols</li>
<li>U+25E0 UPPER HALF CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+25E2 BLACK LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E3 BLACK LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E4 BLACK UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25E5 BLACK UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+25E7 SQUARE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25E8 SQUARE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25E9 SQUARE WITH UPPER LEFT DIAGONAL HALF BLACK: try adding symbols</li>
<li>U+25EA SQUARE WITH LOWER RIGHT DIAGONAL HALF BLACK: try adding symbols</li>
<li>U+25EB WHITE SQUARE WITH VERTICAL BISECTING LINE: try adding symbols</li>
<li>U+25EC WHITE UP-POINTING TRIANGLE WITH DOT: try adding symbols</li>
<li>U+25ED UP-POINTING TRIANGLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25EE UP-POINTING TRIANGLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25EF LARGE CIRCLE: try adding symbols</li>
<li>U+25F0 WHITE SQUARE WITH UPPER LEFT QUADRANT: try adding symbols</li>
<li>U+25F1 WHITE SQUARE WITH LOWER LEFT QUADRANT: try adding symbols</li>
<li>U+25F2 WHITE SQUARE WITH LOWER RIGHT QUADRANT: try adding symbols</li>
<li>U+25F3 WHITE SQUARE WITH UPPER RIGHT QUADRANT: try adding symbols</li>
<li>U+25F4 WHITE CIRCLE WITH UPPER LEFT QUADRANT: try adding symbols</li>
<li>U+25F5 WHITE CIRCLE WITH LOWER LEFT QUADRANT: try adding symbols</li>
<li>U+25F6 WHITE CIRCLE WITH LOWER RIGHT QUADRANT: try adding symbols</li>
<li>U+25F7 WHITE CIRCLE WITH UPPER RIGHT QUADRANT: try adding symbols</li>
<li>U+25F8 UPPER LEFT TRIANGLE: try adding symbols</li>
<li>U+25F9 UPPER RIGHT TRIANGLE: try adding symbols</li>
<li>U+25FA LOWER LEFT TRIANGLE: try adding symbols</li>
<li>U+25FC BLACK MEDIUM SQUARE: try adding symbols</li>
<li>U+25FD WHITE MEDIUM SMALL SQUARE: try adding symbols</li>
<li>U+25FE BLACK MEDIUM SMALL SQUARE: try adding symbols</li>
<li>U+25FF LOWER RIGHT TRIANGLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2609 SUN: try adding symbols</li>
<li>U+2621 CAUTION SIGN: try adding symbols</li>
<li>U+263B BLACK SMILING FACE: try adding symbols</li>
<li>U+263C WHITE SUN WITH RAYS: try adding symbols</li>
<li>U+263D FIRST QUARTER MOON: try adding symbols</li>
<li>U+263E LAST QUARTER MOON: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2660 BLACK SPADE SUIT: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2662 WHITE DIAMOND SUIT: try adding symbols</li>
<li>U+2663 BLACK CLUB SUIT: try adding symbols</li>
<li>U+2664 WHITE SPADE SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2666 BLACK DIAMOND SUIT: try adding symbols</li>
<li>U+2667 WHITE CLUB SUIT: try adding symbols</li>
<li>U+2669 QUARTER NOTE: try adding one of: music, symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+266C BEAMED SIXTEENTH NOTES: try adding one of: music, symbols</li>
<li>U+267E PERMANENT PAPER SIGN: try adding symbols</li>
<li>U+2680 DIE FACE-1: try adding symbols</li>
<li>U+2681 DIE FACE-2: try adding symbols</li>
<li>U+2682 DIE FACE-3: try adding symbols</li>
<li>U+2683 DIE FACE-4: try adding symbols</li>
<li>U+2684 DIE FACE-5: try adding symbols</li>
<li>U+2685 DIE FACE-6: try adding symbols</li>
<li>U+2686 WHITE CIRCLE WITH DOT RIGHT: try adding symbols</li>
<li>U+2687 WHITE CIRCLE WITH TWO DOTS: try adding symbols</li>
<li>U+2688 BLACK CIRCLE WITH WHITE DOT RIGHT: try adding symbols</li>
<li>U+2689 BLACK CIRCLE WITH TWO WHITE DOTS: try adding symbols</li>
<li>U+26A5 MALE AND FEMALE SIGN: try adding symbols</li>
<li>U+26AA MEDIUM WHITE CIRCLE: try adding symbols</li>
<li>U+26AB MEDIUM BLACK CIRCLE: try adding symbols</li>
<li>U+26AC MEDIUM SMALL WHITE CIRCLE: try adding symbols</li>
<li>U+26B2 NEUTER: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2720 MALTESE CROSS: try adding symbols</li>
<li>U+272A CIRCLED WHITE STAR: try adding symbols</li>
<li>U+2736 SIX POINTED BLACK STAR: try adding symbols</li>
<li>U+2739 TWELVE POINTED BLACK STAR: try adding symbols</li>
<li>U+273D HEAVY TEARDROP-SPOKED ASTERISK: try adding symbols</li>
<li>U+2772 LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT: try adding symbols</li>
<li>U+2773 LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT: try adding symbols</li>
<li>U+279B DRAFTING POINT RIGHTWARDS ARROW: try adding symbols</li>
<li>U+2B00 NORTH EAST WHITE ARROW: try adding symbols</li>
<li>U+2B01 NORTH WEST WHITE ARROW: try adding symbols</li>
<li>U+2B02 SOUTH EAST WHITE ARROW: try adding symbols</li>
<li>U+2B03 SOUTH WEST WHITE ARROW: try adding symbols</li>
<li>U+2B04 LEFT RIGHT WHITE ARROW: try adding symbols</li>
<li>U+2B12 SQUARE WITH TOP HALF BLACK: try adding symbols</li>
<li>U+2B13 SQUARE WITH BOTTOM HALF BLACK: try adding symbols</li>
<li>U+2B14 SQUARE WITH UPPER RIGHT DIAGONAL HALF BLACK: try adding symbols</li>
<li>U+2B15 SQUARE WITH LOWER LEFT DIAGONAL HALF BLACK: try adding symbols</li>
<li>U+2B16 DIAMOND WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+2B17 DIAMOND WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+2B18 DIAMOND WITH TOP HALF BLACK: try adding symbols</li>
<li>U+2B19 DIAMOND WITH BOTTOM HALF BLACK: try adding symbols</li>
<li>U+2B1A DOTTED SQUARE: try adding symbols</li>
<li>U+2B1B BLACK LARGE SQUARE: try adding symbols</li>
<li>U+2B1C WHITE LARGE SQUARE: try adding symbols</li>
<li>U+2B1D BLACK VERY SMALL SQUARE: try adding symbols</li>
<li>U+2B1E WHITE VERY SMALL SQUARE: try adding symbols</li>
<li>U+2B1F BLACK PENTAGON: try adding symbols</li>
<li>U+2B20 WHITE PENTAGON: try adding symbols</li>
<li>U+2B21 WHITE HEXAGON: try adding symbols</li>
<li>U+2B22 BLACK HEXAGON: try adding symbols</li>
<li>U+2B23 HORIZONTAL BLACK HEXAGON: try adding symbols</li>
<li>U+2B24 BLACK LARGE CIRCLE: try adding symbols</li>
<li>U+2B25 BLACK MEDIUM DIAMOND: try adding symbols</li>
<li>U+2B26 WHITE MEDIUM DIAMOND: try adding symbols</li>
<li>U+2B27 BLACK MEDIUM LOZENGE: try adding symbols</li>
<li>U+2B28 WHITE MEDIUM LOZENGE: try adding symbols</li>
<li>U+2B29 BLACK SMALL DIAMOND: try adding symbols</li>
<li>U+2B2A BLACK SMALL LOZENGE: try adding symbols</li>
<li>U+2B2B WHITE SMALL LOZENGE: try adding symbols</li>
<li>U+2B2C BLACK HORIZONTAL ELLIPSE: try adding symbols</li>
<li>U+2B2D WHITE HORIZONTAL ELLIPSE: try adding symbols</li>
<li>U+2B2E BLACK VERTICAL ELLIPSE: try adding symbols</li>
<li>U+2B2F WHITE VERTICAL ELLIPSE: try adding symbols</li>
<li>U+2B50 WHITE MEDIUM STAR: try adding symbols</li>
<li>U+2B51 BLACK SMALL STAR: try adding symbols</li>
<li>U+2B52 WHITE SMALL STAR: try adding symbols</li>
<li>U+2B53 BLACK RIGHT-POINTING PENTAGON: try adding symbols</li>
<li>U+2B54 WHITE RIGHT-POINTING PENTAGON: try adding symbols</li>
<li>U+3012 POSTAL MARK: try adding one of: yi, phags-pa, japanese, chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+3030 WAVY DASH: not included in any glyphset definition</li>
<li>U+FE00 VARIATION SELECTOR-1: try adding one of: phags-pa, yi, manichaean</li>
<li>U+1F780 BLACK LEFT-POINTING ISOSCELES RIGHT TRIANGLE: try adding symbols</li>
<li>U+1F781 BLACK UP-POINTING ISOSCELES RIGHT TRIANGLE: try adding symbols</li>
<li>U+1F782 BLACK RIGHT-POINTING ISOSCELES RIGHT TRIANGLE: try adding symbols</li>
<li>U+1F783 BLACK DOWN-POINTING ISOSCELES RIGHT TRIANGLE: try adding symbols</li>
<li>U+1F784 BLACK SLIGHTLY SMALL CIRCLE: try adding symbols</li>
<li>U+1F785 MEDIUM BOLD WHITE CIRCLE: try adding symbols</li>
<li>U+1F786 BOLD WHITE CIRCLE: try adding symbols</li>
<li>U+1F787 HEAVY WHITE CIRCLE: try adding symbols</li>
<li>U+1F788 VERY HEAVY WHITE CIRCLE: try adding symbols</li>
<li>U+1F789 EXTREMELY HEAVY WHITE CIRCLE: try adding symbols</li>
<li>U+1F78A WHITE CIRCLE CONTAINING BLACK SMALL CIRCLE: try adding symbols</li>
<li>U+1F78B ROUND TARGET: try adding symbols</li>
<li>U+1F78C BLACK TINY SQUARE: try adding symbols</li>
<li>U+1F78D BLACK SLIGHTLY SMALL SQUARE: try adding symbols</li>
<li>U+1F78E LIGHT WHITE SQUARE: try adding symbols</li>
<li>U+1F78F MEDIUM WHITE SQUARE: try adding symbols</li>
<li>U+1F790 BOLD WHITE SQUARE: try adding symbols</li>
<li>U+1F791 HEAVY WHITE SQUARE: try adding symbols</li>
<li>U+1F792 VERY HEAVY WHITE SQUARE: try adding symbols</li>
<li>U+1F793 EXTREMELY HEAVY WHITE SQUARE: try adding symbols</li>
<li>U+1F794 WHITE SQUARE CONTAINING BLACK VERY SMALL SQUARE: try adding symbols</li>
<li>U+1F795 WHITE SQUARE CONTAINING BLACK MEDIUM SQUARE: try adding symbols</li>
<li>U+1F796 SQUARE TARGET: try adding symbols</li>
<li>U+1F797 BLACK TINY DIAMOND: try adding symbols</li>
<li>U+1F798 BLACK VERY SMALL DIAMOND: try adding symbols</li>
<li>U+1F799 BLACK MEDIUM SMALL DIAMOND: try adding symbols</li>
<li>U+1F79A WHITE DIAMOND CONTAINING BLACK VERY SMALL DIAMOND: try adding symbols</li>
<li>U+1F79B WHITE DIAMOND CONTAINING BLACK MEDIUM DIAMOND: try adding symbols</li>
<li>U+1F79C DIAMOND TARGET: try adding symbols</li>
<li>U+1F79D BLACK TINY LOZENGE: try adding symbols</li>
<li>U+1F79E BLACK VERY SMALL LOZENGE: try adding symbols</li>
<li>U+1F79F BLACK MEDIUM SMALL LOZENGE: try adding symbols</li>
<li>U+1F7A0 WHITE LOZENGE CONTAINING BLACK SMALL LOZENGE: try adding symbols</li>
<li>U+1F7A1 THIN GREEK CROSS: try adding symbols</li>
<li>U+1F7A2 LIGHT GREEK CROSS: try adding symbols</li>
<li>U+1F7A3 MEDIUM GREEK CROSS: try adding symbols</li>
<li>U+1F7A4 BOLD GREEK CROSS: try adding symbols</li>
<li>U+1F7A5 VERY BOLD GREEK CROSS: try adding symbols</li>
<li>U+1F7A6 VERY HEAVY GREEK CROSS: try adding symbols</li>
<li>U+1F7A7 EXTREMELY HEAVY GREEK CROSS: try adding symbols</li>
<li>U+1F7A8 THIN SALTIRE: try adding symbols</li>
<li>U+1F7A9 LIGHT SALTIRE: try adding symbols</li>
<li>U+1F7AA MEDIUM SALTIRE: try adding symbols</li>
<li>U+1F7AB BOLD SALTIRE: try adding symbols</li>
<li>U+1F7AC HEAVY SALTIRE: try adding symbols</li>
<li>U+1F7AD VERY HEAVY SALTIRE: try adding symbols</li>
<li>U+1F7AE EXTREMELY HEAVY SALTIRE: try adding symbols</li>
<li>U+1F7AF LIGHT FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B0 MEDIUM FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B1 BOLD FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B2 HEAVY FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B3 VERY HEAVY FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B4 EXTREMELY HEAVY FIVE SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B5 LIGHT SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B6 MEDIUM SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B7 BOLD SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B8 HEAVY SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7B9 VERY HEAVY SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BA EXTREMELY HEAVY SIX SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BB LIGHT EIGHT SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BC MEDIUM EIGHT SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BD BOLD EIGHT SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BE HEAVY EIGHT SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7BF VERY HEAVY EIGHT SPOKED ASTERISK: try adding symbols</li>
<li>U+1F7C0 LIGHT THREE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C1 MEDIUM THREE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C2 THREE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C3 MEDIUM THREE POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7C4 LIGHT FOUR POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C5 MEDIUM FOUR POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C6 FOUR POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7C7 MEDIUM FOUR POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7C8 REVERSE LIGHT FOUR POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7C9 LIGHT FIVE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7CA HEAVY FIVE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7CB MEDIUM SIX POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7CC HEAVY SIX POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7CD SIX POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7CE MEDIUM EIGHT POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7CF HEAVY EIGHT POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7D0 VERY HEAVY EIGHT POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7D1 HEAVY EIGHT POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7D2 LIGHT TWELVE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7D3 HEAVY TWELVE POINTED BLACK STAR: try adding symbols</li>
<li>U+1F7D4 HEAVY TWELVE POINTED PINWHEEL STAR: try adding symbols</li>
<li>U+1F7D5 CIRCLED TRIANGLE: try adding symbols</li>
<li>U+1F7D6 NEGATIVE CIRCLED TRIANGLE: try adding symbols</li>
<li>U+1F7D7 CIRCLED SQUARE: try adding symbols</li>
<li>U+1F7D8 NEGATIVE CIRCLED SQUARE: try adding symbols</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>latin</code>, <code>latin-ext</code>, <code>math</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 5 | 10 | 117 | 6 | 113 | 0 | 
| 0% | 0% | 2% | 4% | 47% | 2% | 45% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
