import Vue from "vue";
import App from "./App";
import Axios from "axios";
import router from "./router/index";
import config from "../vue.config";
import BootstrapVue from "bootstrap-vue/dist/bootstrap-vue.esm";
import VueSvgGauge from "vue-svg-gauge";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.use(VueSvgGauge);
Vue.prototype.$http = Axios;
Vue.config.productionTip = false;

Axios.defaults.baseURL = config.devServer.proxy;
Axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  render: h => h(App),
  template: "<App/>"
});
