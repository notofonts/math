## Fontbakery report

Fontbakery version: 0.8.10

<details><summary><b>[6] NotoSansMath-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni210A	Contours detected: 3	Expected: 2

	- Glyph name: uni210D	Contours detected: 3	Expected: 2

	- Glyph name: uni2119	Contours detected: 4	Expected: 2

	- Glyph name: uni211A	Contours detected: 5	Expected: 3

	- Glyph name: uni211D	Contours detected: 5	Expected: 3

	- Glyph name: uni21C7	Contours detected: 2	Expected: 1

	- Glyph name: uni21C8	Contours detected: 2	Expected: 1

	- Glyph name: uni21C9	Contours detected: 2	Expected: 1 

	- And 22 more.

Use -F or --full-lists to disable shortening of long lists.
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check mark characters are in GDEF mark glyph class. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_mark_chars">com.google.fonts/check/gdef_mark_chars</a>)</summary><div>


* ⚠ **WARN** The following mark characters could be in the GDEF mark glyph class:
	 acutecomb (U+0301), gravecomb (U+0300), uni0304 (U+0304), uni0306 (U+0306), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0312 (U+0312), uni0326 (U+0326), uni0327 (U+0327) and uni0328 (U+0328) [code: mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* u1D468 (U+1D468): L<<509.0,687.0>--<486.0,132.0>> -> L<<486.0,132.0>--<486.0,118.0>>

	* u1D612 (U+1D612): L<<207.0,367.0>--<269.0,433.0>> -> L<<269.0,433.0>--<543.0,714.0>>

	* u1D646 (U+1D646): L<<251.0,369.0>--<327.0,471.0>> -> L<<327.0,471.0>--<529.0,714.0>>

	* u1D6AC (U+1D6AC): L<<607.0,-11.0>--<370.0,0.0>> -> L<<370.0,0.0>--<180.0,0.0>>

	* u1D6B3 (U+1D6B3): L<<446.0,0.0>--<329.0,301.0>> -> L<<329.0,301.0>--<232.0,534.0>>

	* u1D6C8 (U+1D6C8): L<<241.0,395.0>--<241.0,313.0>> -> L<<241.0,313.0>--<244.0,39.0>>

	* u1D6F2 (U+1D6F2): L<<105.0,3.0>--<220.0,568.0>> -> L<<220.0,568.0>--<224.0,607.0>>

	* u1D720 (U+1D720): L<<554.0,-11.0>--<320.0,0.0>> -> L<<320.0,0.0>--<130.0,0.0>> 

	* And u1D741 (U+1D741): L<<381.0,113.0>--<411.0,243.0>> -> L<<411.0,243.0>--<444.0,438.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* u1D44E (U+1D44E): B<<250.0,34.0>-<250.0,64.0>-<284.0,175.0>>/B<<284.0,175.0>-<227.0,81.0>-<177.5,34.5>> = 14.20175277562993

	* u1D451 (U+1D451): B<<272.0,40.0>-<272.0,79.0>-<300.0,167.0>>/B<<300.0,167.0>-<247.0,76.0>-<198.0,32.0>> = 12.567149737454237

	* u1D485 (U+1D485): B<<234.0,52.0>-<234.0,80.0>-<244.0,113.0>>/B<<244.0,113.0>-<206.0,49.0>-<168.0,17.5>> = 13.841323783076136

	* u1D493 (U+1D493): L<<225.0,461.0>--<170.0,281.0>>/B<<170.0,281.0>-<194.0,328.0>-<215.0,362.0>> = 10.05977371509991

	* u1D4B0 (U+1D4B0): B<<641.0,67.0>-<641.0,93.0>-<678.0,177.0>>/B<<678.0,177.0>-<600.0,68.0>-<555.0,30.0>> = 11.815021751769102

	* u1D4B1 (U+1D4B1): B<<436.5,427.0>-<466.0,469.0>-<511.0,524.0>>/B<<511.0,524.0>-<473.0,494.0>-<442.0,472.5>> = 12.420429945256531

	* u1D4B2 (U+1D4B2): B<<473.0,190.0>-<409.0,130.0>-<316.0,57.0>>/B<<316.0,57.0>-<392.0,96.0>-<470.0,155.0>> = 10.965022634453765

	* u1D4B2 (U+1D4B2): L<<780.0,411.0>--<869.0,530.0>>/B<<869.0,530.0>-<851.0,512.0>-<830.0,488.0>> = 8.207216411918077

	* u1D4B4 (U+1D4B4): B<<589.0,294.5>-<610.0,330.0>-<631.0,365.0>>/B<<631.0,365.0>-<560.0,278.0>-<516.0,246.0>> = 8.253851145562376

	* u1D4B6 (U+1D4B6): B<<266.0,51.0>-<266.0,82.0>-<279.0,108.0>>/B<<279.0,108.0>-<200.0,-6.0>-<125.0,-6.0>> = 8.156229018789725 

	* And 47 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* u1D47E (U+1D47E): L<<118.0,-17.0>--<122.0,536.0>>

	* u1D57B (U+1D57B): L<<229.0,193.0>--<228.0,508.0>>

	* u1D57B (U+1D57B): L<<363.0,532.0>--<364.0,151.0>>

	* u1D652 (U+1D652): L<<230.0,714.0>--<233.0,324.0>>

	* u1D66C (U+1D66C): L<<198.0,546.0>--<200.0,304.0>>

	* u1D6AA (U+1D6AA): L<<261.0,538.0>--<260.0,326.0>>

	* u1D6AC (U+1D6AC): L<<515.0,339.0>--<285.0,340.0>>

	* u1D6B3 (U+1D6B3): L<<965.0,649.0>--<964.0,427.0>>

	* u1D6B5 (U+1D6B5): L<<530.0,595.0>--<195.0,597.0>>

	* u1D6B7 (U+1D6B7): L<<266.0,584.0>--<264.0,290.0>> 

	* And 11 more.

Use -F or --full-lists to disable shortening of long lists. [code: found-semi-vertical]
</div></details><br></div></details>
### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 6 | 111 | 7 | 103 | 0 |
| 0% | 0% | 3% | 49% | 3% | 45% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
