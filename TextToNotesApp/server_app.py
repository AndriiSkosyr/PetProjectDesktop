from flask import Flask, request, jsonify
import summarizing_app


app = Flask(__name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    summarized_text = summarizing_app.summarize_text(text)
    return jsonify({'summarized_text': summarized_text})


if __name__ == '__main__':
    app.run()
