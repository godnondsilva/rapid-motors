<template>
	<div class="home">
		<div class="banner-container">
			<img class="banner" src="../assets/home-banner.png" alt="home-banner" />
			<div class="banner-text">
				<div class="heading">Welcome to Rapid Motors!</div>
				<div class="text">
					Looking to purchase a new car? Look no furthur! Here at rapid motors,
					we have a wide variety of cars to choose from.
				</div>
				<div class="button">
					<router-link class="button-text" to="/cars">Book now!</router-link>
				</div>
			</div>
		</div>

		<div class="outer-services">
			<div class="container" style="textalign: center">
				<div class="section-heading">Our Services</div>
				<div class="services">
					<div class="service">
						<img src="../assets/home-icons/check-icon.png" alt="check-icon" />
						<div class="service-heading">Quality Assurance</div>
						<div class="service-text">
							We provide the best in class quality and service to all our
							customers
						</div>
					</div>
					<div class="service">
						<img src="../assets/home-icons/car-icon.png" alt="car-icon" />
						<div class="service-heading">Test Drives</div>
						<div class="service-text">
							We provide testdrives for our cars so that you can get first hand
							experience of the vehicle before booking it.
						</div>
					</div>
					<div class="service">
						<img src="../assets/home-icons/bolt-icon.png" alt="bolt-icon" />
						<div class="service-heading">Quick Delivery</div>
						<div class="service-text">
							We provide a fast handover experience and delivery of the car to
							your home.
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="who-are-we">
			<div class="container">
				<div class="section-heading">Who are we?</div>
				<div class="section-text">
					We at Rapid Motors aim to provide a hassle free experience for our
					customers. We provide the best in class quality and service for you.
					You can book a testdrive from our online portal. You can also direct
					book the vehicle based on your favorite category. We provide a fast
					handover experience and delivery of the car to your home. Rapid Motors
					is a one stop shop for all your car needs.
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Home',
};
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
	background-color: #e4c314;
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
	background-color: #f5f5f5;
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
	box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
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
