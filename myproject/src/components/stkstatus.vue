<template>


  <div class="container">
    <!--  title  -->
    <div class="title">
      <h1>堆垛机后台数据</h1>
    </div>

    <!--  pos  -->
    <div class="chart-container">
      <div id="chart1"></div>
    </div>

    <!--currrent-->
    <div class="chart-container">
      <div id="chart2"></div>
    </div>
    <div class="chart-container">
      <div id="chart3"></div>
    </div>
    <div class="chart-container">
      <div id="chart4"></div>
    </div>
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

      // pos
      const chart1 = echarts.init(document.getElementById('chart1'));
      const pos_x = this.data.map(item => item.fields.pos_x);
      const pos_y = this.data.map(item => item.fields.pos_y);
      const pos_z = this.data.map(item => item.fields.pos_z);

      const option1 = {
        title: {
          text: 'Pos',
          left: 'center',
          top: 0
        },
        xAxis: {
          type: 'category',
          data: createTime,
        },
        yAxis: {
          type: 'value',
        },
        tooltip: {},
        legend: {
          orient: 'vertical',
          right: 0
        },
        dataZoom: [
          {
            type: 'inside'
          },
          {
            type: 'slider'
          }
        ],
        animation: false,
        series: [
          {
            name: 'pos x',
            type: 'scatter',
            data: pos_x,
            symbolSize: 3,
            itemStyle: {
              opacity: 0.4
            },
            large: true
          },
          {
            name: 'pos y',
            type: 'scatter',
            data: pos_y,
            symbolSize: 3,
            itemStyle: {
              opacity: 0.4
            },
            large: true
          },
          {
            name: 'pos z',
            type: 'scatter',
            data: pos_z,
            symbolSize: 3,
            itemStyle: {
              opacity: 0.4
            },
            large: true
          }
        ]
      };

      chart1.setOption(option1);


      // current

      const createTime = this.data.map(item => item.fields.createtime);
      const x_current = this.data.map(item => item.fields.x_current);
      const y_current = this.data.map(item => item.fields.y_current);
      const z_current = this.data.map(item => item.fields.z_current);

      // x current
      const chart2 = echarts.init(document.getElementById('chart2'));
      const option2 = {
        title: {
          text: 'X Current',
          left: 'center',
          top: 0
        },
        visualMap: {
          min: 150,
          max: -150,
          dimension: 1,
          orient: 'vertical',
          right: 0,
          top: 'center',
          text: ['HIGH', 'LOW'],
          calculable: true,
          inRange: {
            color: ['#f2c31a', '#24b7f2']
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: [
          {
            name: '',
            type: 'category',
            data: createTime,
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'x current',
            type: 'scatter',
            data: x_current,
            symbolSize: 5,
          }
        ]
      };
      chart2.setOption(option2);

      // y current
      const chart3 = echarts.init(document.getElementById('chart3'));
      const option3 = {
        title: {
          text: 'Y Current',
          left: 'center',
          top: 0
        },
        visualMap: {
          min: 150,
          max: -150,
          dimension: 1,
          orient: 'vertical',
          right: 0,
          top: 'center',
          text: ['HIGH', 'LOW'],
          calculable: true,
          inRange: {
            color: ['#000080', '#00FF7F']
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: [
          {
            name: '',
            type: 'category',
            data: createTime,
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'y current',
            type: 'scatter',
            data: y_current,
            symbolSize: 5,
          }
        ]
      };
      chart3.setOption(option3);

      // z current
      const chart4 = echarts.init(document.getElementById('chart4'));
      const option4 = {
        title: {
          text: 'Z Current',
          left: 'center',
          top: 0
        },
        visualMap: {
          min: 150,
          max: -150,
          dimension: 1,
          orient: 'vertical',
          right: 0,
          top: 'center',
          text: ['HIGH', 'LOW'],
          calculable: true,
          inRange: {
            color: ['#00008B', '#E0FFFF']
          }
        },
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'cross'
          }
        },
        xAxis: [
          {
            name: '',
            type: 'category',
            data: createTime,
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'z current',
            type: 'scatter',
            data: z_current,
            symbolSize: 5,
          }
        ]
      };
      chart4.setOption(option4);
    },
  },
};
</script>

<style scoped>
body {
  background: linear-gradient(to bottom, #003366, #66ccff); /* 从顶部到底部的渐变色 */
}



#chart1, #chart2, #chart3, #chart4 {
  height: 500px;
  width: 95%;
  padding: 20px;

  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.container {
  display: flex; /* 使用 flex 布局 */
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 20px;
}

.title {
  width: 100%;
}

.chart-container {
  width: 48%;
  margin-bottom: 20px;
}


</style>

