<template>
  <div>
    <div id="chart1"></div>
    <div id="chart2"></div>
  </div>
</template>

<script>
import * as echarts from "echarts"

export default {
  data() {
    return {
      data: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      fetch('http://127.0.0.1:8000/api/stkstatus')
        .then(response => response.json())
        .then(data => {
          // console.log('Data from backend:', data);
          this.data = data;
          this.renderCharts();
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    renderCharts() {
      // console.log(this.data);
      this.data = JSON.parse(this.data);

      if (Array.isArray(this.data)) {
        // 在这里执行.map()操作
      } else {
        console.error('this.data is not an array');
      }

      // 渲染折线图1
      const chart1 = echarts.init(document.getElementById('chart1'));
      const xAxisData = this.data.map(item => item.fields.createtime);
      const seriesData1 = this.data.map(item => item.fields.x_current);
      const seriesData2 = this.data.map(item => item.fields.y_current);
      const seriesData3 = this.data.map(item => item.fields.z_current);
      const option1 = {
        xAxis: {
          type: 'category',
          data: xAxisData,
        },
        yAxis: {
          type: 'value',
        },
        series: [{
          name: 'x_current',
          type: 'scatter',
          data: seriesData1,
        }, {
          name: 'y_current',
          type: 'scatter',
          data: seriesData2,
        }, {
          name: 'z_current',
          type: 'scatter',
          data: seriesData3,
        }],
      };
      chart1.setOption(option1);

      // 渲染折线图2
      const chart2 = echarts.init(document.getElementById('chart2'));
      const seriesData4 = this.data.map(item => item.fields.pos_x);
      const seriesData5 = this.data.map(item => item.fields.pos_y);
      const seriesData6 = this.data.map(item => item.fields.pos_z);
      const option2 = {
        xAxis: {
          type: 'category',
          data: xAxisData,
        },
        yAxis: {
          type: 'value',
        },
        series: [{
          name: 'pos_x',
          type: 'scatter',
          data: seriesData4,
        }, {
          name: 'pos_y',
          type: 'scatter',
          data: seriesData5,
        }, {
          name: 'pos_z',
          type: 'scatter',
          data: seriesData6,
        }],
      };
      chart2.setOption(option2);
    },
  },
};
</script>

<style scoped>
#chart1, #chart2 {
  width: 1500px;
  height: 800px;
  margin-bottom: 20px;
}
</style>

