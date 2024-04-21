// Get the input field and send button
const inputBox = document.getElementById('text-input');
const sendButton = document.getElementById('send-button');
const chatBox = document.getElementById("text-message-div"); // Use querySelector to select the first element with the specified class

// Function to fetch message
async function sendMessage() {
    try {
        const inputMessage = inputBox.value; // Get the current value of the input field
        const url = "/"; // Define the URL to send the POST request
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify(inputMessage), // Send inputMessage as JSON
            headers: {
                "Content-type": "application/json"
            }
        });

        const textJson = await response.text();
        console.log(`POST response: ${textJson}`);

        addToBox(textJson)

        // Clear the input field after sending the message
        inputBox.value = "";
    } catch (error) {
        console.log(error);
    }
}

function addToBox(textJson) {
    // Create a paragraph element for the text
    const text = JSON.parse(textJson);
    const paragraph = document.createElement('p');
    paragraph.textContent = text.response;

    // Set attributes to the paragraph element
    paragraph.style.fontFamily = "Arial";
    paragraph.style.backgroundColor = "#f0f0f0";
    paragraph.style.margin = "20px";
    paragraph.style.padding = "20px 10px";



    
    // Append the paragraph element to the chat box
    chatBox.appendChild(paragraph);
}


// Add event listener to the send button for click event
sendButton.addEventListener('click', sendMessage);

// Add event listener to the input field for keypress event
inputBox.addEventListener("keypress", function(event){
    if (event.key === "Enter") {
        // Prevent the default action of Enter key (e.g., form submission)
        event.preventDefault();
        // Trigger the click event of the send button
        sendButton.click();
    }
});

