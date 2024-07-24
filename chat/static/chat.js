import websocketManager from '../../static/js/websocketManager';

// chat/static/chat.js
const username = document.body.getAttribute('data-username');
console.log('Username: ', username);

document.getElementById('username').textContent = `User: ${username}`;

const roomName = getRoomName();
if (!roomName) {
    alert("Room name is required");
    window.location.href = "/login.html";
}
//Show the room name
document.getElementById('room-name-header').textContent = `Chat Room: ${roomName}`

websocketManager.addHandler('chat_message', handleChatMessage);

function handleChatMessage(data) {
    const message = data['message'];
    const messageUserName = data['username'];
    console.log("handleChatMessage: " + message);
    console.log("handleChatMessage: " + messageUserName);
    console.log("handleChatMessage: " + data);
    if (messageUserName && message) {
        console.log("I am inside the if in the handleChatMessage");
        document.querySelector('#chat-log').value += (messageUserName + ': ' + message + '\n');
    }
}

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) { 
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    e.preventDefault();

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'type': 'chat_message',
        'message': message
    }));
    messageInputDom.value = '';
};

// # http://127.0.0.1:8000/chat/?user_select=felipe&private_chat_room=asdf


document.getElementById('private-chat-form').onsubmit = function(e) {
    e.preventDefault();
    
    const selectedUser = document.getElementById('user-select').value;
    const privateChatRoom = document.getElementById('private-chat-room').value;

    if (selectedUser && privateChatRoom) 
        window.location.href = `/chat/?room_name=$(privateChatRoom)`;
    else
        alert('Please select a user and enter a room name.');
}

function getRoomName() {
    const params = new URLSearchParams(window.location.search);
    return params.get('room_name');
}
