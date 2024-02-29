from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/rss')
def get_rss():
    try:
        url = request.args.get('url')
        if not url:
            raise ValueError('URL parameter is missing.')

        # Fetch the RSS feed from the specified URL
        response = requests.get(url)
        feed_data = response.text

        # Set the appropriate headers
        headers = {'Content-Type': 'application/xml', 'Access-Control-Allow-Origin': '*'}

        # Return the fetched RSS feed data
        return (feed_data, 200, headers)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
