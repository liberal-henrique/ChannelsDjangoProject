import webSocketManager from "../../static/js/websocketManager.js"

const roomName = getRoomName();
document.getElementById('room-name-header').textContent = `Game Room: ${roomName}`

// const gameSocket = new WebSocket(
//     'ws://' + window.location.host + '/ws/game/' + roomName + '/'
// );

webSocketManager.addHandler('initial_settings', hadleInitialSettings);
webSocketManager.addHandler('game_update', handleGameUpdate);

function hadleInitialSettings(data) {
    const settings = data.settings;
    //Esse é o lugar onde receberemos o número de players.
}

function handleGameUpdate(data) {
    const paddlePosition = data.paddle_position;
    const ballPosition = data.ball_position;
    const ballSpeed = data.ball_speed;
    const ballDirection = data.ball_direction;

    if (ballPosition !== undefined 
        && ballSpeed !== undefined
        && ballDirection !== undefined
    ) {
        console.log("Message from Host");
        updateGame(paddlePosition, ballPosition, ballSpeed, ballDirection);
    } else {
        console.log('Message from player');
        updateGame(paddlePosition);
    }
}

function updateGame(
    paddlePosition, 
    ballPosition = null, 
    ballSpeed = null, 
    ballDirection = null) 
{
    const paddle = document.getElementById('paddle');
    paddle.style.left = `${paddlePosition.x}px`;
    paddle.style.top = `${paddlePosition.y}px`;

    if (ballPosition) {
        const ball = document.getElementById('ball');
        ball.style.left = `${ballPosition.x}px`;
        ball.style.top = `${ballPosition.y}px`;
        ball.speed = ballSpeed;
        ball.direction = ballDirection;
    }
}

function sendGameUpdate(
    paddlePosition, 
    ballPosition = null, 
    ballSpeed = null, 
    ballDirection = null) 
{
    const message = {
        'type': 'game_update',
        'paddle_position': paddlePosition
    };

    if (ballPosition !== null && ballSpeed != null && ballDirection != null) {
        message['ball_position'] = ballPosition;
        message['ball_speed'] = ballSpeed;
        message['ball_direction'] = ballDirection;
    }
    webSocketManager.send(JSON.stringify(message));
}

function getRoomName() {
    const params = new URLSearchParams(window.location.search);
    return params.get('room_name');
}