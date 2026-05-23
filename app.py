from flask import Flask, request, render_template_string, jsonify
import requests
import os
import time
import random
import threading

app = Flask(__name__)

AUTHOR = "Suraj Oberoy"
VERSION = "4.0 - HACKER EDITION"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>[Suraj Oberoy] HACKER TOOL v4.0</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #0a0a0a;
            min-height: 100vh;
            font-family: 'Courier New', 'Fira Code', monospace;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }
        
        /* Matrix Rain Effect */
        .matrix-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            opacity: 0.15;
            pointer-events: none;
        }
        
        .glitch {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(
                0deg,
                rgba(0, 255, 0, 0.03) 0px,
                rgba(0, 255, 0, 0.03) 2px,
                transparent 2px,
                transparent 4px
            );
            pointer-events: none;
            z-index: 1;
        }
        
        .container {
            max-width: 600px;
            margin: auto;
            background: rgba(0, 0, 0, 0.85);
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(0, 255, 0, 0.3), inset 0 0 20px rgba(0, 255, 0, 0.1);
            position: relative;
            z-index: 2;
            backdrop-filter: blur(5px);
        }
        
        /* ASCII Art */
        .ascii {
            color: #00ff00;
            font-size: 10px;
            line-height: 1;
            text-align: center;
            margin-bottom: 20px;
            text-shadow: 0 0 5px #00ff00;
            white-space: pre;
        }
        
        h1 {
            color: #00ff00;
            text-align: center;
            font-size: 24px;
            text-shadow: 0 0 10px #00ff00;
            letter-spacing: 3px;
            margin-bottom: 10px;
        }
        
        .owner {
            text-align: center;
            color: #ff00ff;
            font-size: 14px;
            margin-bottom: 20px;
            border-bottom: 1px solid #00ff00;
            padding-bottom: 10px;
            text-shadow: 0 0 5px #ff00ff;
        }
        
        .terminal-line {
            color: #00ff00;
            font-family: monospace;
            font-size: 12px;
            margin-bottom: 15px;
            border-left: 3px solid #00ff00;
            padding-left: 10px;
        }
        
        .form-label {
            color: #00ff00;
            display: block;
            margin-bottom: 5px;
            font-family: monospace;
            font-weight: bold;
            letter-spacing: 1px;
        }
        
        .form-control {
            width: 100%;
            padding: 10px;
            background: #000000;
            border: 1px solid #00ff00;
            color: #00ff00;
            font-family: monospace;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        
        .form-control:focus {
            outline: none;
            box-shadow: 0 0 10px #00ff00;
        }
        
        .btn {
            width: 100%;
            padding: 12px;
            background: transparent;
            border: 2px solid #00ff00;
            color: #00ff00;
            font-family: monospace;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .btn:hover {
            background: #00ff00;
            color: #000000;
            box-shadow: 0 0 20px #00ff00;
        }
        
        .btn-danger {
            border-color: #ff0000;
            color: #ff0000;
        }
        
        .btn-danger:hover {
            background: #ff0000;
            color: #000000;
            box-shadow: 0 0 20px #ff0000;
        }
        
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #00ff00;
            font-size: 11px;
            opacity: 0.7;
        }
        
        .blink {
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0; }
        }
        
        .status-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #000;
            border-top: 1px solid #00ff00;
            color: #00ff00;
            padding: 5px;
            text-align: center;
            font-size: 10px;
            z-index: 2;
            font-family: monospace;
        }
        
        select.form-control option {
            background: #000;
            color: #00ff00;
        }
        
        input[type="file"] {
            color: #00ff00;
        }
        
        ::-webkit-scrollbar {
            width: 8px;
            background: #000;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #00ff00;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="matrix-bg" id="matrix"></div>
    <div class="glitch"></div>
    
    <div class="container">
        <div class="ascii">
    ╔═══════════════════════════════════════╗
    ║  ░▒▓█ SURAJ OBEROY HACKER EDITION █▓▒░  ║
    ║  ═══════════════════════════════════   ║
    ║  [>] FACEBOOK MESSENGER EXPLOIT [<]    ║
    ║  [>] MODE: ADVANCED ATTACK [<]         ║
    ╚═══════════════════════════════════════╝
        </div>
        
        <h1>⚡ ROOT ACCESS GRANTED ⚡</h1>
        <div class="owner">🔥 EXPLOIT BY: SURAJ OBEROY 🔥</div>
        
        <div class="terminal-line">
            $ sudo ./messenger_attacker --init<br>
            <span style="color: #ff00ff">[+] Target system detected: Facebook Messenger</span><br>
            <span style="color: #ffff00">[+] Bypassing rate limits... READY</span>
        </div>
        
        <form action="/" method="post" enctype="multipart/form-data">
            <label class="form-label">>> TOKEN_TYPE:</label>
            <select class="form-control" name="tokenType" id="tokenType">
                <option value="single">[1] SINGLE_TOKEN_MODE</option>
                <option value="multi">[2] MULTI_TOKEN_MODE</option>
            </select>
            
            <div id="singleTokenDiv">
                <label class="form-label">>> ACCESS_TOKEN:</label>
                <input type="text" class="form-control" name="accessToken" placeholder="EAAB...">
            </div>
            
            <div id="multiTokenDiv" style="display:none;">
                <label class="form-label">>> TOKEN_FILE:</label>
                <input type="file" class="form-control" name="tokenFile" accept=".txt">
            </div>
            
            <label class="form-label">>> TARGET_THREAD_ID:</label>
            <input type="text" class="form-control" name="threadId" placeholder="[+] Enter conversation ID" required>
            
            <label class="form-label">>> PREFIX_NAME:</label>
            <input type="text" class="form-control" name="kidx" placeholder="[+] Hacker name">
            
            <label class="form-label">>> MESSAGE_PAYLOAD_FILE:</label>
            <input type="file" class="form-control" name="txtFile" accept=".txt" required>
            
            <label class="form-label">>> DELAY (SECONDS):</label>
            <input type="number" step="0.1" class="form-control" name="time" placeholder="0.5 - 10" required>
            
            <button type="submit" class="btn">🚀 EXECUTE_ATTACK 🚀</button>
        </form>
        
        <footer class="footer">
            <span class="blink">█</span> SURAJ OBEROY SECURITY FORCE <span class="blink">█</span><br>
            [!] FOR EDUCATIONAL PURPOSES ONLY [!]
        </footer>
    </div>
    
    <div class="status-bar">
        [SYSTEM] Online | SURAJ OBEROY HACKER EDITION v4.0 | Ready for attack
    </div>

    <script>
        document.getElementById('tokenType').addEventListener('change', function() {
            var isMulti = this.value === 'multi';
            document.getElementById('singleTokenDiv').style.display = isMulti ? 'none' : 'block';
            document.getElementById('multiTokenDiv').style.display = isMulti ? 'block' : 'none';
        });
        
        // Matrix Rain Effect
        function createMatrix() {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const matrixDiv = document.getElementById('matrix');
            canvas.style.width = '100%';
            canvas.style.height = '100%';
            canvas.style.position = 'absolute';
            matrixDiv.appendChild(canvas);
            
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            const chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン";
            const fontSize = 14;
            const columns = canvas.width / fontSize;
            const drops = [];
            
            for(let i = 0; i < columns; i++) {
                drops[i] = Math.random() * canvas.height / fontSize;
            }
            
            function draw() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#00ff00';
                ctx.font = fontSize + 'px monospace';
                
                for(let i = 0; i < drops.length; i++) {
                    const char = chars[Math.floor(Math.random() * chars.length)];
                    ctx.fillText(char, i * fontSize, drops[i] * fontSize);
                    
                    if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }
            
            setInterval(draw, 50);
        }
        
        createMatrix();
        
        window.addEventListener('resize', () => {
            location.reload();
        });
    </script>
</body>
</html>
''')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
