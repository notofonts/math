from fontTools.ttLib import TTFont
import glob

# The TTX file isn't necessarily sorted by our glyph order,
# so we have to sort it while applying
for fontfile in glob.glob("fonts/**/*.*tf", recursive=True):
    font = TTFont(fontfile)
    glyphmap = font.getReverseGlyphMap()

    font.importXML("sources/NotoSansMath-Regular-MATH-table.ttx")
    table = font["MATH"].table
    italic_correction = table.MathGlyphInfo.MathItalicsCorrectionInfo
    topaccents = table.MathGlyphInfo.MathTopAccentAttachment

    def fix_a_thing(coverage, things):
        items = list(zip(coverage.glyphs, things))
        items = sorted(items, key=lambda item: glyphmap.get(item[0]))
        coverage.glyphs = [item[0] for item in items]
        things[:] = [item[1] for item in items]


    fix_a_thing(italic_correction.Coverage, italic_correction.ItalicsCorrection)
    fix_a_thing(topaccents.TopAccentCoverage, topaccents.TopAccentAttachment)
    fix_a_thing(table.MathGlyphInfo.ExtendedShapeCoverage, table.MathGlyphInfo.ExtendedShapeCoverage.glyphs)
    fix_a_thing(table.MathVariants.VertGlyphCoverage, table.MathVariants.VertGlyphConstruction)
    fix_a_thing(table.MathVariants.HorizGlyphCoverage, table.MathVariants.HorizGlyphConstruction)

    font.save(fontfile)
    print("Applied math ttx to "+fontfile)
