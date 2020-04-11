import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import BootstrapVue from "bootstrap-vue/dist/bootstrap-vue.esm";
import Vue from "vue";
import App from "./App.vue";
import router from "./router/index";
import VueSvgGauge from "vue-svg-gauge";

Vue.use(BootstrapVue);
Vue.use(VueSvgGauge);
Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  render: h => h(App),
  template: "<App/>"
});
