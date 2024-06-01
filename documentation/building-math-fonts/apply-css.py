import re
from pathlib import Path

CSS = """\
 <style>
  path {
   fill: black;
  }
  @media (prefers-color-scheme: dark) {
   path {
       fill: white;
   }
   path[stroke="#000"] {
    stroke: white;
   }
  }
 </style>"""

svgs = Path.glob(Path.cwd(), "*.svg")

for svg in svgs:
    text = svg.read_text()
    if "<style>" in text:
        text = re.sub(r" <style>.*.</style>", CSS, text, flags=re.DOTALL)
    else:
        text = re.sub(r"(<svg.*.>)", r"\1" + f"\n{CSS}", text)
    svg.write_text(text)
