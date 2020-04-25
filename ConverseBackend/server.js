const express = require('express');
const VoiceResponse = require('twilio').twiml.VoiceResponse;

const app = express();

// Firebase

var admin = require("firebase-admin");

var serviceAccount = require("./converse-hacknow-a6513-firebase-adminsdk-im6cm-9b7d8528e9");

admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: "https://converse-hacknow-a6513.firebaseio.com"
});

var ref = admin.database().ref('Node-client');
var messagesRef = ref.child('Test');

var messagesRef = messagesRef.push();
var messagesRef = messagesRef.push();
messagesRef.push({
    name: 'Shayaan',
    admin: true,
    count: 1,
    text: 'Hey guys'
});


// Create a route that will handle Twilio webhook requests, sent as an
// HTTP POST to /voice in our application
app.post('/voice', (request, response) => {
    // Use the Twilio Node.js SDK to build an XML response
    const twiml = new VoiceResponse();
    twiml.say({ voice: 'alice' }, 'hello world!');

    // Render the response as XML in reply to the webhook request
    response.type('text/xml');
    response.send(twiml.toString());
});

// Create an HTTP server and listen for requests on port 3000
app.listen(3000, () => {
    console.log(
        'Now listening on port 3000. ' +
        'Be sure to restart when you make code changes!'
    );
});