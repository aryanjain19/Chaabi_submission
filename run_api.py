from flask import Flask, request, jsonify
import llm_model


app = Flask(__name__)
@app.route('/query-engine')
def query_example():
    arg = request.args.get('query')
    query = str(arg)
    ans = llm_model.generate_ans(query)
    return(jsonify(ans))

if __name__ == '__main__':
    app.run(debug=True)

