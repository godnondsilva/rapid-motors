import Vue from 'vue';
import VueRouter from 'vue-router'

// Common routes
import Home from '../views/Home.vue'
import About from '../views/About.vue'

// User routes
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import BookTestdrive from '../views/BookTestdrive.vue'
import Cars from '../views/Cars.vue'
import Car from '../views/Car.vue'
import Testdrives from '../views/Testdrives.vue'
import Bookings from '../views/Bookings.vue'
import ForgotPassword from '../views/ForgotPassword.vue'

// Admin routes
import AdminLogin from '../views/AdminLogin.vue'
import AdminCars from '../views/AdminCars.vue'
import AdminModifyCar from '../views/AdminModifyCar.vue'
import AdminAddCar from '../views/AdminAddCar.vue'
import AdminTestdrives from '../views/AdminTestdrives.vue'
import AdminBookings from '../views/AdminBookings.vue'
import AdminCategories from '../views/AdminCategories.vue'
import AdminCustomers from '../views/AdminCustomers.vue'
import AdminAddCategory from '../views/AdminAddCategory.vue'
import AdminModifyCategory from '../views/AdminModifyCategory.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/cars',
    name: 'Cars',
    component: Cars
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/car/:model_id',
    name: 'Car',
    component: Car
  },
  {
    path: '/booktestdrive',
    name: 'BookTestdrive',
    component: BookTestdrive
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/testdrives/:cust_id',
    name: 'Testdrives',
    component: Testdrives
  },
  {
    path: '/bookings/:cust_id',
    name: 'Bookings',
    component: Bookings
  },
  {
    path: '/forgotpassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  // Admin routes
  {
    path: '/adminlogin',
    name: 'AdminLogin',
    component: AdminLogin
  },
  {
    path: '/addcar',
    name: 'AdminAddCar',
    component: AdminAddCar
  },
  {
    path: '/modifycars',
    name: 'AdminModifyCars',
    component: AdminCars
  },
  {
    path: '/modifycar/:model_id',
    name: 'AdminModifyCar',
    component: AdminModifyCar
  },
  {
    path: '/admintestdrives',
    name: 'AdminTestdrives',
    component: AdminTestdrives
  },
  {
    path: '/adminbookings',
    name: 'AdminBookings',
    component: AdminBookings
  },
  {
    path: '/admincustomers',
    name: 'AdminCustomers',
    component: AdminCustomers
  },
  {
    path: '/admincategories',
    name: 'AdminCategories',
    component: AdminCategories
  },
  {
    path: '/adminaddcategory',
    name: 'AdminAddCategory',
    component: AdminAddCategory
  }
  ,
  {
    path: '/adminmodifycategory/:category_id',
    name: 'AdminModifyCategory',
    component: AdminModifyCategory
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;