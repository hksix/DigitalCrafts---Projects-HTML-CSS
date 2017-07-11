from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = """<style>
      table {
        width: 60%;
        border-top: 1px solid #333;
        border-left: 1px solid #333;
      }
      td {
        border-right: 1px solid #333;
        border-bottom: 1px solid #333;
        padding: 4px 8px;
      }
    </style>"""
    data = data + "<table cellpadding='0' cellspacing='0' border='0'>"
    for key in request.values:
      data = data + "<tr>"
      data = data + "<td>"
      data = data + key
      data = data + "</td>"
      data = data + "<td>"
      data = data + request.values[key]
      data = data + "</td>"
      data = data + "</tr>"
    data = data + "</table>"
    return data

if __name__ == "__main__":
    app.run()