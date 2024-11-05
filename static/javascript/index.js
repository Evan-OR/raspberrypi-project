// cringe trick to get the URL lol
const urlElement = document.getElementById('url');
const SERVER_URL = urlElement.dataset.url;

const socket = io.connect(SERVER_URL);

let gTemperatureData = [[], []];
let gTemperatureChart = null;

let gGyroData = { x: 0, y: 0, z: 0 };
let gGyroCalibratedRotation = { x: 0, y: 0, z: 0 };

socket.on('connect', () => {
  console.log('Connected');
  createChart(gTemperatureData);
});

socket.on('update_data', (response) => {
  // console.log(response);

  const gryoElement = document.getElementById('gyroData');
  gryoElement.innerText = Object.entries(response['gyroData'])
    .map(([key, value]) => `${key}: ${parseFloat(value).toFixed(4)}`)
    .join(', ');

  gGyroData = response['gyroData'];
  gTemperatureData = response['tempData'];
  createChart(gTemperatureData);
});

document.getElementById('calButton').addEventListener('click', (e) => {
  gGyroCalibratedRotation = gGyroData;
  console.log('gGyroCalibratedRotation: ', gGyroCalibratedRotation);
});
