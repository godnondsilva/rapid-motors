<template>
  <div class="home">
    <div class="banner-container">
      <img class="banner" src="../assets/home-banner.png" alt="home-banner"/>
      <div class="banner-text">
        <div class="heading">Welcome to Volt Motors!</div>
        <div class="text">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
          tempor incididunt ut labore et dolore magna 
        </div>
        <div class='button'>
          <router-link class="button-text" to="/cars">Book now!</router-link>
        </div>
      </div>
    </div>

    <div class="outer-services">
      <div class="container" style="textAlign: center;">
        <div class="section-heading">Our Services</div>
        <div class="services">
          <div class="service">
            <img src="../assets/home-icons/check-icon.png" alt="check-icon"/>
            <div class="service-heading">Quality Assurance</div>
            <div class="service-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt </div>
          </div>
          <div class="service">
            <img src="../assets/home-icons/car-icon.png" alt="car-icon"/>
            <div class="service-heading">Test Drives</div>
            <div class="service-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt </div>
          </div>
          <div class="service">
            <img src="../assets/home-icons/bolt-icon.png" alt="bolt-icon"/>
            <div class="service-heading">Quick Delivery</div>
            <div class="service-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt </div>
          </div>
        </div>
      </div>
    </div>

    <div class="who-are-we">
      <div class="container">
        <div class="section-heading">Who are we?</div>
        <div class="section-text">
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna 
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
            ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit 
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
            occaecat cupidatat non proident, sunt in culpa qui officia 
            deserunt mollit anim id est laborum."
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
.banner-container {
  position: relative;
}
.banner {
  width: 100%;
}
.banner-text {
  position: absolute;
  top: 26%;
  left: 20%;
  width: 600px;
}
.heading {
  font-size: 3rem;
  font-weight: bold;
  color: #fff;
}
.button {
  background-color: #E4C314;
  width: 120px;
  padding: 6px 10px;
  margin-top: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.button:hover {
  cursor: pointer;
}
.text {
  width: 400px;
  font-size: 1.1rem;
  color: #eee;
  margin-top: 10px;
}

.button-text {
  font-size: 1.1rem;
  color: #000;
  text-decoration: none;
}

.outer-services {
  background-color: #F5F5F5;
  padding: 60px 0 80px 0;
}
.services {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.service {
  width: 280px;
  height: 300px;
  padding: 20px 40px;
  background-color: #fff;
  box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.service-heading {
  font-size: 1.25rem;
  font-weight: bold;
  color: #000;
  padding-top: 20px;
  padding-bottom: 10px;
}
.service-text {
  color: #000;
}

.who-are-we {
  padding: 80px 0;
  text-align: center;
}
.section-heading {
  font-size: 2.2rem;
  font-weight: bold;
  color: #000;
  padding-bottom: 30px;
  text-align: center;
}
.section-text {
  font-size: 1.1rem;
  color: #000;
}
</style>
