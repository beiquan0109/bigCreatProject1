import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import pa from "../components/pa.vue";
import save from "../components/save.vue";
import login from "../components/login.vue";
import stkstatus from "../components/stkstatus.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      // path: '/',
      // name: 'pa',
      // component: pa
      // path: '/',
      // // name: 'HelloWorld',
      // name: 'Home',
      // // component: HelloWorld
      // component: Home

      path: '/save',
      name: 'save',
      component: save
    },
    {
      path: '/pa',
      name: 'pa',
      component: pa
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/stkstatus',
      name: 'stkstatus',
      component: stkstatus
    }
  ]
})
