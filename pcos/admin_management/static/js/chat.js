
// Chatbot toggle function
// function toggleChatbot() {
//     const chatbot = document.getElementById('chatbot');
//     chatbot.style.display = chatbot.style.display === 'none' ? 'block' : 'none';
// }

// function sendMessage() {
//     const userInput = document.getElementById('user-input').value;
//     const chatMessages = document.getElementById('chat-messages');
//     const userMessage = `<div class="message user-message">${userInput}</div>`;
//     chatMessages.innerHTML += userMessage
//     // You would add actual chatbot response handling here
//     const botResponse = `<div class="message bot-message">Thank you for your question! I'm here to help.</div>`;
//     chatMessages.innerHTML += botResponse
//     document.getElementById('user-input').value = ''; // Clear input
// }



// $(document).ready(function() {
//     $('#user-input-form').on('submit', function(event) {
//         event.preventDefault();
//         var user_input = $('#user-input').val();
//         var csrftoken = $('[name=csrfmiddlewaretoken]').val();

//         if (user_input.trim() !== '') {
//             $('#user-input').val('');
//             appendUserMessage(user_input);

//             $.ajax({
//                 type: 'POST',
//                 url: '{% url 'chats' %}',
//                 data: {
//                     user_input: user_input,
//                     csrfmiddlewaretoken: csrftoken
//                 },
//                 success: function(response) {
//                     appendChatbotMessage(response.response_text);
//                 },
//                 error: function(xhr, status, error) {
//                     console.error('AJAX Error:', error);
//                 }
//             });
//         }
//     });

//     function appendUserMessage(message) {
//         var messageElement = $('<div class="message user-message"><div class="message-content"><div class="message-text"></div></div></div>').text(message);
//         $('#chat-container').append(messageElement);
//         scrollChatToBottom();
//     }

//     function appendChatbotMessage(message) {
//         var messageElement = $('<div class="message chatbot-message"><div class="message-content"><div class="message-text"></div></div></div>').text(message);
//         $('#chat-container').append(messageElement);
//         scrollChatToBottom();
//     }

//     function scrollChatToBottom() {
//         $('#chat-container').scrollTop($('#chat-container')[0].scrollHeight);
//     }
// });

