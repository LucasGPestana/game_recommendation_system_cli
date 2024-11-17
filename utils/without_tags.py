import re

def getTextWithoutTags(text: str) -> str:

  tag_pattern = re.compile(r"\</?\w+\s*/?\>")

  return "".join(tag_pattern.split(text))