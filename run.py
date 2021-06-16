#! /usr/bin/env python

from app import app

if __name__ == "__main__":
    #certificate and key files
    # context = ('local.crt', 'local.key')

    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context='adhoc')