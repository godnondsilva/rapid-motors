<template>
    <div class="add-car">
        <div class="add-car-form">
            <div class="add-car-form-header">
                Enter the details of the car you wish to add
            </div>
            <div class="add-car-form-body">
                <validation-observer v-slot="{ invalid, handleSubmit }">
                    <form @submit.prevent="handleSubmit(addCar)">
                        <div class="form-group">
                            <label for="name">Car Name</label>
                            <validation-provider rules="required|min:3|max:30" v-slot="{ errors }">
                                <input type="text" id="name" v-model="localCar.name" placeholder="Enter the name of the car">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="year">Model Year</label>
                            <validation-provider rules="required|year_limit:4" v-slot="{ errors }">
                                <input type="text" id="year" v-model="localCar.year" placeholder="Enter the model year of the car">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="image">Car Image</label>
                            <validation-provider rules="required" v-slot="{ errors, validate }">
                                <input type="file" id="image" @input="validate($event)" name="image" @change="updateImage" accept="image/png, image/jpeg, image/jpg">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="color">Color</label>
                            <validation-provider rules="required|min:3|max:20" v-slot="{ errors }" >
                                <input type="text" id="color" v-model="localCar.color" placeholder="Enter the color of the car">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="price">Price</label>
                            <validation-provider rules="required|min_value:1000|max_value:99999999.99" v-slot="{ errors }">
                                <input type="text" id="price" v-model="localCar.price" placeholder="Enter the price of the car in numbers">
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="description" class="textarea-label">Description</label>
                            <validation-provider rules="required|min:3|max:255" v-slot="{ errors }">
                                <textarea type="text" id="description" v-model="localCar.description" placeholder="Enter the description of the car"></textarea>
                                <div class="text-danger push-right">{{ errors[0] }}</div>
                            </validation-provider>
                        </div>
                        <b-button @click="openModal()" :disabled="invalid" class="btn btn-yellow push-right">Add Car</b-button>

                        <b-modal v-model="show" id="add-car" title="Confirm Car Addition">
                            <p class="my-4">Are you sure you want to add this car?</p>
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
                                    @click="addCar(car)"
                                >
                                    Add Car
                                </b-button>
                            </template>
                        </b-modal>
                    </form>
                </validation-observer>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { ValidationProvider, ValidationObserver } from 'vee-validate';
import axios from 'axios';

export default {
    name: 'AddCar',
    data() {
        return {
            localCar: {
                model_id: '',
                name: '',
                img: '',
                img_name: '',
                price: '',
                year: '',
                color: '',
                description: '',
            },
            show: false,
            car: {},
        }
    },
    components: {
        ValidationObserver,
        ValidationProvider,
    },
    computed: {
        ...mapGetters(['getUser', 'getAdminID']),
    },
    methods: {
        openModal(car) {
            this.show=true;
            this.car = car;
        },
        updateImage(e) {
            console.log(e.target.files[0])
            this.localCar.img = e.target.files[0];
            this.localCar.img_name = e.target.files[0].name;
        },
        async addCar() {
            const formData = new FormData();
            formData.append('img', this.localCar.img, this.localCar.img_name);
            formData.append('name', this.localCar.name);
            formData.append('year', this.localCar.year);
            formData.append('color', this.localCar.color);
            formData.append('price', this.localCar.price);
            formData.append('description', this.localCar.description);
            formData.append('admin_id', this.getAdminID)

            await axios.post('http://localhost:5000/addcar', formData, {
                headers: {
                'Content-Type': 'multipart/form-data'
                },
            })
            .then(() => {
                alert('Car succesfully added!')
                this.$router.push('/modifycars');
            })
            .catch(() => {
                alert('Error adding car!')
            });
            this.show = false;
        }
    }  
}
</script>

<style scoped>
.add-car {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 50px 0 100px 0;
}
.add-car-form {
    background-color: #F5F5F5;
    padding: 50px 200px;
}
.add-car-form-header {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 50px;
    text-align: center;
}
label {
    width: 150px;
    font-weight: 500;
}
.form-group {
    margin-bottom: 30px;
}
input {
    width: 400px;
    height: 35px;
    border: 1px solid #eee;
    padding: 0 10px;
}
textarea {
    width: 600px;
    height: 100px;
    border: 1px solid #eee;
    padding: 10px;
    resize: none;
}
.textarea-label {
    vertical-align: top;
}
.btn-yellow {
    background-color: #E4C314 !important;
    color: #000 !important;
    font-weight: 600;
}
.btn-yellow:disabled {
    background-color: #666 !important;
    color: #fff !important;
}
.push-right {
    margin-left: 150px;
}
.btn-red {
    background-color: #FF918D;
    color: #000;
    font-weight: 600;
}
</style>