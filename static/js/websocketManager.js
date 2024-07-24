//static/js/websocketManager.js

class websocketManager {
    constructor(url, handlers) {
        if (websocketManager.instance) {
            return websocketManager.instance;
        }
        this.url = url;
        this.socket = new WebSocket(url);
        this.handlers = handlers;


        this.socket.onmessage = this.onMessage.bind(this);
        this.socket.onopen = this.onOpen.bind(this);
        this.socket.onclose = this.onClose.bind(this);

        websocketManager.instance = this;
    }

    onOpen() {
        console.log("Websocket conn")
    }

    onMessage(event) {
        const data = JSON.parse(event.data);
        const handler = this.handlers[data.type];
        
        console.log("websocketManager: " + data);

        if (handler)
            handler(data);
        else
            console.warn(`No handlers for message type: ${data.type}`);
    }

    onClose() {
        console.error('WebSockets connection closed');
    }

    send(message) {
        this.socket.send(JSON.stringify(message));
    }

    addHandler(type, handler) {
        this.handlers[type] = handler;
    }

    removeHandler(type) {
        delete this.handlers[type];
    }
}

function getRoomName() {
    const params = new URLSearchParams(window.location.search);
    return params.get('room_name');
}

const webSocketManagerInstance = new WebSocketManager('ws://' + window.location.host + '/ws/chat/' + getRoomName() + '/');
    
export default webSocketManagerInstance;
