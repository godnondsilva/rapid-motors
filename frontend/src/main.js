import Vue from 'vue';
import App from './App.vue';
import router from './router';
import bootstrap from './plugins/bootstrap';
import store from './store';
import './plugins/validation';

Vue.config.productionTip = false;

new Vue({
	router,
	bootstrap,
	store,
	render: (h) => h(App),
}).$mount('#app');
