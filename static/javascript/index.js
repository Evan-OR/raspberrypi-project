// cringe trick to get the URL lol
const urlElement = document.getElementById('url');
const SERVER_URL = urlElement.dataset.url;

const socket = io.connect(SERVER_URL);

let gTemperatureData = [[], []];
let gHumidityData = [[], []];
let gTemperatureChart = null;

let gGyroData = { roll: 0, pitch: 0, yaw: 0 };
let gGyroCalibratedRotation = { roll: 0, pitch: 0, yaw: 0 };

socket.on('connect', () => {
  console.log('Connected');
  createChart(gTemperatureData, gHumidityData);
});

socket.on('update_data', (response) => {
  // console.log(response);

  const gryoElement = document.getElementById('gyroData');
  gryoElement.innerText = Object.entries(response['gyroData'])
    .map(([key, value]) => `${key}: ${parseFloat(value).toFixed(4)}`)
    .join(', ');

  gGyroData = response['gyroData'];
  gTemperatureData = response['tempData'];
  gHumidityData = response['humidData'];
  createChart(gTemperatureData, gHumidityData);
});

document.getElementById('calButton').addEventListener('click', (e) => {
  gGyroCalibratedRotation = gGyroData;
  console.log('gGyroCalibratedRotation: ', gGyroCalibratedRotation);
});
