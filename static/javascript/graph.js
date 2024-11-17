const createChart = (chartData, chartId, chartLabel) => {
  const [xData, yData] = chartData;

  const ctx = document.getElementById(chartId);

  if (window[chartId]) window[chartId].destroy();

  window[chartId] = new Chart(ctx, {
    type: 'line',
    data: {
      labels: xData.map((time) => {
        const date = new Date(time);
        return `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
      }),
      datasets: [
        {
          label: chartLabel,
          data: yData,
          borderColor: chartLabel === 'Temperature' ? '#f2960c' : '#00bbff',
          backgroundColor: chartLabel === 'Temperature' ? '#ffb74a' : '#4acfff',
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: {
        title: {
          display: true,
          text: `${chartLabel} Graph`,
        },
      },
      animation: false,
      scales: {
        y: {
          title: { display: true, text: chartLabel },
        },
        x: {
          title: { display: true, text: 'Time' },
        },
      },
    },
  });
};
