from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from database import get_db, init_db
import os

app = Flask(__name__, 
           static_folder='/mnt/c/Users/matth/Documents/Coding/opencode/static',
           template_folder='/mnt/c/Users/matth/Documents/Coding/opencode/templates')
CORS(app)

init_db()

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('../static', filename)

@app.route('/api/<username>', methods=['GET'])
def get_user_data(username):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if not user:
        cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        
        for i in range(1, 25):
            cursor.execute('INSERT INTO button_states (username, button_number, is_on) VALUES (?, ?, ?)', 
                         (username, i, False))
        conn.commit()
    
    cursor.execute('SELECT button_number, is_on FROM button_states WHERE username = ?', (username,))
    button_states = {row['button_number']: bool(row['is_on']) for row in cursor.fetchall()}
    
    conn.close()
    
    return jsonify({
        'username': username,
        'button_states': button_states
    })

@app.route('/api/<username>', methods=['POST'])
def update_button_state(username):
    data = request.json
    if not data:
        return jsonify({'error': 'JSON data is required'}), 400
    
    button_number = data.get('button_number')
    is_on = data.get('is_on')
    
    if not button_number or is_on is None:
        return jsonify({'error': 'button_number and is_on are required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO button_states (username, button_number, is_on)
        VALUES (?, ?, ?)
    ''', (username, button_number, is_on))
    
    conn.commit()
    conn.close()
    
    return jsonify({'success': True})

@app.route('/api/<username>', methods=['DELETE'])
def delete_user(username):
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM button_states WHERE username = ?', (username,))
        cursor.execute('DELETE FROM users WHERE username = ?', (username,))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/overview', methods=['GET'])
def get_overview():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT username FROM users ORDER BY username')
    users = cursor.fetchall()
    
    overview_data = {}
    for user in users:
        username = user['username']
        cursor.execute('SELECT button_number, is_on FROM button_states WHERE username = ?', (username,))
        button_states = {row['button_number']: bool(row['is_on']) for row in cursor.fetchall()}
        
        total_kilometers = sum(day for day, is_on in button_states.items() if is_on)
        
        overview_data[username] = {
            'button_states': button_states,
            'completed_days': sum(1 for is_on in button_states.values() if is_on),
            'kilometers': total_kilometers
        }
    
    conn.close()
    
    return jsonify(overview_data)

@app.route('/<username>')
def user_page(username):
    return render_template('user.html', username=username)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview_page():
    return render_template('overview.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)