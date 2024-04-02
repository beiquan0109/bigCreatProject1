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



    <h1>答案列表</h1>
    <div v-for="(item, index) in answers" :key="index">
      <p>{{ index + 1 }}. {{ item.answer }}</p>
      <p>赞数: {{ item.zan }}</p>
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
      }
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
/* 在这里添加样式 */
</style>
