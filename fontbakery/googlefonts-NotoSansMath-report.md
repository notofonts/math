## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[12] NotoSansMath-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x00AB (LEFT-POINTING DOUBLE ANGLE QUOTATION MARK)


	- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)


	- 0x02D9 (DOT ABOVE)


	- 0x00C1 (LATIN CAPITAL LETTER A WITH ACUTE)


	- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


	- 0x00C2 (LATIN CAPITAL LETTER A WITH CIRCUMFLEX)


	- 0x00C4 (LATIN CAPITAL LETTER A WITH DIAERESIS)


	- 0x00C0 (LATIN CAPITAL LETTER A WITH GRAVE)


	- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


	- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)
 

	- 179 more.

Use -F or --full-lists to disable shortening of long lists. [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Noto fonts must have an ARTICLE.en_us.html file (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/description/noto_has_article">com.google.fonts/check/description/noto_has_article</a>)</summary><div>


* 🔥 **FAIL** This is a Noto font but it lacks an ARTICLE.en_us.html file [code: missing-article]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 2962, but got 2685 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 2406, but got 1572 instead. [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Glyphs are similiar to Google Fonts version? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/production_glyphs_similarity">com.google.fonts/check/production_glyphs_similarity</a>)</summary><div>


* ⚠ **WARN** Following glyphs differ greatly from Google Fonts version:
	* radical
	* u1D400
	* u1D401
	* u1D402
	* u1D403
	* u1D404
	* u1D405
	* u1D406
	* u1D407
	* u1D408 and 439 more.

Use -F or --full-lists to disable shortening of long lists.
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- arrowdblup.x

	- arrowleft.l

	- arrowright.r

	- arrowup.x

	- backslash.s1

	- backslash.s2

	- backslash.s3

	- backslash.s4

	- braceleft.s1

	- braceleft.s10 

	- 473 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni210A	Contours detected: 3	Expected: 2

	- Glyph name: uni210D	Contours detected: 3	Expected: 2

	- Glyph name: uni2119	Contours detected: 4	Expected: 2

	- Glyph name: uni211A	Contours detected: 5	Expected: 3

	- Glyph name: uni211D	Contours detected: 5	Expected: 3

	- Glyph name: uni21C7	Contours detected: 2	Expected: 1

	- Glyph name: uni21C8	Contours detected: 2	Expected: 1

	- Glyph name: uni21C9	Contours detected: 2	Expected: 1

	- Glyph name: uni21CA	Contours detected: 2	Expected: 1

	- Glyph name: uni21E0	Contours detected: 4	Expected: 3 

	- 18 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters should disappear in other cases, for example: i̅ i⃐ i⃑ i⃔ i⃕ i⃖ i⃗ i⃛ i⃜ i⃡ i⃧ i⃩ ị̅ ị⃐ ị⃑ ị⃔ ị⃕ ị⃖ ị⃗ ị⃛ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 572 among a set of 170 math glyphs.
The following math glyphs have a different width, though:

Width = 699:
uni2AC7, uni22FB, uni2AC8, uni2288, propersuperset, uni2289, uni22F5, uni228B, uni22D0, uni22F8, propersubset, uni27C3, uni27C4, reflexsubset, notelement, uni220C, uni22FD, element, uni2ABE, uni22F9, uni2ABD, notsubset, uni22F6, uni22F3, uni228A, suchthat, uni2285, reflexsuperset, uni22D1

Width = 540:
proportional

Width = 652:
uni2221, uni299D, uni27D4, uni27D3, uni29AA, uni29A5, uni29A4, uni299F, uni299E, uni29AB, uni29A9, uni27C0, uni299C, uni29A8, uni22BE, uni299B, angle, orthogonal, uni29A3, uni29A2

Width = 617:
uni2239, uni2A27

Width = 696:
uni223E

Width = 667:
uni223F, uni2A33

Width = 542:
uni227A, uni2280, uni227C, uni2281, uni22E1, uni22DF, uni227B, uni227D, uni22DE, uni22E0

Width = 644:
uni2292, uni2291, uni2290

Width = 756:
uni22A5, uni22A8, uni22A2, uni2AE2, uni2ADF, uni2AE0, uni2AE4, uni2AEB, uni22A4, uni22A3, uni2AEA, uni2AE8, uni2AE7, uni2AE9

Width = 567:
uni22B0, uni22B1

Width = 600:
uni22D5

Width = 532:
uni22D7, uni22D6

Width = 775:
uni2979, uni297B

Width = 634:
uni297F, uni297E

Width = 732:
uni2995, uni2994, uni2996, uni2993

Width = 624:
uni29A1

Width = 689:
uni29E5, uni29E3, uni29E4

Width = 744:
uni29FA

Width = 916:
uni29FB

Width = 745:
uni2A68, uni2A69

Width = 762:
uni2A78

Width = 669:
uni2A7A, uni2A79

Width = 573:
uni2A7B, uni2A7C

Width = 798:
uni2AA1, uni2AA2

Width = 760:
uni2AA7, uni2AA6, uni2AA9, uni2AA8

Width = 681:
uni2AAD, uni2AAB, smallerthanorequalto, smallerthan

Width = 679:
uni2AC6, uni2AD0, uni2AC0, uni2AD2, uni2AD5, uni2ABF, uni2ACF, uni2AD1, uni2AD4, uni2AD3, uni2AC9, uni2AC3, uni2AC1, uni2AC5, uni2ACA, uni2AD6, uni2AC2, uni2ACB, uni2ACC, uni2AC4

Width = 754:
uni2AE1

Width = 836:
uni2AE6

Width = 547:
uni2AF4

Width = 735:
uni2AF5

Width = 222:
uni2AF6
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* doublestruckrehArabicmath (U+1EEB3): L<<232.0,323.0>--<262.0,266.0>> -> L<<262.0,266.0>--<282.0,231.0>>

	* doublestruckzainArabicmath (U+1EEA6): L<<232.0,323.0>--<262.0,266.0>> -> L<<262.0,266.0>--<282.0,231.0>>

	* u1D604 (U+1D604): L<<425.0,432.0>--<369.0,189.0>> -> L<<369.0,189.0>--<325.0,0.0>>

	* u1D612 (U+1D612): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* u1D646 (U+1D646): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* u1D6FD (U+1D6FD): L<<-38.0,-240.0>--<42.0,126.0>> -> L<<42.0,126.0>--<127.0,543.0>>

	* u1D707 (U+1D707): L<<-34.0,-240.0>--<45.0,126.0>> -> L<<45.0,126.0>--<126.0,536.0>>

	* u1D70C (U+1D70C): L<<-59.0,-240.0>--<17.0,109.0>> -> L<<17.0,109.0>--<47.0,253.0>>

	* u1D737 (U+1D737): L<<-48.0,-240.0>--<32.0,126.0>> -> L<<32.0,126.0>--<109.0,527.0>>

	* u1D741 (U+1D741): L<<-48.0,-240.0>--<22.0,75.0>> -> L<<22.0,75.0>--<111.0,536.0>> 

	* 3 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* u1D432 (U+1D432): B<<321.0,162.0>-<327.0,138.0>-<329.0,118.0>>/B<<329.0,118.0>-<331.0,139.0>-<339.5,165.0>> = 11.150925168505127

	* u1D4A9 (U+1D4A9): B<<638.0,510.5>-<658.0,602.0>-<695.0,666.0>>/B<<695.0,666.0>-<653.0,623.0>-<607.0,551.5>> = 14.292682666020351

	* u1D4B6 (U+1D4B6): B<<266.0,51.0>-<266.0,82.0>-<279.0,108.0>>/B<<279.0,108.0>-<200.0,-6.0>-<125.0,-6.0>> = 8.156229018789725

	* u1D4B7 (U+1D4B7): B<<113.0,187.0>-<126.0,210.0>-<139.0,236.0>>/B<<139.0,236.0>-<118.0,211.0>-<103.5,197.5>> = 13.465208094811695

	* u1D4B9 (U+1D4B9): B<<261.0,51.0>-<261.0,82.0>-<274.0,108.0>>/B<<274.0,108.0>-<229.0,50.0>-<192.5,22.0>> = 11.241478767626447

	* u1D4BB (U+1D4BB): L<<78.0,105.0>--<153.0,236.0>>/B<<153.0,236.0>-<132.0,214.0>-<116.0,198.5>> = 13.875819336765673

	* u1D4BD (U+1D4BD): L<<414.0,586.0>--<166.0,112.0>>/B<<166.0,112.0>-<256.0,213.0>-<309.0,261.0>> = 14.0850159536873

	* u1D4BD (U+1D4BD): L<<9.0,-6.0>--<139.0,236.0>>/B<<139.0,236.0>-<125.0,220.0>-<106.0,201.5>> = 12.94167409490862

	* u1D4BE (U+1D4BE): B<<111.5,190.5>-<123.0,210.0>-<135.0,229.0>>/B<<135.0,229.0>-<123.0,216.0>-<107.5,201.0>> = 10.433745642783816

	* u1D4BF (U+1D4BF): L<<-1.0,-5.0>--<135.0,229.0>>/B<<135.0,229.0>-<124.0,216.0>-<108.5,201.0>> = 10.071350503532525 

	* 38 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* u1D421 (U+1D421): L<<101.0,122.0>--<100.0,646.0>>

	* u1D421 (U+1D421): L<<252.0,309.0>--<253.0,118.0>>

	* u1D652 (U+1D652): L<<230.0,714.0>--<233.0,324.0>> 

	* u1D66C (U+1D66C): L<<198.0,546.0>--<200.0,304.0>> [code: found-semi-vertical]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 3 | 9 | 116 | 7 | 107 | 0 |
| 0% | 1% | 4% | 48% | 3% | 44% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
