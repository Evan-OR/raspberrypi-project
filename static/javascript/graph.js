const createChart = (tempData) => {
  const [xData, yData] = tempData;

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
      plugins: {
        title: {
          display: true,
          text: 'Temperature Graph',
        },
      },
      animation: false,
      scales: {
        y: {
          title: { display: true, text: 'Temperature' },
        },
        x: {
          title: { display: true, text: 'Time' },
        },
      },
    },
  });
};
