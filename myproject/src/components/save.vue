<template>
  <div class="body_container">
    <h1>反馈保存</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="pinpai">品牌：</label>
        <input type="text" id="pinpai" v-model="formData.pinpai" required>
      </div>
      <div>
        <label for="xinghao">型号：</label>
        <input type="text" id="xinghao" v-model="formData.xinghao" required>
      </div>
      <div>
        <label for="errorid">报警信息：</label>
        <input type="text" id="errorid" v-model="formData.errorid" required>
      </div>
      <div>
        <label for="question">问题描述：</label>
        <textarea id="question" v-model="formData.question" required></textarea>
      </div>
      <div>
        <label for="selectedList">选中列表：</label>
        <input type="text" id="selectedList" v-model="selectedList" required>
      </div>
      <div>
        <label for="yuanyin">原因：</label>
        <input type="text" id="yuanyin" v-model="formData.yuanyin" required>
      </div>
      <div>
        <label for="answer">答案：</label>
        <textarea id="answer" v-model="formData.answer" required></textarea>
      </div>
      <button type="submit">提交</button>
    </form>
    <p v-if="message">{{ message }}</p>
    <router-link to="/pa" class="custom-link">问题提问</router-link>
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
                        yuanyin: '',
                        answer: ''
                    },
                    selectedList: '',
                    message: ''
                }
            },
            methods: {
                submitForm() {
                    // 将选中列表转换为数组
                    const selectedListArray = this.selectedList.split('|').filter(item => item.trim() !== '');
                    // 合并选中列表到表单数据中
                    this.formData.selectedList = selectedListArray;

                    // 构建查询参数字符串
                    const queryString = Object.keys(this.formData).map(key => {
                        return encodeURIComponent(key) + '=' + encodeURIComponent(this.formData[key]);
                    }).join('&');

                    // 向后端提交数据
                    fetch('http://127.0.0.1:8000/save?' + queryString)
                    .then(response => {
                        if (response.ok) {
                            return response.json();
                        } else {
                            throw new Error('Network response was not ok.');
                        }
                    })
                    .then(data => {
                        // 处理后端返回的数据
                        this.message = data.message;
                        this.$forceUpdate();
                    })
                    .catch(error => {
                        console.error('There was an error!', error);
                        this.message = '提交失败，请重试';
                    });
                }
            }
        };
    </script>

<style scoped>

.body_container {
  text-align: center;
}


h1 {
  color: black;
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 700;
  color: lightblue; /* Label color */
}

input[type="text"],
textarea {
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
