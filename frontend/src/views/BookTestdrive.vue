<template>
    <div class="book-testdrive">
        <!-- <div class="banner-container">
            <img class="banner" src="../assets/test-drive-banner.png" alt="home-banner"/>
        </div> -->

        <div class="test-drive">
            <div class="test-drive-form">
                <div class="test-drive-form-header">
                    Book a Test Drive
                </div>
                <div class="test-drive-form-body">
                    <validation-observer v-slot="{ invalid, handleSubmit }">
                        <form @submit.prevent="handleSubmit(submitTestdrive)">
                            <div class="form-group">
                                <label for="model">Model Name</label>
                                <validation-provider rules="required" v-slot="{ errors }">
                                    <select id="model" v-model="selectedModel">
                                        <option value="" disabled>Select a model</option>
                                        <option v-for="(model, idx) in models" :value="model.model_id"  :key="idx">{{ model.model_id + ' - ' + model.name }}</option>
                                    </select>
                                    <div class="text-danger push-right">{{ errors[0] }}</div>
                                </validation-provider>
                                                       
                            </div>
                            <div class="form-group">
                                <label for="State">State</label>
                                    <validation-provider rules="required|min:3|max:20" v-slot="{ errors }">
                                    <input type="text" id="state" v-model="state" placeholder="Enter your state">
                                    <div class="text-danger push-right">{{ errors[0] }}</div>
                                </validation-provider>
                            </div>
                            <div class="form-group">
                                <label for="city">City</label>
                                <validation-provider rules="required|min:3|max:20" v-slot="{ errors }">
                                    <input type="text" id="city" v-model="city" placeholder="Enter your city">
                                    <div class="text-danger push-right">{{ errors[0] }}</div>
                                </validation-provider>
                            </div>
                            <div class="form-group">
                                <label for="comments" class="textarea-label">Comments</label>
                                <validation-provider rules="required|min:3|max:255" v-slot="{ errors }">
                                    <textarea type="text" id="comments" v-model="comments" placeholder="Enter comments or questions here"></textarea>
                                    <div class="text-danger push-right">{{ errors[0] }}</div>
                                </validation-provider>
                            </div>
                            <b-button @click="show=true" :disabled="invalid" class="btn btn-yellow push-right">Book Now</b-button>

                            <b-modal v-model="show" id="book-testdrive" title="Confirm your testdrive booking">
                                <p class="my-4">Are your sure you want to book this car for a testdrive?</p>
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
                                        @click="submitTestdrive(car)"
                                    >
                                        Book Now
                                    </b-button>
                                </template>
                            </b-modal>
                        </form>
                    </validation-observer>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { ValidationProvider, ValidationObserver  } from 'vee-validate';

export default {
    name: 'TestDrive',
    data() {
        return {
            model: '',
            state: '',
            city: '',
            comments: '',
            selectedModel: '',
            models: [],
            show: false,
        }
    },
    components: {
        ValidationObserver,
        ValidationProvider,
    },
    computed: {
        ...mapGetters(['getCars'])
    },
    methods: {
        ...mapActions(['loadCars', 'addTestdrive']),
        submitTestdrive() {
            this.addTestdrive({
                cust_id: this.$store.state.user.cust_id,
                model_id: this.selectedModel,
                state: this.state,
                city: this.city,
                comments: this.comments,
                testdrive_date: new Date(),
            })
            .then(() => {
                alert('Testdrive booked successfully!')
                this.$router.push(`/testdrives/${this.$store.state.user.cust_id}`)
            })
            .catch(() => {
                alert('Error booking testdrive!')
            })
        }
    },
    created() {
        this.loadCars()
        this.getCars.map(model => {
            this.models.push({
                name: model.name,
                model_id: model.model_id
            })
        })
    },
}
</script>

<style scoped>
.banner-container {
  position: relative;
}
.banner {
  width: 100%;
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
/* Form */
.test-drive {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 0 40px 0;
    background-color: #F5F5F5;
}
.test-drive-form {
    padding: 50px 200px;
}
.test-drive-form-header {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 70px;
    text-align: center;
}
label {
    width: 150px;
    font-weight: 500;
}
.form-group {
    margin-bottom: 30px;
}
select {
    width: 600px;
    height: 35px;
    border: 1px solid #eee;
    padding: 0 10px;
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
.btn-red {
    background-color: #FF918D !important;
    color: #000 !important;
    font-weight: 600;
}
.push-right {
    margin-left: 150px;
}
</style>

