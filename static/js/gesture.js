const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const canvasCtx = canvasElement.getContext('2d');
const recButton = document.getElementById("snap")
const labelslider = document.getElementById("sliderlabel")
const slider = document.getElementById("yeppers")
const sendData = document.getElementById("send")

var data;

var labels = ['fist', 'face', 'corner', 'cup', 'circle', 'side', 'forward', 'checkmark']

function onResults(results) {
  canvasCtx.save();
  canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
  canvasCtx.drawImage(
      results.image, 0, 0, canvasElement.width, canvasElement.height);
  if (results.multiHandLandmarks) {
    for (const landmarks of results.multiHandLandmarks) {
      drawConnectors(canvasCtx, landmarks, HAND_CONNECTIONS,
                     {color: '#00FF00', lineWidth: 5});
      drawLandmarks(canvasCtx, landmarks, {color: '#FF0000', lineWidth: 2});
      data = landmarks
    }
  }
  canvasCtx.restore();
}

const hands = new Hands({locateFile: (file) => {
  return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});
hands.setOptions({
  maxNumHands: 2,
  modelComplexity: 1,
  minDetectionConfidence: 0.5,
  minTrackingConfidence: 0.5
});
hands.onResults(onResults);

const camera = new Camera(videoElement, {
  onFrame: async () => {
    await hands.send({image: videoElement});
  },
  width: 768,
  height: 432
});
camera.start();

slider.addEventListener('change', () => {
  labelslider.textContent = labels[slider.value]
})


labelslider.textContent = labels[slider.value]

function errorFunc(error){
  console.log("Error: " + error.responseText)
  alert("Error encountered... please try again")
}

sendData.addEventListener("click", () => {
  $.ajax({
    type: 'POST',
    url:'/gestures/savedata',
    success: function(data){
      if(!data['success']){
        alert("No hand data logged or sent")
      }
    },
    error: errorFunc
  })
})

recButton.addEventListener("click", () => {
  console.log(data)
  let mmyep = JSON.stringify(data)
  $.ajax({
      type: 'POST',
      url: '/gestures/save',
      data: {'points':mmyep, 'label':labels[slider.value]},
      success: function(data){
      },
      error: errorFunc
  });
})