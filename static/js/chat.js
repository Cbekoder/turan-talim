document.addEventListener('DOMContentLoaded', function() {
  const messageInput = document.querySelector('.message-input');
  const sendButton = document.querySelector('.send-button');
  const chatMessages = document.querySelector('.chat-messages');

  sendButton.addEventListener('click', function() {
    const userMessage = messageInput.value;
    if (userMessage.trim() !== '') {
      sendMessageToAI(userMessage);
      displayUserMessage(userMessage);
      messageInput.value = '';
    }
  });

  function displayUserMessage(message) {
    const userMessageContainer = document.createElement('div');
    userMessageContainer.classList.add('message-container');

    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');

    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
    messageContent.textContent = message;

    userMessage.appendChild(messageContent);
    userMessageContainer.appendChild(userMessage);
    chatMessages.appendChild(userMessageContainer);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function displayAIResponse(response) {
    const aiMessageContainer = document.createElement('div');
    aiMessageContainer.classList.add('message-container');

    const aiMessage = document.createElement('div');
    aiMessage.classList.add('message', 'ai-message');

    const avatar = document.createElement('div');
    avatar.classList.add('avatar');
    const avatarImg = document.createElement('img');
    avatarImg.src = "{% static 'img/logo.png' %}";
    avatarImg.alt = "AI Avatar";
    avatar.appendChild(avatarImg);

    const messageContent = document.createElement('div');
    messageContent.classList.add('message-content');
    messageContent.textContent = response;

    aiMessage.appendChild(avatar);
    aiMessage.appendChild(messageContent);
    aiMessageContainer.appendChild(aiMessage);
    chatMessages.appendChild(aiMessageContainer);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function sendMessageToAI(message) {
    // Send the message to the Python backend
    fetch('/send-to-ai/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
      },
      body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
      // Display the AI's response
      displayAIResponse(data.response);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
});