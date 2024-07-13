
const username = document.body.getAttribute('data-username');
console.log('Username: ', username);

document.getElementById('username').textContent = `User: ${username}`;

function getRoomName() {
    const params = new URLSearchParams(window.location.search);
    return params.get('room_name');
}

const roomName = getRoomName();
if (!roomName) {
    alert("Room name is required");
    window.location.href = "/login.html";
}
//Show the room name
document.getElementById('room-name-header').textContent = `Chat Room: ${roomName}`

let url = 'ws://' + window.location.host + '/ws/lobby/' + roomName + '/';

const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data)
    console.log('Data:', data)
    const message = data['message'];
    const messageUsername = data['username']

    if (messageUsername && message)
        document.querySelector('#chat-log').value += (messageUsername + ': ' + message + '\n');   
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly')
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) { 
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};  
