"""Read the .ta anchors from the glyphs source and
use this to update the TTX file."""
from glyphsLib import load
from fontTools.ttLib import TTFont


font = TTFont()
font.importXML("sources/NotoSansMath-Regular-MATH-table.ttx")
source = load("sources/NotoSansMath.glyphspackage")
topaccents = font["MATH"].table.MathGlyphInfo.MathTopAccentAttachment

coverage = topaccents.TopAccentCoverage.glyphs

for glyph in source.glyphs:
    layer = glyph.layers[0]
    anchor = layer.anchors["math.ta"]
    name = glyph.production
    if not anchor:
        continue
    if name not in coverage:
        print(f"{glyph.name} not in coverage table!")
        continue
    attachment = topaccents.TopAccentAttachment[coverage.index(name)]
    attachment.Value = anchor.position.x

font.saveXML("sources/NotoSansMath-Regular-MATH-table.ttx", tables=["MATH"])
