<template>
    <div class="modify-car">
        <div class="modify-car-form">
            <div class="modify-car-form-header">
                Update the details of the car
            </div>
            <div class="modify-car-form-body">
                <validation-observer v-slot="{ invalid, handleSubmit }">
                    <form @submit.prevent="handleSubmit(saveCar)">
                        <div class="form-group">
                            <label for="name">Car Name</label>
                            <validation-provider
                                rules="required|min:3|max:30"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="text"
                                    id="name"
                                    v-model="localCar.name"
                                    :disabled="isDisabled"
                                    placeholder="Enter the name of the car"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="year">Model Year</label>
                            <validation-provider
                                rules="required|year_limit:4"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="text"
                                    id="year"
                                    v-model="localCar.year"
                                    :disabled="isDisabled"
                                    placeholder="Enter the model year of the car"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="image">Car Image</label>
                            <validation-provider v-slot="{ errors }">
                                <input
                                    type="file"
                                    id="image"
                                    name="image"
                                    :disabled="isDisabled"
                                    @change="updateImage"
                                    accept="image/png, image/jpeg, image/jpg"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="color">Color</label>
                            <validation-provider
                                rules="required|min:3|max:20"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="text"
                                    id="color"
                                    v-model="localCar.color"
                                    :disabled="isDisabled"
                                    placeholder="Enter the color of the car"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="price">Price</label>
                            <validation-provider
                                rules="required|min_value:1000|max_value:99999999.99"
                                v-slot="{ errors }"
                            >
                                <input
                                    type="text"
                                    id="price"
                                    v-model="localCar.price"
                                    :disabled="isDisabled"
                                    placeholder="Enter the price of the car in numbers"
                                />
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="category">Category</label>
                            <validation-provider
                                rules="required"
                                v-slot="{ errors }"
                            >
                                <select
                                    id="category"
                                    v-model="localCar.category_id"
                                    :disabled="isDisabled"
                                >
                                    <option
                                        v-for="(category, idx) in categories"
                                        :value="category.category_id"
                                        :key="idx"
                                    >
                                        {{
                                            category.category_id +
                                            " - " +
                                            category.name
                                        }}
                                    </option>
                                </select>
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div class="form-group">
                            <label for="description" class="textarea-label"
                                >Description</label
                            >
                            <validation-provider
                                rules="required|min:3|max:255"
                                v-slot="{ errors }"
                            >
                                <textarea
                                    type="text"
                                    id="description"
                                    v-model="localCar.description"
                                    :disabled="isDisabled"
                                    placeholder="Enter the description of the car"
                                ></textarea>
                                <div class="text-danger push-right">
                                    {{ errors[0] }}
                                </div>
                            </validation-provider>
                        </div>
                        <div>
                            <button
                                v-if="isDisabled === true"
                                class="btn btn-yellow push-right"
                                @click.prevent="isDisabled = false"
                            >
                                Update Car
                            </button>
                            <b-button
                                v-else
                                @click="show = true"
                                class="btn-bg btn-yellow push-right"
                                :disabled="invalid"
                                >Save</b-button
                            >
                        </div>

                        <b-modal
                            v-model="show"
                            id="car-modify-confirm"
                            title="Confirm Car Modification"
                        >
                            <p class="my-4">
                                Are your sure you want to save this car?
                            </p>
                            <template #modal-footer>
                                <b-button
                                    size="md"
                                    class="float-right btn-red"
                                    @click="resetCar()"
                                >
                                    Reset
                                </b-button>
                                <b-button
                                    size="md"
                                    class="float-right btn-yellow"
                                    @click="saveCar()"
                                >
                                    Save
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
import { mapActions, mapGetters } from "vuex";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import axios from "axios";

export default {
    name: "ModifyCar",
    data() {
        return {
            localCar: {
                model_id: "",
                name: "",
                price: "",
                img: undefined,
                img_name: undefined,
                year: "",
                color: "",
                category_id: "",
                description: "",
            },
            dummyCar: {}, // dummyCar is used to check if the user has changed any of the fields
            isDisabled: true,
            show: false,
            hasImageChanged: false,
            categories: [],
        };
    },
    components: {
        ValidationObserver,
        ValidationProvider,
    },
    computed: {
        ...mapGetters(["getCar", "getAdminID"]),
    },
    async beforeMount() {
        this.localCar = this.getCar;
    },
    mounted() {
        this.dummyCar = {
            model_id: this.localCar.model_id,
            name: this.localCar.name,
            price: this.localCar.price,
            year: this.localCar.year,
            color: this.localCar.color,
            category_id: this.localCar.category_id,
            description: this.localCar.description,
        };
        this.loadCategories();
        // Store the list of categories got from the vuex store
        this.categories = this.getCategories();
    },
    methods: {
        ...mapActions(["loadCategories"]),
        // Include the getCategories getter from vuex
        ...mapGetters(["getCategories"]),
        resetCar() {
            this.localCar = this.dummyCar;
            this.isDisabled = true;
            this.show = false;
        },
        updateImage(e) {
            this.localCar.img = e.target.files[0];
            this.localCar.img_name = e.target.files[0].name;
            if (
                this.localCar.img_name === undefined ||
                this.localCar.img_name === ""
            ) {
                this.hasImageChanged = false;
            } else {
                this.hasImageChanged = true;
            }
            console.log(this.hasImageChanged);
        },
        checkUpdate() {
            if (
                this.localCar.model_id !== this.dummyCar.model_id ||
                this.localCar.name !== this.dummyCar.name ||
                this.localCar.price !== this.dummyCar.price ||
                this.localCar.year !== this.dummyCar.year ||
                this.localCar.color !== this.dummyCar.color ||
                this.localCar.category_id !== this.dummyCar.category_id ||
                this.localCar.description !== this.dummyCar.description ||
                this.hasImageChanged === true
            ) {
                return true;
            }
            return false;
        },
        async saveCar() {
            if (this.checkUpdate()) {
                const formData = new FormData();
                if (this.hasImageChanged === true) {
                    formData.append(
                        "img",
                        this.localCar.img,
                        this.localCar.img_name
                    );
                    formData.append("img_name", this.localCar.img_name);
                }
                formData.append("name", this.localCar.name);
                formData.append("year", this.localCar.year);
                formData.append("color", this.localCar.color);
                formData.append("price", this.localCar.price);
                formData.append("category_id", this.localCar.category_id);
                formData.append("description", this.localCar.description);

                await axios.put(
                    `http://localhost:5000/modifycar/${this.$route.params.model_id}`,
                    formData,
                    {
                        headers: {
                            "Content-Type": "multipart/form-data",
                        },
                    }
                );
            }
            this.show = false;
            this.isDisabled = true;
        },
    },
};
</script>

<style scoped>
.modify-car {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 50px 0 100px 0;
}
.modify-car-form {
    background-color: #f5f5f5;
    padding: 50px 200px;
}
.modify-car-form-header {
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
.push-right {
    margin-left: 150px;
}
.btn-yellow {
    background-color: #e4c314 !important;
    color: #000 !important;
    font-weight: 600;
}
.btn-yellow:disabled {
    background-color: #666 !important;
    color: #fff !important;
}
.btn-red {
    background-color: #ff918d;
    color: #000;
    font-weight: 600;
}
input:disabled {
    background-color: #dfdfdf;
}
textarea:disabled {
    background-color: #dfdfdf;
}
</style>