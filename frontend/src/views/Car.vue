<template>
    <div class="car">
        <div class="container">
            <span class="back-button">
                <router-link class="back-link" to="/cars">
                    &lt; Back
                </router-link>
            </span>
            <div class="flex-container">
                <div class="left-container">
                    <img 
                        :src="require(`../../../images/${carData.img_name}`)" 
                        alt="car"
                        width="500px"
                        height="350px"
                    >
                </div>
                <div class="right-container">
                    <div class="heading">
                        Car name: {{ carData.name }}
                    </div>
                    <div class="subheading">
                        Year: {{ carData.year }} |
                        Price: {{ carData.price }} |
                        Color: {{ carData.color }}
                    </div>
                    <div class="description">
                        {{ carData.description }}
                    </div>
                    <b-button @click="show=true" class="btn btn-yellow">Book Now</b-button>

                    <b-modal v-model="show" id="car" title="Confirm your booking">
                        <p class="my-4">Are your sure you want to book this car?</p>
                        <template #modal-footer>
                            <b-button
                                size="md"
                                class="float-right btn btn-red"
                                @click="show=false"
                            >
                                Cancel
                            </b-button>
                            <b-button
                                size="md"
                                class="float-right btn btn-yellow"
                                @click="bookCar(carData)"
                            >
                                Book Now
                            </b-button>
                        </template>
                    </b-modal>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Car',
    data() {
        return {
            carData: [],
            show: false
        }
    },
    methods: {
        async loadCar() {
            await axios.get(`http://localhost:5000/car/${this.$route.params.model_id}`)
            .then((response) => {
                console.log(response.data)
                this.carData = response.data
            })
        },
        async bookCar(carData) {
            this.show = false
            console.log(carData)
            const bookingData = {
                model_id: carData.model_id,
                cust_id: this.$store.state.user.cust_id,
                booking_date: new Date(),
                booking_price: carData.price
            }
            await axios.post(`http://localhost:5000/bookcar`, bookingData)
            .then((response) => {
                this.carData = response.data
                alert('Car booked successfully!')
                this.$router.push(`/bookings/${this.$store.state.user.cust_id}`)
            })
            .catch(() => {
                alert('Error booking car!')
            })
        }
    },
    mounted() {
        this.loadCar()    
    }
}
</script>

<style scoped>
.car {
    margin-top: 50px;
}
.flex-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 50px;
    margin-bottom: 100px;
}
.right-container {
    margin-left: 80px;
    align-self: start;
}
.back-button {
    font-size: 20px;
    padding: 5px 15px;
    border: 1px solid #000;
}
.back-link {
    color: #000;
    font-weight: 600;
    text-decoration: none;
}
.heading {
    font-size: 2.5rem;
    font-weight: bold;
    color: #000;
}
.subheading {
    font-size: 1.5rem;
    color: #000;
    padding-top: 20px;
}
.description {
    padding: 20px 0;
}
.btn {
    padding: 5px 20px;
    border-radius: 5px;
}
.btn-yellow {
    background-color: #E4C314 !important;
    color: #000 !important;
    font-weight: 600;
}
.btn-red {
    background-color: #FF918D;
    color: #000;
}
.btn-red:hover {
    background-color: #FF918D;
    color: #000;
}
</style>