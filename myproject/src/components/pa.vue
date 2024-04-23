<template>
  <div>
    <h1>参数提交表单</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="pinpai">品牌：</label>
        <input type="text" id="pinpai" v-model="formData.pinpai">
      </div>
      <div>
        <label for="xinghao">型号：</label>
        <input type="text" id="xinghao" v-model="formData.xinghao">
      </div>
      <div>
        <label for="errorid">报警ID：</label>
        <input type="text" id="errorid" v-model="formData.errorid">
      </div>
      <div>
        <label for="question">问题描述：</label>
        <input type="text" id="question" v-model="formData.question">
      </div>
      <div>
        <label for="relationList">相关列表：</label>
        <input type="text" id="relationList" v-model="formData.relationListtmp">
      </div>
      <button type="submit">提交</button>
    </form>



    <h1 v-if="answers.length > 0">答案列表</h1>
    <div v-if="answers.length > 0" class="table-container">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>答案</th>
            <th>赞数</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in answers" :key="index">
            <!-- 序号列 -->
            <td>{{ index + 1 }}</td>
            <td>{{ item.answer }}</td>
            <td>{{ item.zan }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div>
      <router-link to="/save" class="custom-link">保存反馈</router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        pinpai: '',
        xinghao: '',
        errorid: '',
        question: '',
        relationListtmp: ''
      },
       answers: []
    };
  },
  methods: {
    submitForm() {
      // 构建查询字符串
      const queryString = `pinpai=${encodeURIComponent(this.formData.pinpai)}&xinghao=${encodeURIComponent(this.formData.xinghao)}&errorid=${encodeURIComponent(this.formData.errorid)}&question=${encodeURIComponent(this.formData.question)}&relationList=${encodeURIComponent(this.formData.relationListtmp)}`;

      // 构建完整的 URL
      const url = `http://127.0.0.1:8000/pa?${queryString}`; // 注意 URL 格式

       fetch(url, {
        method: 'GET'
      })
      .then(response => response.json())
      .then(data => {
        // 将从后端获取的数据赋值给 answers 数组

          //
          this.answers = data.answer;
          console.log("success");
          console.log(this.answers);
          this.$forceUpdate();
      })
      .catch(error => {
        console.error('Error:', error);
      });

    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
}
h1{
  color: rgb(85,130,124);
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 700;
  color: #4CAF50; /* Label color */
}

input[type="text"] {
  width: calc(100% / 5); /* Set input width to occupy one-fifth of page width */
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 4px;

}

button[type="submit"] {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
}

button[type="submit"]:hover {
  background-color: #45a049;
}


table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

.table-container {
  width: calc(100% / 2); /* 页面宽度的三分之一 */
  margin: 0 auto; /* 居中 */
  //display: none; /* 隐藏答案表格 */
}

.custom-link {
  color: #007bff; /* 设置颜色为浅蓝色 */
  text-decoration: none; /* 移除下划线 */
  box-shadow: 0 2px 4px rgba(0, 123, 255, 0.3); /* 添加投影效果 */
  padding: 5px 10px; /* 调整内边距以增加按钮大小 */
}

.custom-link:hover {
  opacity: 0.8; /* 鼠标悬停时的透明度 */
}
</style>
