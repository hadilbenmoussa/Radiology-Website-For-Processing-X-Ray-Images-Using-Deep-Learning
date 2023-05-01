function hideMessage() {
  var messageContainer = document.getElementById('message-container');
  setTimeout(function() {
    messageContainer.classList.add('hidden');
  }, 3000);
}

hideMessage();