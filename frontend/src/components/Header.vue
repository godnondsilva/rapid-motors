<template>
  <div>
    <b-navbar toggleable="xl" class="header">
      <b-navbar-brand>
        <router-link class="nav-heading" :to="{ path: '/' }">
            <img class="logo" src="../assets/logo.png" />
            Volt Motors
        </router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse" />

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ms-auto">
          <b-navbar-nav>
            <b-nav-item class="nav-flex-item">
              <router-link class="nav-item" :to="{ path: '/' }">
                Home
              </router-link>
            </b-nav-item>
            <span class="d-flex">
              <b-nav-item class="nav-flex-item">
                <router-link class="nav-item" :to="{ path: '/about' }">
                  About
                </router-link>
              </b-nav-item>
              <b-nav-item v-if="getUserType!='admin'" class="nav-flex-item">
                <router-link class="nav-item" :to="{ path: '/cars' }">
                  Cars
                </router-link>
              </b-nav-item>

              <span v-if="getSignedInState" style="display: flex;">
                <span v-if="getUserType==='customer'" style="display: flex;">
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: '/booktestdrive' }">
                      Book Testdrive
                    </router-link>
                  </b-nav-item>

                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: `/testdrives/${getCustID}` }">
                      Testdrives
                    </router-link>
                  </b-nav-item>
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: `/bookings/${getCustID}` }">
                      Bookings
                    </router-link>
                  </b-nav-item>
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: '/profile' }">
                      Profile
                    </router-link>
                  </b-nav-item>
                </span>

                <span v-if="getUserType==='admin'"  style="display: flex;">
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: '/modifycars' }">
                      Modify Cars
                    </router-link>
                  </b-nav-item>

                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: `/admintestdrives` }">
                      Testdrives
                    </router-link>
                  </b-nav-item>
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: `/adminbookings` }">
                      Bookings
                    </router-link>
                  </b-nav-item>
                  <b-nav-item class="nav-flex-item">
                    <router-link class="nav-item" :to="{ path: `/admincustomers` }">
                      Customers
                    </router-link>
                  </b-nav-item>
                </span>

                <b-nav-item class="nav-flex-item">
                    <!-- <router-link class="nav-item" :to="{ path: '/login' }"> -->
                      <div class="logout" @click="signOut">Logout</div>
                    <!-- </router-link> -->
                </b-nav-item>
              </span>
              <span v-else style="display: flex;">
                <b-nav-item class="nav-flex-item">
                  <router-link class="nav-item" :to="{ path: '/register' }">
                    Register
                  </router-link>
                </b-nav-item>
                <b-nav-item class="nav-flex-item">
                  <router-link class="nav-item" :to="{ path: '/login' }">
                    Login
                  </router-link>
                </b-nav-item>
              </span>
            </span>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Header',
  computed: {
    ...mapGetters(['getSignedInState', 'getUserType', 'getCustID']),
  },
  methods: {
    ...mapActions(['signOut']),
  },
};
</script>

<style scoped>
.logo {
    width: 50px;
    height: 50px;
    transform: scale(1.4);
}
@media (min-width: 768px) {
    .header {
        padding: 1rem 16rem;
    }
}
@media (max-width: 767px) {
    .header {
        padding: 1rem 2rem;
    }
}
@media (max-width: 600px) {
    .d-flex {
        display: block !important;
    }
}
.nav-heading {
    color: #000 !important;
    text-decoration: none !important;
    display: flex;
    flex-direction: row;
    align-items: center;
    font-weight: 600;
    font-size: 20px;
}
.nav-item {
    padding: 0 4px !important;
    font-size: 18px;
    color: #000;
    font-weight: 600;
    text-decoration: none !important;
}
.logout {
  color: #000;
}
</style>
