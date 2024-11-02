// cringe trick to get the URL lol
const urlElement = document.getElementById('url');
const SERVER_URL = urlElement.dataset.url;

const socket = io.connect(SERVER_URL);

let gTemperatureData = [[], []];
let gTemperatureChart = null;

const createChart = () => {
  const [xData, yData] = gTemperatureData;

  const ctx = document.getElementById('tempChart');

  if (gTemperatureChart) gTemperatureChart.destroy();

  gTemperatureChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: xData.map((time) => {
        const date = new Date(time);
        return `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
      }),
      datasets: [
        {
          label: 'temp',
          data: yData,
          borderWidth: 1,
        },
      ],
    },
    options: {
      animation: false,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
};

socket.on('connect', () => {
  console.log('Connected');
  createChart();
});

socket.on('update_data', (response) => {
  console.log(response['tempData']);

  gTemperatureData = response['tempData'];
  createChart();
});
