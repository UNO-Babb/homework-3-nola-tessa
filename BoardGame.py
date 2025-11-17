from flask import Flask, render_template_string
import random

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Enhanced Math Game</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(to right, red, green);
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
        }
        #game {
            padding: 20px;
            border-radius: 20px;
            background: rgba(0,0,0,0.4);
            width: 90%;
            max-width: 500px;
            animation: fadeIn 1s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }
        .answer {
            background: white;
            color: black;
            margin: 10px;
            padding: 15px;
            font-size: 2em;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.2s ease, background 0.2s;
        }
        .answer:hover {
            transform: scale(1.1);
            background: yellow;
        }
        #difficulty, #mode {
            font-size: 1.2em;
            margin: 10px;
        }
        #playAgain {
            display: none;
            margin-top: 20px;
            padding: 15px;
            background: orange;
            color: black;
            border-radius: 10px;
            font-size: 1.5em;
            cursor: pointer;
            transition: 0.2s;
        }
        #playAgain:hover {
            transform: scale(1.1);
            background: gold;
        }
    </style>
</head>
<body>

<div id='game'>
    <h2>Difficulty:</h2>
    <select id='difficulty'>
        <option value='easy'>Easy</option>
        <option value='medium'>Medium</option>
        <option value='hard'>Hard</option>
    </select>

    <h2>Mode:</h2>
    <select id='mode'>
        <option value='add'>Addition</option>
        <option value='sub'>Subtraction</option>
        <option value='mul'>Multiplication</option>
        <option value='mix'>Mixed</option>
    </select>

    <h1 id='question'></h1>
    <div id='answers'></div>

    <h2 id='score'>Score: 0</h2>
    <h2 id='lives'>Lives: 3</h2>
    <h2 id='highscore'>High Score: 0</h2>

    <button id="playAgain" onclick="restartGame()">Play Again</button>
</div>

<script>
    let score = 0;
    let lives = 3;
    let highscore = 0;

    const difficultyLevels = {
        easy: 10,
        medium: 20,
        hard: 50
    };

    function generateQuestion() {
        let diff = document.getElementById("difficulty").value;
        let mode = document.getElementById("mode").value;
        let max = difficultyLevels[diff];

        let a = Math.floor(Math.random() * max);
        let b = Math.floor(Math.random() * max);

        let operator = "+";
        let correct;

        if (mode === "add") {
            correct = a + b;
        } else if (mode === "sub") {
            correct = a - b;
            operator = "-";
        } else if (mode === "mul") {
            correct = a * b;
            operator = "×";
        } else {
            const ops = ["+", "-", "×"];
            operator = ops[Math.floor(Math.random()*3)];
            correct = operator === "+" ? a+b : operator === "-" ? a-b : a*b;
        }

        document.getElementById("question").textContent = `${a} ${operator} ${b} = ?`;

        let wrong1 = correct + Math.floor(Math.random()*4 + 1);
        let wrong2 = correct - Math.floor(Math.random()*4 + 1);

        let options = [correct, wrong1, wrong2].sort(() => Math.random() - 0.5);

        let answersDiv = document.getElementById("answers");
        answersDiv.innerHTML = "";

        options.forEach(num => {
            let btn = document.createElement("div");
            btn.className = "answer";
            btn.textContent = num;
            btn.onclick = () => checkAnswer(num, correct);
            answersDiv.appendChild(btn);
        });
    }

    function checkAnswer(choice, correct) {
        if (choice === correct) {
            score++;
        } else {
            lives--;
        }

        if (score > highscore) highscore = score;

        document.getElementById("score").textContent = `Score: ${score}`;
        document.getElementById("lives").textContent = `Lives: ${lives}`;
        document.getElementById("highscore").textContent = `High Score: ${highscore}`;

        if (lives <= 0) {
            gameOver();
            return;
        }

        generateQuestion();
    }

    function gameOver() {
        document.getElementById("question").textContent = "Game Over!";
        document.getElementById("answers").innerHTML = "";
        document.getElementById("playAgain").style.display = "inline-block";
    }

    function restartGame() {
        score = 0;
        lives = 3;

        document.getElementById("score").textContent = "Score: 0";
        document.getElementById("lives").textContent = "Lives: 3";
        document.getElementById("playAgain").style.display = "none";

        generateQuestion();
    }

    generateQuestion();
</script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
