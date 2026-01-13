# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/about")
# def about():
#     return render_template("about.html")
#
# if __name__ == "__main__":
#     app.run(debug=True)


from nltk.corpus import stopwords
from nltk import word_tokenize
import string
from nltk.stem import PorterStemmer
# import nltk

# nltk.download('stopwords')

# print(stopwords.words('english'))

text = "This handout will help you understand how paragraphs are formed, how to develop stronger paragraphs, and how to completely and clearly express your ideas."
print(text)

stop_words = stopwords.words('english')

tokens = word_tokenize(text)

# filtered_words = []

filtered_setence = ""

for token in tokens:
    if token.lower() not in stop_words:
        # filtered_words.append(token)
        if len(filtered_setence) == 0:
            filtered_setence += token
        else:
            filtered_setence += " " + token

# print(filtered_words)

# print(filtered_setence)

cleaned_text = ''
for char in filtered_setence:
    if char not in string.punctuation:
        cleaned_text += char

# print(cleaned_text)

final_text = " ".join(cleaned_text.split())
final_text = final_text.lower()
# print(final_text)

tokens = word_tokenize(final_text)

stemmer = PorterStemmer()

final_text = ""
for token in tokens:
    if len(final_text) == 0:
        final_text += stemmer.stem(token)
    else:
        final_text += " " + stemmer.stem(token)

print(final_text)






# import string
#
# text = "Hello, world! Python is awesome :)"
#
# print(text)
#
# cleaned_text = ""
#
# for char in text:
#     if char not in string.punctuation:
#         cleaned_text += char
#
# print(cleaned_text)


# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
#
# text = "The running runner ran towards the happiest place easily."
#
# tokens = word_tokenize(text)
#
# stemmer = PorterStemmer()
#
# for token in tokens:
#     print(f"Original word: {token} \t|\t Stemmed: {stemmer.stem(token)}")








#
#
#
#
#
#
#
#
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
#
# # Sample sentence
# sentence = "The running runner ran towards the happiest place easily."
#
# # Tokenize the sentence
# words = word_tokenize(sentence)
#
# # Initialize the Porter Stemmer
# stemmer = PorterStemmer()
#
# # Apply stemming to each word
# stems = [stemmer.stem(word) for word in words]
#
# print("Original Sentence:")
# print(sentence)
#
# print("\nStemmed Sentence:")
# print(" ".join(stems))
#







































