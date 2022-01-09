<template>
    <div class="about">
        <div class="banner-container">
            <img class="banner" src="../assets/about-banner.png" alt="home-banner"/>
            <div class="banner-text">
                <div class="heading">Volt Motors</div>
                <div class="text">A Car Showroom Managament System</div>
            </div>
        </div>

        <div class="about-us">
            <div class="container">
                <div class="section-heading">About Us</div>
                <p class="section-text">
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna 
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    Duis aute irure dolor in reprehenderit in voluptate velit 
                    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                    occaecat cupidatat non proident, sunt in culpa qui officia 
                    deserunt mollit anim id est laborum."
                </p>
                <p class="section-text">
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna 
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                    ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    Duis aute irure dolor in reprehenderit in voluptate velit 
                    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
                    occaecat cupidatat non proident, sunt in culpa qui officia 
                    deserunt mollit anim id est laborum."
                </p>
            </div>
        </div>

        <div class="outer-gallery">
            <div class="container" style="textAlign: center;">
                <div class="section-heading">Gallery</div>
                <div class="gallery">
                        <img src="../assets/about-images/img1.png" alt="check-icon"/>
                        <img src="../assets/about-images/img2.png" alt="car-icon"/>
                        <img src="../assets/about-images/img3.png" alt="bolt-icon"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style scoped>
.banner-container {
  position: relative;
}
.banner {
  width: 100%;
}
.banner-text { 
  text-align: center;
  position: absolute;
  top: 35%;
  left: 29%;
}
.heading {
  font-size: 3.5rem;
  font-weight: bold;
  color: #fff;
}
.text {
  font-size: 3rem;
  color: #eee;
  font-weight: 600;
  margin-top: 10px;
}

.about-us {
  padding: 80px 0;
  background-color: #F5F5F5;
  text-align: center;
}
.section-heading {
  font-size: 2.2rem;
  font-weight: bold;
  color: #000;
  padding-bottom: 40px;
  text-align: center;
}
.section-text {
  font-size: 1.1rem;
  color: #000;
}

.outer-gallery {
  padding: 60px 0 80px 0;
}
.gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.image {
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
</style>

