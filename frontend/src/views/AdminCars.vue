<template>
    <div class="admin-cars">
        <!-- <div class="banner-container">
            <img class="banner" src="../assets/cars-banner.png" alt="home-banner"/>
            <div class="banner-text">
                <div class="heading">Book your favourite car today!</div>           
            </div>
        </div> -->

        <div class="all-cars">
            <div class="container">
                <div class="car-item add-car" @click.prevent="routeAddCar()">
                    + Add a new car
                </div>
                <div class="flex-items">
                    <div v-for="(car, idx) in this.getCars" :key="idx" class="car-item">
                        <div class="car-name">
                            {{ car.name }}
                        </div>
                        <div class="car-image">
                            <img class="car-img" :src="require(`../../../images/${car.img_name}`)" alt="car-image"/>
                        </div>
                        <div class="car-details">
                            <div class="car-year">
                                Year: {{ car.year}}
                            </div>
                            <div class="car-color">
                                Color: {{ car.color }}
                            </div>
                            <div class="car-price">
                                Price: Rs. {{ car.price }}
                            </div>
                            <b-button @click="deleteButton(car)" class="btn btn-red right-margin">Delete</b-button>
                            <button type="submit" @click.prevent="routeUpdate(car)" class="btn btn-yellow">Update</button>

                            <b-modal v-model="show" id="modal-1" title="Confirm car deletion">
                                <p class="my-4">Are your sure you want to delete this car?</p>
                                <template #modal-footer>
                                    <b-button
                                        size="md"
                                        class="float-right btn-red"
                                        @click="show=false"
                                    >
                                        Cancel
                                    </b-button>
                                    <b-button
                                        size="md"
                                        class="float-right btn-yellow"
                                        @click="deleteCar()"
                                    >
                                        Delete
                                    </b-button>
                                </template>
                            </b-modal>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'Cars',
    data() {
        return {
            cars: [],
            show: false,
            car: {},
        }
    },
    computed: {
        ...mapGetters(['getCars'])
    },
    mounted() {
        this.loadCars()
    },
    methods: {
        ...mapActions(['loadCars', 'routeUpdateCar']),
        deleteButton(car) {
            this.show=true;
            this.car = car;
        },
        routeUpdate(car) {
            this.routeUpdateCar(car)
            this.$router.push(`/modifycar/${car.model_id}`)
        },
        routeAddCar() {
            this.$router.push('/addcar')
        },
        async deleteCar() {
            await axios.delete(`http://localhost:5000/deletecar/${this.car.model_id}`)
            .then(() => {
                alert('Car deleted successfully!')
                this.loadCars()
            })
            .catch(() => {
                alert('Error deleting car!')
            })
            this.show = false;
        }
    }
}
</script>

<style scoped>
.all-cars {
    margin: 50px 0;
}
.banner-container {
  position: relative;
}
.banner {
  width: 100%;
}
.banner-text { 
  text-align: center;
  position: absolute;
  top: 40%;
  left: 29%;
}
.heading {
  font-size: 3.5rem;
  font-weight: bold;
  color: #fff;
}

.car-img {
    width: 250px;
    height: 150px;
}
.car-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: #F5F5F5;
    padding: 30px 0;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
}
.btn-red {
    background-color: #FF918D !important;
    color: #000 !important;
    font-weight: 600;
}
.btn-yellow {
    background-color: #E4C314 !important;
    color: #000 !important;
    font-weight: 600;
}
.flex-items {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    column-gap: 100px;
    row-gap: 30px;
}
.car-name {
    font-size: 1.5rem;
    font-weight: bold;
    color: #000;
    padding-bottom: 10px;
}
.car-year {
    font-weight: 500;
    color: #000;
    padding-top: 20px;
    padding-bottom: 10px;
}
.car-color {
    font-weight: 500;
    color: #000;
    padding-bottom: 10px;
}
.car-price {
    font-weight: 500;
    color: #000;
    padding-bottom: 20px;
}
.cars-header {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 70px;
    text-align: center;
}
.right-margin {
    margin-right: 15px;
}
.add-car {
    font-size: 18px;
    font-weight: 500;
}
.add-car:hover {
    cursor: pointer;
}
</style>