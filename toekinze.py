# import re

# text = "My name is jil from marque columbia he's isn't from delhi"
# # tokens = text.split()
# # repr() ~ r treats the string as object(raw) string 
# tokens = re.findall(r'\b\w+\b',text)
# print(tokens)
#word tokenization
import nltk
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize,sent_tokenize

text = "Don't stop beleving isn't, hold on to that feeling. He's an alien!Unbeliveable"
print(word_tokenize(text))
print(sent_tokenize(text))