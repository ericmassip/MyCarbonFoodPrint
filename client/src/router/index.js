import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/components/MainPage'
import MapPage from '@/components/MapPage'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/map',
      name: 'MapPage',
      component: MapPage
    }
  ]
})