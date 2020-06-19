document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port); 
    var username = document.getElementById("script").getAttribute('data-username');
    var room = 'coding';
    join(room);
    console.log(username);

    document.getElementById("message").focus();
    document.querySelector('#message-box').onsubmit = SendMessage;
    
    rooms = document.querySelectorAll('.roomclass');
    for (i=0; i<rooms.length; i++) {
	rooms[i].addEventListener('click', function() {
	   room_change(this.innerHTML);
    	});
    };

    socket.on('display message', data =>{
	let message = document.createElement('p');
	if (data.user){
	    message.innerHTML = data.user + ':' + data.message;}
	else{
	    message.innerHTML = data.message;};
	console.log(message);
	document.querySelector('#textbox').append(message);
    });

    function SendMessage(){
        text = document.querySelector('#message').value;
	document.querySelector('#message').value = '';
	console.log(text);
        socket.emit('message to server', {'message':text, 'username':username});
	return false;
    }

    function room_change(new_room) {
	if(room == new_room)
	    console.log('Tried to change!')
	else{
	    leave(room);
	    join(new_room);
	    room = new_room;
	    document.querySelector('#textbox').innerHTML = '';
    }};
    
    function join(room) {
    	console.log(room)
    	socket.emit('join', {'room':room, 'username':username});
    }

    function leave(room) {
    	console.log(room);
    	socket.emit('leave', {'room':room, 'username':username});
    }

});
