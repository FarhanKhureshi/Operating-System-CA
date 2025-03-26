from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to calculate FCFS
def fcfs(requests, start):
    seek_count = 0
    current_position = start
    movements = [start]
    for request in requests:
        seek_count += abs(request - current_position)
        current_position = request
        movements.append(request)
    avg_seek_time = seek_count / len(requests)
    return seek_count, avg_seek_time, movements

# Function to calculate SSTF
def sstf(requests, start):
    seek_count = 0
    current_position = start
    requests = sorted(requests)
    visited = [start]
    movements = [start]
    
    while requests:
        closest = min(requests, key=lambda x: abs(x - current_position))
        seek_count += abs(closest - current_position)
        current_position = closest
        requests.remove(closest)
        visited.append(closest)
        movements.append(closest)
    
    avg_seek_time = seek_count / len(visited)
    return seek_count, avg_seek_time, movements

# Function to calculate SCAN
def scan(requests, start, direction, max_track):
    seek_count = 0
    current_position = start
    requests = sorted(requests)
    movements = [start]

    # Move towards 0 if direction is left, otherwise move towards max_track
    if direction == "left":
        requests = [x for x in requests if x < start] + [x for x in requests if x > start]
    
    for request in requests:
        seek_count += abs(request - current_position)
        current_position = request
        movements.append(request)
    
    avg_seek_time = seek_count / len(requests)
    return seek_count, avg_seek_time, movements

# Function to calculate C-SCAN
def cscan(requests, start, direction, max_track):
    seek_count = 0
    current_position = start
    requests = sorted(requests)
    movements = [start]
    
    if direction == "left":
        requests = [x for x in requests if x < start] + [x for x in requests if x > start]
    
    for request in requests:
        seek_count += abs(request - current_position)
        current_position = request
        movements.append(request)
    
    avg_seek_time = seek_count / len(requests)
    return seek_count, avg_seek_time, movements

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    requests = list(map(int, data['requests'].split(',')))
    start = int(data['start'])
    algorithm = data['algorithm']
    max_track = int(data['max_track'])
    direction = data['direction']

    if algorithm == "FCFS":
        seek_count, avg_seek_time, movements = fcfs(requests, start)
    elif algorithm == "SSTF":
        seek_count, avg_seek_time, movements = sstf(requests, start)
    elif algorithm == "SCAN":
        seek_count, avg_seek_time, movements = scan(requests, start, direction, max_track)
    elif algorithm == "C-SCAN":
        seek_count, avg_seek_time, movements = cscan(requests, start, direction, max_track)

    response = {
        'seek_count': seek_count,
        'avg_seek_time': avg_seek_time,
        'movements': movements
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
