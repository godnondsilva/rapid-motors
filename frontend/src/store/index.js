import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isSignedIn: false,
    user: {},
    cars: [],
    car: {},
    userType: '',
  },
  getters: {
    getSignedInState: state => state.isSignedIn,
    getUserType: state => state.userType,
    getUser: state => state.user,
    getCars: state => state.cars,
    getCar: state => state.car,
    getCustID: state => state.user.cust_id,
    getAdminID: state => state.user.admin_id,
  },
  mutations: {
    loginUser: (state, user) => {
      state.user = user
      state.userType = 'customer'
      state.isSignedIn = true
    },
    loginAdmin: (state, admin) => {
      state.user = admin
      state.userType = 'admin'
      state.isSignedIn = true
    },
    signOut: (state) => {
      state.user = {}
      state.car = {}
      state.isSignedIn = false
      state.userType = ''
      router.push('/login')
    },
    setCars: (state, payload) => {
      state.cars = payload
    },
    routeUpdateCar: (state, payload) => {
      state.car = payload
    },
  },
  actions: {
    async registerUser(_, account) {
      await axios.post('http://localhost:5000/register', account, {
          headers: {
          'Content-Type': 'application/json'
          },
      })
      .then((response) => {
        if(!response.data.error) {
          router.push({ name: 'Login' })
        }
      })
    },

    async loginUser({ commit }, account) {
      await axios.post('http://localhost:5000/login', account, {
          headers: {
          'Content-Type': 'application/json'
          },
      })
      .then((response) => {
        // if the server does not respond with the error object, it means that the user can be authenticated
        if(!response.data.error) {
          const token = response.data.access_token;
          localStorage.setItem('token', token);
          commit('loginUser', response.data);
        }
      })
    },

    async loginAdmin({ commit }, account) {
      await axios.post('http://localhost:5000/loginadmin', account, {
          headers: {
          'Content-Type': 'application/json'
          },
      })
      .then(async (response) => {
          if(!response.data.error) {
            const token = response.data.access_token;
            localStorage.setItem('token', token);
            commit('loginAdmin', response.data);
          }
      })
    },

    signOut({ commit }) {
      commit('signOut');
    },

    async loadCars({commit}) {
      await axios.get('http://localhost:5000/cars')
        .then(response => {
          commit('setCars', response.data)
        })
    },

    async addTestdrive(_, testdrive) {
      await axios.post('http://localhost:5000/booktestdrive', testdrive, {
          headers: {
          'Content-Type': 'application/json'
          },
      })
    },

    async updateProfile(_, account) {
      await axios.put('http://localhost:5000/updateprofile', account, {
          headers: {
          'Content-Type': 'application/json'
          },
      })
    },

    routeUpdateCar({commit}, payload) {
      commit('routeUpdateCar', payload)
    }
  },
})
